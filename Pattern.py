#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:07:13 2020

@author: Elliot
"""

import abc
import cairo
import numpy as np
from numpy import linalg as LA

class Pattern():
    
    __metaclass__ = abc.ABCMeta
    
    WIDTH = 600
    HEIGHT = 600
    width_factor = 0.5
    height_factor = 0.5
    width = WIDTH * width_factor
    height = HEIGHT * height_factor
    is_mask = False
    
    def __init__(self):
        self.ctx = None
        self.surface = None
 
        self.background_color = None
        
    @abc.abstractmethod
    def draw_path(self):
        """Classes which inherit from the pattern class must have the draw_path() method implented"""
        raise("This method must be implemented")
        return
        
    def rotate(self, theta):
        self.ctx.translate(self.width, self.height)
        self.ctx.rotate(theta)
        self.ctx.translate(-self.width, -self.height)

    def translate(self, dx, dy, draw=True):
        self.ctx.translate(dx, dy)
        if draw:
            self.ctx.line_to(self.width, self.height)
        else:
            self.ctx.move_to(self.width, self.height)

    def shear(self, x_shear, y_shear):
        self.ctx.translate(self.width, self.height)
        shear_matrix = cairo.Matrix(1.0, x_shear, y_shear, 1.0)
        self.ctx.transform(shear_matrix)
        self.ctx.translate(-self.width, -self.height)

    def color_background(self):
        
        # set random background color
        self.ctx.rectangle(0, 0, self.WIDTH, self.HEIGHT)
        
        if not self.is_mask:
            background_color = np.random.rand(3)
        else:
            background_color = np.zeros(3)
            
        self.ctx.set_source_rgb(*background_color)
        self.ctx.fill()
        return background_color

    def color_shape(self, background_color, line_width, fill_shape):
    
        # choose random shape color
        if not self.is_mask:
            spiral_color = np.random.rand(3)
        else:
            spiral_color = np.ones(3)
    
        # prevents spiral and background colors from being too similar
        while LA.norm(spiral_color - background_color) < 0.2:
            spiral_color = np.random.rand(3)
    
        self.ctx.set_source_rgb(*spiral_color)
    
        if fill_shape:
            self.ctx.fill()
    
        self.ctx.set_line_width(line_width)
        self.ctx.stroke()
        
    def random_transform(self):
        
        if not self.is_mask:
            rand_x = np.random.normal(0, 30)
            rand_y = np.random.normal(0, 30)
            angle = np.random.uniform(low=0.0, high=360, size=1)
            theta = angle * np.pi / 180
                
            # random shift
            self.ctx.translate(rand_x, rand_y)

            # random rotatation
            self.rotate(theta)

    def create_image(self):
        
        # create pycairo surface and context 
        self.surface = cairo.ImageSurface(cairo.FORMAT_RGB24, self.WIDTH, self.HEIGHT)
        self.ctx = cairo.Context(self.surface)
        
        self.background_color = self.color_background()
        
        # add a random shift and rotation on the original image
        # self.random_transform()
        
        # must be implemented by other shape classes
        self.draw_path()
        
        self.color_shape(self.background_color, self.line_width, self.fill_shape)
        # write image to file
        self.surface.write_to_png(self.filepath)
    