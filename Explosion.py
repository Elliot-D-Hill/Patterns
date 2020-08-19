#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:39:03 2020

@author: Elliot
"""

import numpy as np
from Pattern import Pattern


class Explosion(Pattern):
    
    def __init__(self, 
                 degrees, 
                 n_joints, 
                 distance, 
                 offset,
                 offset_noise,
                 shear_sigma, 
                 length_noise, 
                 angle_noise, 
                 line_width):
        
        self.label = 'explosion'
        self.fill_shape = False
        
        # shape parameters
        self.degrees = np.random.choice(degrees)
        self.n_joints = np.random.choice(n_joints)
        self.distance = np.random.choice(distance)
        self.offset = np.random.choice(offset)
        self.offset_noise = np.random.choice(offset_noise)
        self.shear_sigma = shear_sigma
        self.length_noise = np.random.choice(length_noise)
        self.angle_noise = np.random.choice(angle_noise)
        self.line_width = np.random.choice(line_width)

    def draw_line(self, ctx, theta):
        ctx.save()
        self.rotate(ctx, theta)
        self.translate(ctx, 
                       self.offset + np.random.normal(0, self.offset_noise), 
                       self.offset + np.random.normal(0, self.offset_noise), 
                       draw=False)
        for i in range(self.n_joints):
            self.translate(ctx, self.distance + np.random.normal(0, self.angle_noise),
                          self.distance + np.random.normal(0, self.angle_noise))
        ctx.restore()
        ctx.move_to(self.width, self.height)
        
    def make_points(self):
        pass
        
    def draw_path(self, ctx):
        self.shear(ctx, np.random.normal(0, self.shear_sigma), 
                        np.random.normal(0, self.shear_sigma))
        ctx.move_to(self.width, self.height)
        
        theta = 0
        while theta < 2*np.pi:
            degrees_temp = self.degrees + np.random.normal(0, self.angle_noise)
            self.draw_line(ctx, theta)
            theta += degrees_temp * (np.pi / 180)