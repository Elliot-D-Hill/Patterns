#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:07:13 2020

@author: Elliot
"""
import cairo
import numpy as np
from numpy import linalg as LA

class Pattern():
    
    def __init__(self, WIDTH, HEIGHT, width_factor, height_factor):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.width_factor = width_factor
        self.height_factor = height_factor
        
    def rotate(self, ctx, theta, w, h):
        ctx.translate(w, h)
        ctx.rotate(theta)
        ctx.translate(-w, -h)

    def translate(self, ctx, d, w, h):
        ctx.translate(d, d)
        ctx.line_to(w, h)

    def shear(self, ctx, x_shear, y_shear, w, h):
        ctx.translate(w, h)
        shear_matrix = cairo.Matrix(1.0, x_shear, y_shear, 1.0)
        ctx.transform(shear_matrix)
        ctx.translate(-w, -h)
        
    def random_sigma(self, arr, start, end):
        p = np.arange(start, end, (end - start) / len(arr))
        p = p / p.sum()
        self.sigma = np.random.choice(arr, p=p)

    def color_background(self, ctx, WIDTH, HEIGHT):
        # set random background color
        ctx.rectangle(0, 0, WIDTH, HEIGHT)
        background_color = np.random.rand(3)
        ctx.set_source_rgb(*background_color)
        ctx.fill()
        return background_color

    def color_shape(self, ctx, background_color, line_width, fill_shape):
    
        # choose random shape color
        spiral_color = np.random.rand(3)
    
        # prevents spiral and background colors from being too similar
        while LA.norm(spiral_color - background_color) < 0.2:
            spiral_color = np.random.rand(3)
    
        ctx.set_source_rgb(*spiral_color)
    
        if fill_shape:
            ctx.fill()
    
        ctx.set_line_width(line_width)
        ctx.stroke()

    def draw_shape(self, idx):
    
        surface = cairo.ImageSurface(cairo.FORMAT_RGB24, self.WIDTH, self.HEIGHT)
        ctx = cairo.Context(surface)

        background_color = self.color_background(ctx, self.WIDTH, self.HEIGHT)

        # set center and add a random shift
        width = self.width_factor * self.WIDTH + np.random.normal(0, 30)
        height = self.height_factor * self.HEIGHT + np.random.normal(0, 30)

        # random rotatation
        angle = np.random.uniform(low=0.0, high=360, size=1)
        theta = angle * np.pi / 180
        self.rotate(ctx, theta, width, height)

        self.draw_path(ctx)

        self.color_shape(ctx, background_color, self.line_width, self.fill_shape)

        surface.write_to_png(f'data/spirals/spiral{idx}.png')
        
    def create_image(self, idx):
        self.make_points()
        self.draw_shape(idx)