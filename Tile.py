#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:59:37 2020

@author: Elliot
"""

import cairo
import numpy as np
import alphashape

from Pattern import Pattern
from numpy import linalg as LA
from scipy.spatial import Voronoi
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from descartes import PolygonPatch

class Tile(Pattern):
    
    def __init__(self, n, m, s, xs, ys, line_width):
        
        self.label = 'tile'
        self.fill_shape = False
        
        # shape parameters
        self.n = np.random.choice(n)
        self.m = np.random.choice(n)
        self.s = np.random.choice(s)
        self.xs = np.random.choice(xs)
        self.ys = np.random.choice(ys)
        self.line_width = np.random.choice(line_width)
        
        # shape data
        self.points = [] # FIXME make is so that you don't have to append (very slow)
        
    def create_polygon(self, points):
        alpha_shape = alphashape.alphashape(points, 0)
        poly_path = PolygonPatch(alpha_shape, alpha=.2)._path._vertices
        polygon = Polygon(poly_path)
        return polygon

    # generate uniform n x m grid and add gaussian noise to each grid point
    def make_points(self):
        
        for i in range(self.n):
            if i % 2 == 0:
                x_shift = 0
            else:
                x_shift = self.xs
            for j in range(self.m):
                if j % 2 == 0:
                    y_shift = 0
                else:
                    y_shift = self.ys
                self.points.append([i + np.random.normal(0, self.s) + y_shift, 
                               j + np.random.normal(0, self.s) + x_shift])
        self.points = np.array(self.points)
        
    def draw_path(self, ctx):
        
        # scale, center, and add random translation
        self.points *= (self.width/10)
        mid_pt = self.points[(self.n * self.m) // 2]
        fst_pt = self.points[0]
        dist = LA.norm(mid_pt - fst_pt)
        ctx.translate(self.width - (dist/1.5) + np.random.normal(0, 20), 
                      self.height - (dist/1.5) + np.random.normal(0, 20) + 50)
    
        # create bounding polygon
        N = 12 # just seemed like a good number...
        rand_points = np.random.randint(self.m, size=(N, 2)) * (self.width/10.2)
        
        polygon = self.create_polygon(rand_points)
    
        # remove grid points outside of polygon
        pts_in_poly = np.array([list(p) for p in self.points if polygon.contains(Point(p))])
        
        # create polygon in which lines will be drawn
        bounding_poly = self.create_polygon(pts_in_poly)
            
        # calculate Voronoi tessellation
        vor = Voronoi(pts_in_poly)
        
        # draw Voronoi tessellation inside bounding polygon
        for simplex in vor.ridge_vertices:
            simplex = np.asarray(simplex)
            if np.all(simplex >= 0):
                v = vor.vertices[simplex, :]
                if bounding_poly.contains(Point(*v[0])) and bounding_poly.contains(Point(*v[1])):
                    ctx.move_to(*v[0])
                    ctx.line_to(*v[1])
    