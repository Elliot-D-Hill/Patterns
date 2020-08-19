#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:11:54 2020

@author: Elliot
"""

from Pattern import Pattern
import numpy as np

class Archimedean(Pattern):
    
    def __init__(self, N, t, x, y, alpha, spiral_width, sigma):
        
        self.label = 'spiral'
        self.line_width = 2
        self.fill_shape = True
        
        # shape parameters
        self.N = np.random.choice(N)
        self.t = np.random.choice(t) 
        self.x = np.random.choice(x) 
        self.y = np.random.choice(y)
        self.alpha = np.random.choice(alpha)
        self.spiral_width = [0, np.random.choice(spiral_width)]
        self.sigma = sigma
        self.random_sigma(arr=self.sigma, start=0.5, end=0.1)
        
        # shape data
        self.points = [None] * len(self.spiral_width)
    
    def archimedean_spiral(self, width):
    
        xy_pts = np.zeros((self.N, 2))
        for i in range(self.N):
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