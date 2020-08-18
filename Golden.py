#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:14:41 2020

@author: Elliot
"""

from Pattern import Pattern
import numpy as np

class Golden(Pattern):
    
    def __init__(self, WIDTH, HEIGHT, width_factor, height_factor):
        super().__init__(WIDTH, HEIGHT, width_factor, height_factor)
        
        # shape parameters
        self.label = 'spiral'
        self.N = np.random.choice(np.arange(25, 45, 1))
        self.b = np.random.choice(np.arange(1, 1.2, 0.01))
        self.a = np.random.choice(np.arange(1, 4, 0.1))
        self.step = np.random.choice(np.arange(0.18, 0.25, 0.01))
        self.sigma = None
        self.random_sigma(arr=np.arange(0, 3, 0.2), start=0.5, end=0.1)
        self.num_arms = np.random.choice(np.arange(1, 10, 1))
        self.line_width = np.random.choice(np.arange(0.5, 5, 0.5))
        self.fill_shape = False
        
        # shape data
        self.points = None
        self.thetas = []
            
    def golden_spiral(self):
    
        def curve(arr, theta):
            xy_pts = [None] * len(theta)
            for i, (r, t) in enumerate(zip(arr, theta)):
                xy_pts[i] = np.array([r * np.cos(t), r * np.sin(t)])

            xy_pts = np.array(xy_pts)
            return xy_pts

        def golden(theta, a, b):
            r = a * np.exp(theta *  (1 / np.tan(b)))
            return r

        theta = np.zeros(self.N)
        t = 0
        for i in range(self.N):
            theta[i] = t
            t += self.step

        arr = np.zeros(self.N)
        for i, t in enumerate(theta):
            arr[i] = golden(t, self.a, self.b)

        xy_pts = curve(arr, theta).reshape(-1, 2)
        xy_pts[:, 0] = xy_pts[:, 0] + (self.WIDTH/2)
        xy_pts[:, 1] = xy_pts[:, 1] + (self.HEIGHT/2)

        return xy_pts
            
    def make_points(self):
        degree = 360 / self.num_arms
        theta = degree * (np.pi / 180)
        d = 0
        while d < 360:
            d += degree
            self.thetas.append(theta)
        self.points = self.golden_spiral()
    
    def draw_path(self, ctx):
        for t in self.thetas:
            ctx.move_to(*self.points[0])
            for p in self.points:
                ctx.line_to(*p)
            self.rotate(ctx, t, self.WIDTH/2, self.HEIGHT/2)