#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:36:57 2020

@author: Elliot
"""

# spiral classes implemented: Archimedean, and Golden pirals

from Pattern import Pattern
import numpy as np

class Archimedean(Pattern):
    
    def __init__(self, N, t, x, y, c, alpha, spiral_width, noise):
        
        self.label = 'spiral'
        self.line_width = 2
        self.fill_shape = True
        
        # shape parameters
        self.N = N
        self.t = t
        self.x = x
        self.y = y
        self.c = c
        self.alpha = alpha
        self.spiral_width = [0, spiral_width]
        self.noise = noise
        
        # shape data
        self.points = [None] * len(self.spiral_width)
        
        self.make_points()
    
    def archimedean_spiral(self, width):
    
        xy_pts = np.zeros((self.N, 2))
        for i in range(self.N):
            t = (i / self.t) * np.pi
            x = (self.c + (self.x + width) * t) * np.cos(self.alpha * t)
            y = (self.c + (self.y + width) * t) * np.sin(self.alpha * t)
            xy_pts[i, 0] = x + (self.WIDTH/2) + (np.log(i+1) * np.random.normal(0, self.noise, 1))
            xy_pts[i, 1] = y + (self.HEIGHT/2) + (np.log(i+1) * np.random.normal(0, self.noise, 1))

        return xy_pts
        
    def make_points(self):
        for i, width in enumerate(self.spiral_width):
            xy_pts = self.archimedean_spiral(width)
            self.points[i] = xy_pts
    
    def draw_path(self):
        if not self.is_mask:
            self.points[1] = self.points[1][::-1]
        self.ctx.move_to(*self.points[0][0])
        for xy_pts in self.points:
            for p in xy_pts:
                self.ctx.line_to(*p)
        self.ctx.close_path()
        
        
class Golden(Pattern):
    
    def __init__(self, N, b, a, step, noise, num_arms, line_width):
        
        self.label = 'spiral'
        self.fill_shape = False
        
        # shape parameters
        self.N = N
        self.b = b
        self.a = a
        self.step = step
        self.noise = noise
        self.num_arms = num_arms
        self.line_width = line_width
        
        # shape data
        self.points = None
        self.thetas = []
        
        self.make_points()
            
    def golden_spiral(self):
        
        # used to scale the xy coordinate noise
        def logistic_curve(l, k, x, x0):
            y = l / (1 + np.exp(-k * (x - x0)))
            return y
    
        def curve(arr, theta):
            xy_pts = [None] * len(theta)
            for i, (r, t) in enumerate(zip(arr, theta)):
                noise = logistic_curve(20, 0.3, i, 30) * np.random.normal(0, self.noise)
                xy_pts[i] = np.array([r * np.cos(t) + noise,
                                      r * np.sin(t)+ noise])
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
    
    def draw_path(self):
        for t in self.thetas:
            self.ctx.move_to(*self.points[0])
            for p in self.points:
                self.ctx.line_to(*p)
            self.rotate(t)