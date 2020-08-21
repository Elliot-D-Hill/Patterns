#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:47:34 2020

@author: Elliot
"""

import numpy as np
import L_System

from Pattern import Pattern

class Branch(Pattern):
    
    def __init__(self, 
                 n_iter, 
                 degrees, 
                 length, 
                 length_noise, 
                 angle_noise, 
                 line_width):
        
        self.label = 'branch'
        self.fill_shape = False
        
        # shape parameters
        self.system = L_System.L_System(n_iter)
        self.theta = degrees * np.pi / 180
        self.length = length
        self.length_noise = length_noise
        self.angle_noise = angle_noise
        self.line_width = line_width
        
    def reduce_noise_freq(self, randomize):
        ln = 0
        an = 0
    
        if randomize:
            if np.random.uniform(0, 1) < 0.2:
                ln = self.length_noise
            if np.random.uniform(0, 1) < 0.2:
                an = self.angle_noise
        return ln, an
    
    def make_points(self):
        pass
    
    def draw_path(self):        
        
        self.ctx.move_to(self.width, self.height)

        randomize = np.random.uniform(0, 1) < 0.0
        for cmd in self.system.instructions:
            
            ln, an = self.reduce_noise_freq(randomize)
                
            if cmd == 'F': # move forward
                self.translate(self.length + ln, -self.length + ln)
            elif cmd == 'B': # move backward
                self.translate(-self.length + ln, -self.length + ln)
            elif cmd == '+': # rotate left
                self.rotate(self.theta + an)
            elif cmd == '-': # rotate right
                self.rotate(-self.theta + an)
            elif cmd == '[': # save current state
                self.ctx.save()
            elif cmd == ']': # return to last saved state
                self.ctx.restore()
                self.ctx.move_to(self.width, self.height)