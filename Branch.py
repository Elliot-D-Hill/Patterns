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
                 distance, 
                 length_noise, 
                 angle_noise, 
                 line_width):
        
        self.label = 'branch'
        self.fill_shape = False
        
        self.system = L_System.L_System(np.random.choice(n_iter))
        self.theta = np.random.choice(degrees) * np.pi / 180
        self.distance = np.random.choice(distance)
        self.length_noise = np.random.choice(length_noise)
        self.angle_noise = np.random.choice(angle_noise)
        self.line_width = np.random.choice(line_width)
        
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
    
    def draw_path(self, ctx):
        ctx.move_to(self.width, self.height)

        randomize = np.random.uniform(0, 1) < 0.6
        for cmd in self.system.instructions:
            
            ln, an = self.reduce_noise_freq(randomize)
                
            if cmd == 'F': # move forward
                self.translate(ctx, self.distance + ln, -self.distance + ln)
            elif cmd == 'B': # move backward
                self.translate(ctx, -self.distance + ln, -self.distance + ln)
            elif cmd == '+': # rotate left
                self.rotate(ctx, self.theta + an)
            elif cmd == '-': # rotate right
                self.rotate(ctx, -self.theta + an)
            elif cmd == '[': # save current state
                ctx.save()
            elif cmd == ']': # return to last saved state
                ctx.restore()
                ctx.move_to(self.width, self.height)