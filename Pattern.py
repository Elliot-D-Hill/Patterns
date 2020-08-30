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
from PIL import Image

class Pattern():
    
    __metaclass__ = abc.ABCMeta

    
    def __init__(self, WIDTH, HEIGHT, width_factor=0.5, height_factor=0.5):
        self.ctx = None
        self.surface = None
        self.background_color = None
        self.shape_color = None
        self.filepath = None
        self.maskpath = None
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.width_factor = width_factor
        self.height_factor = height_factor
        self.width = self.WIDTH * width_factor
        self.height = self.HEIGHT * height_factor
        
    @abc.abstractmethod
    def draw_path(self):
        """Classes which inherit from the pattern class must have the draw_path() method implented"""
        raise('draw_path() method must be implemented for classes that inherit from the Pattern class')
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
        
        self.background_color = np.random.randint(0, 256, 3)
            
        self.ctx.set_source_rgb(*self.background_color/255)
        self.ctx.fill()

    def color_shape(self, line_width, fill_shape):
    
        # choose random shape color
        self.shape_color = np.random.randint(0, 256, 3)
    
        # prevents spiral and background colors from being too similar
        while LA.norm(self.shape_color - self.background_color) < 40:
            self.shape_color = np.random.randint(0, 256, 3)
    
        self.ctx.set_source_rgb(*self.shape_color/255)
    
        if fill_shape:
            self.ctx.fill()
    
        self.ctx.set_line_width(line_width)
        self.ctx.stroke()
        
    def random_transform(self):
        
        rand_x = np.random.normal(0, 30)
        rand_y = np.random.normal(0, 30)
        angle = np.random.uniform(low=0.0, high=360, size=1)
        theta = angle * np.pi / 180
        x_shear_noise = np.random.normal(0, 0.25)
        y_shear_noise = np.random.normal(0, 0.25)
            
        # random shift
        self.ctx.translate(rand_x, rand_y)

        # random rotatation
        self.rotate(theta)
        
        # random shear
        self.shear(x_shear_noise, y_shear_noise)

    def create_image(self):
        
        # create pycairo surface and context 
        self.surface = cairo.ImageSurface(cairo.FORMAT_RGB24, self.WIDTH, self.HEIGHT)
        self.ctx = cairo.Context(self.surface)
        
        self.color_background()
        
        # add a random shift, rotation, and shear
        self.random_transform()
        
        # must be implemented by classes that inherit from Pattern
        self.draw_path()
        
        self.color_shape(self.line_width, self.fill_shape)
        # write image to file
        self.surface.write_to_png(self.filepath)
        
        
    def create_mask(self, pattern_labels):
        
        if not self.filepath:
            raise("An image must be create before a mask can be created")
            
        # open image and convert to array
        mask = Image.open(self.filepath)
        mask = np.array(mask)
        
        # convert to boolean array
        mask = np.all(mask == self.shape_color, axis=-1)
        
        # convert to int
        mask = mask.astype(np.uint8) * pattern_labels[self.label]
        
        img = Image.fromarray(mask)
        img.save(self.maskpath)
            
    