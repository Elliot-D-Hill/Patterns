#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:11:54 2020

@author: Elliot
"""

from Pattern import Pattern
import numpy as np

class Archimedean(Pattern):
    
    def __init__(self, WIDTH, HEIGHT, width_factor, height_factor):
        super().__init__(WIDTH, HEIGHT, width_factor, height_factor)
        
        # shape parameters
        self.name = 'archimedean'
        self.n_pts = np.random.choice(np.arange(140, 221, 10))
        self.t = np.random.choice(range(15,70)) 
        self.x = np.random.choice(range(3,10)) 
        self.y = np.random.choice(range(3,10))
        self.alpha = np.random.choice(range(1,5))
        self.spiral_width = [0, np.random.choice([0.1, 0.2, 0.3, 0.4, 0.5])]
        self.sigma = None
        self.random_sigma(arr=np.arange(0, 3, 0.2), start=0.5, end=0.1)
        self.line_width = 2
        self.fill_shape = True
        
        # shape data
        self.points = [None] * len(self.spiral_width)
    
    def archimedean_spiral(self, width):
    
        xy_pts = np.zeros((self.n_pts, 2))
        for i in range(self.n_pts):
            t = (i / self.t) * np.pi
            x = (1 + (self.x + width) * t) * np.cos(self.alpha * t) + np.random.normal(0, self.sigma, 1)
            y = (1 + (self.y + width) * t) * np.sin(self.alpha * t) + np.random.normal(0, self.sigma, 1)
            xy_pts[i, 0] = x + (self.WIDTH/2)
            xy_pts[i, 1] = y + (self.HEIGHT/2)

        return xy_pts
        
    def make_points(self):
        for i, width in enumerate(self.spiral_width):
            xy_pts = self.archimedean_spiral(width)
            self.points[i] = xy_pts
    
    def draw_path(self, ctx):
        self.points[1] = self.points[1][::-1]
        ctx.move_to(*self.points[0][0])
        for xy_pts in self.points:
            for p in xy_pts:
                ctx.line_to(*p)
        ctx.close_path()