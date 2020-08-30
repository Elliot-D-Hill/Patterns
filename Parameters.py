#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 08:25:30 2020

@author: Elliot
"""

import numpy as np

class Parameters():
    
    def __init__(self):
        
        self.patterns = ['spiral', 'explosion', 'tile', 'branch']
        self.parameters = {p: None for p in self.patterns}
        self.set_parameters()
    
    def set_parameters(self):
        
        # golden spiral parameters
        N = np.arange(35, 45) # number of points in spiral sequence
        b = np.arange(1, 1.2, 0.01) # how tightly the spirals curves (I think...)
        a = np.arange(1.5, 2.5, 0.05) # scaling constant
        step = np.arange(0.16, 0.25, 0.01) # length between samples
        noise = np.arange(0, 0.2, 0.05) # noise in xy coordinates
        num_arms = np.arange(1, 11) # number of spiral arms
        line_width = np.arange(3, 8, 0.1) # width of each spiral arm
            
        self.parameters['golden'] = [N, b, a, step, noise, num_arms, line_width]
            
        # archimedean spiral parameters
        N = np.arange(140, 231, 10) # number of points in spiral sequence
        t = np.arange(10, 70) # affects smoothness of spiral
        x = np.arange(3, 10) # scale of x points
        y = np.arange(3, 10) # scale of y points
        c = np.arange(0, 40) # distance of intial point to spiral center
        alpha = np.arange(1, 4, 0.1) # number of loops (I think...)
        spiral_width = np.arange(0.5, 1, 0.01) # width of spiral arm
        noise = np.arange(0, 0.25, 0.01) # noise in x and y
        
        self.parameters['archimedean'] = [N, t, x, y, c, alpha, spiral_width, noise]
            
        # explosion parameters
        degrees = np.arange(0.5,15, 0.1) # number of degrees between arms
        n_joints = np.arange(1, 5) # number of joints per arm
        length = np.arange(25, 35, 0.1) # length between each arm joint 
        length_noise = np.arange(0, 30)
        offset = np.arange(0, 25) # how far away each arm is from the center
        offset_noise = np.arange(0, 5)
        angle_noise = np.arange(0, 10)
        line_width = np.arange(2, 4, 0.1)
        
        self.parameters['explosion'] = [degrees, n_joints, length, length_noise, offset, offset_noise, angle_noise, line_width]
    
        # tile parameters
        N = np.arange(10, 21) # grid size in x dimension
        scale = np.arange(0.5, 1.5, 0.05) # scales space between grid points
        noise = np.arange(0, 0.08, 0.001) # noise of grid points
        x_shift = np.arange(0, 0.7, 0.01) # shifts alternating rows
        y_shift = np.arange(0, 0.7, 0.01) # shifts alternating columns
        line_width = np.arange(2, 8, 0.25)

        self.parameters['tile'] = [N, scale, noise, x_shift, y_shift, line_width]
            
        # branch parameters    
        n_iter=np.arange(2, 4) # number of L-system iterations
        degrees=np.arange(20, 50) # degrees turned per L-system instruction
        length=np.arange(10, 25) # distance moved per L-system instruction
        length_noise=np.arange(5, 10) 
        angle_noise=np.arange(np.pi / 180, np.pi / 20, 0.05)
        line_width=np.arange(2.5, 5, 0.1)
            
        self.parameters['branch'] = [n_iter, degrees, length, length_noise, angle_noise, line_width]
        
    def choose_random(self, pattern):
        params = self.parameters[pattern]
        random_parameters = [None] * len(params)
        for i, p in enumerate(params):
            random_parameters[i] = np.random.choice(p)
        return random_parameters
            