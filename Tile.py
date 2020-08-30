#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:59:37 2020

@author: Elliot
"""

import numpy as np
import alphashape

from Pattern import Pattern
from numpy import linalg as LA
from scipy.spatial import Voronoi
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from descartes import PolygonPatch
from collections import deque

class Tile(Pattern):
    
    def __init__(self, 
                 WIDTH, 
                 HEIGHT, 
                 N, 
                 scale, 
                 noise, 
                 x_shift, 
                 y_shift, 
                 line_width):
         
        super().__init__(WIDTH, HEIGHT)
        
        self.label = 'tile'
        self.fill_shape = False
        
        # shape parameters
        self.N = N
        self.scale = scale
        self.noise = noise
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.line_width = line_width
        
        # shape data
        self.points = deque()
        self.pts_in_poly = None
        self.bounding_poly = None
        
    # creates the polygon that is used to bound grid points
    def create_polygon(self, points):
        alpha_shape = alphashape.alphashape(points, 0)
        poly_path = PolygonPatch(alpha_shape, alpha=0)._path._vertices
        polygon = Polygon(poly_path)
        return polygon

    # generate uniform n x n grid and add gaussian noise to each grid point
    def make_points(self):
        
        # add random shift to alternating rows/columns to create more tiling variations
        def skip_shift(idx, val, shift):
            if idx % 2 == 0:
                val += shift
            val *=  self.scale
            val += np.random.normal(0, self.noise)
            return val
        
        # grid generation
        rand = np.random.choice([0, 1])
        for i in range(self.N):
            for j in range(self.N):
                x_val = skip_shift(i, j, self.x_shift)
                if rand:
                    y_val = skip_shift(j, i, self.y_shift)
                else:
                    y_val = skip_shift(i, i, self.y_shift)
                
                self.points.append(np.array([x_val, y_val], dtype='float64'))
                
        self.points = np.array(self.points)
        
    def filter_points(self):
        
        # create bounding polygon
        n = 12 # just seemed like a good number...
        rand_points = np.random.randint(self.N, size=(n, 2)) * (self.width/10.2)
        polygon = self.create_polygon(rand_points)
        
        # remove grid points outside of polygon
        self.pts_in_poly = np.array([np.array(p) for p in self.points if polygon.contains(Point(p))])
        # create polygon in which lines will be drawn
        self.bounding_poly = self.create_polygon(self.pts_in_poly)
        
    def draw_path(self):
        
        self.make_points()
        
        # scale
        self.points *= (self.width/10)
        
        # filter points not in bounding polygon
        self.filter_points()
            
        # center on middle of grid polygon
        mid_pt = self.points[(self.N * self.N) // 2]
        fst_pt = self.points[0]
        dist = LA.norm(mid_pt - fst_pt)
        self.ctx.translate(self.width - dist*0.7,  self.height - dist*0.7)
            
        # calculate Voronoi tessellation
        vor = Voronoi(self.pts_in_poly)
        
        # draw Voronoi tessellation inside the bounding polygon
        for simplex in vor.ridge_vertices:
            simplex = np.asarray(simplex)
            # filter out -1 (i.e. points at infinity)
            if np.all(simplex >= 0):
                v = vor.vertices[simplex, :]
                # only plot points if they are in the bounding poly
                if self.bounding_poly.contains(Point(*v[0])) and self.bounding_poly.contains(Point(*v[1])):
                    self.ctx.move_to(*v[0])
                    self.ctx.line_to(*v[1])
    
