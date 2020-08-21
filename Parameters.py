#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 08:25:30 2020

@author: Elliot
"""

import numpy as np

class Parameters():
    
    def __init__(self):
        
        self.patterns = ['golden', 'archimedean', 'explosion', 'tile', 'branch']
        self.parameters = {p: None for p in self.patterns}
        self.set_parameters()
    
    def set_parameters(self):
        
        # golden spiral parameters
        N = np.arange(32, 45) # number of points in spiral sequence
        b = np.arange(1, 1.2, 0.01) # how tightly the spirals curves (I think...)
        a = np.arange(1, 3, 0.1) # scaling constant
        step = np.arange(0.16, 0.25, 0.01) # length between samples
        noise = np.arange(0, 0.2, 0.05) # noise in xy coordinates
        num_arms = np.arange(1, 11) # number of spiral arms
        line_width = np.arange(0.5, 8, 0.5) # width of each spiral arm
            
        self.parameters['golden'] = [N, b, a, step, noise, num_arms, line_width]
            
        # archimedean spiral parameters
        N = np.arange(140, 231, 10) # number of points in spiral sequence
        t = np.arange(10, 80) # affects smoothness of spiral
        x = np.arange(3,10) # scale of x points
        y = np.arange(3,10) # scale of y points
        c = np.arange(1, 40) # size of center
        alpha = np.arange(1, 4, 0.1) # number of loops
        spiral_width = np.arange(0.15, 0.8, 0.05)
        noise = np.arange(0, 0.25, 0.01) # <------- FIXME sigma doesn't add noise???
        
        self.parameters['archimedean'] = [N, t, x, y, c, alpha, spiral_width, noise]
            
        # explosion parameters
        degrees = np.arange(0.1,15, 0.1)
        n_joints = np.arange(1, 5)
        length = np.arange(25, 40)
        length_noise = np.arange(0, 30)
        offset = np.arange(0, 25)
        offset_noise = np.arange(0, 5)
        shear_noise = [0.3]
        angle_noise = np.arange(0, 10)
        line_width = np.arange(1, 4, 0.1)
        
        self.parameters['explosion'] = [degrees, n_joints, length, length_noise, offset, offset_noise, shear_noise, angle_noise, line_width]
    
        # tile parameters
        N = np.arange(10, 21) # grid size in x dimension
        scale = np.arange(0.6, 1.1, 0.05)
        noise = np.arange(0, 0.16, 0.01)
        x_shift = np.arange(0, 1.01, 0.01)
        y_shift = np.arange(0, 0.7, 0.01)
        line_width = np.arange(1, 10, 0.25)

        self.parameters['tile'] = [N, scale, noise, x_shift, y_shift, line_width]
            
        # branch parameters    
        n_iter=np.arange(2, 4)
        degrees=np.arange(20, 50) 
        length=np.arange(10, 25) 
        length_noise=np.arange(5, 10) 
        angle_noise=np.arange(np.pi / 100, np.pi / 10, 0.05)
        line_width=np.arange(1, 5)
            
        self.parameters['branch'] = [n_iter, degrees, length, length_noise, angle_noise, line_width]
        
    def choose_random(self, pattern):
        params = self.parameters[pattern]
        random_parameters = [None] * len(params)
        for i, p in enumerate(params):
            random_parameters[i] = np.random.choice(p)
        return random_parameters
            