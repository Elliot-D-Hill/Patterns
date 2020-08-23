#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:17:20 2020

@author: Elliot
"""


from IPython.display import Image, display
import Parameters
import Spiral
import Tile
import Explosion
import Branch
import numpy as np
import os

# sets the working directory to YOUR_PATH/Patterns
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

PATH_TO_IMAGE_FOLDER = 'data/images'
PATH_TO_MASKS_FOLDER = 'data/image_masks'

dispay_images = True # only turn this on if you create a small number of images...

parameters = Parameters.Parameters()
num_images = 20
num_patterns = len(parameters.patterns)
# the number of images per shape type
imgs_per_class = int(np.ceil(num_images / num_patterns))

# initialize the ranges of all shape parameters
parameters.set_parameters()

indexes = {p: 0 for p in parameters.patterns}

for i in range(imgs_per_class):
    for j in range(num_patterns):
        
        pattern = 'tile'# parameters.patterns[j]
        random_parameters = parameters.choose_random(pattern)
        indexes[pattern] += 1
        
        if pattern == 'golden': # golden spiral
            shape = Spiral.Golden(*random_parameters)
        elif pattern == 'archimedean': # archimedean spiral 
            shape = Spiral.Archimedean(*random_parameters)
        elif pattern == 'explosion': # explosion
            shape = Explosion.Explosion(*random_parameters)
        elif pattern == 'tile': # tile 
            shape = Tile.Tile(*random_parameters)
        elif pattern == 'branch': # branch
            shape = Branch.Branch(*random_parameters)
        
        # set image dimensions
        shape.WIDTH=600
        shape.HEIGHT=600

        filepath = f'{PATH_TO_IMAGE_FOLDER}/{shape.label}{indexes[pattern]}.png'
        shape.filepath = filepath
        shape.is_mask=False
        shape.create_image()
        
        shape.filepath = f'{PATH_TO_MASKS_FOLDER}/{shape.label}{indexes[pattern]}_mask.png'
        shape.is_mask=True
        shape.create_image()
    
        if dispay_images:
            img = Image(filename=filepath)
            display(img)

