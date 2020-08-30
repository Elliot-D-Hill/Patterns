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
                 WIDTH, 
                 HEIGHT,
                 degrees, 
                 n_joints, 
                 length, 
                 length_noise, 
                 offset,
                 offset_noise,
                 angle_noise, 
                 line_width):
        
        super().__init__(WIDTH, HEIGHT)

        self.label = 'explosion'
        self.fill_shape = False
        
        # shape parameters
        self.degrees = degrees
        self.n_joints = n_joints
        self.length = length
        self.offset = offset
        self.offset_noise = offset_noise
        self.length_noise = length_noise
        self.angle_noise = angle_noise
        self.line_width = line_width

    def draw_line(self, theta):
        self.ctx.save()
        self.rotate(theta)
        self.translate(self.offset + np.random.normal(0, self.offset_noise), 
                       self.offset + np.random.normal(0, self.offset_noise), 
                       draw=False)
        for i in range(self.n_joints):
            self.translate(self.length + np.random.normal(0, self.angle_noise),
                          self.length + np.random.normal(0, self.angle_noise))
        self.ctx.restore()
        self.ctx.move_to(self.width, self.height)
        
    def make_points(self):
        pass
        
    def draw_path(self):
        
        self.ctx.move_to(self.width, self.height)
        
        theta = 0
        while theta < 2*np.pi:
            degrees_temp = self.degrees + np.random.normal(0, self.angle_noise)
            self.draw_line(theta)
            theta += degrees_temp * (np.pi / 180)