#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:14:41 2020

@author: Elliot
"""

from Pattern import Pattern
import numpy as np

class Golden(Pattern):
    
    def __init__(self, N, b, a, step, sigma, num_arms, line_width):
        
        self.label = 'spiral'
        self.fill_shape = False
        
        # shape parameters
        self.N = np.random.choice(N)
        self.b = np.random.choice(b)
        self.a = np.random.choice(a)
        self.step = np.random.choice(step)
        self.sigma = sigma
        self.random_sigma(arr=self.sigma, start=0.5, end=0.1)
        self.num_arms = np.random.choice(num_arms)
        self.line_width = np.random.choice(line_width)
        
        # shape data
        self.points = None
        self.thetas = []
            
    def golden_spiral(self):
    
        def curve(arr, theta):
            xy_pts = [None] * len(theta)
            for i, (r, t) in enumerate(zip(arr, theta)):
                xy_pts[i] = np.array([r * np.cos(t) + np.random.normal(0, self.sigma), 
                                      r * np.sin(t) + np.random.normal(0, self.sigma)])

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
        xy_pts[:, 0] = xy_pts[:, 0] + self.width
        xy_pts[:, 1] = xy_pts[:, 1] + self.height

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
            self.rotate(ctx, t)
            