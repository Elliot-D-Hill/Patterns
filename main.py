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

# set path to data folder
PATH_TO_IMAGE_FOLDER = 'data/images'
PATH_TO_MASKS_FOLDER = 'data/image_masks'

# choose number of images to create
num_images = 20
# only turn this on if you create a small number of images
dispay_images = True 

parameters = Parameters.Parameters()
num_patterns = len(parameters.patterns)
imgs_per_pattern = int(np.ceil(num_images / num_patterns))

# initialize the ranges of all shape parameters
parameters.set_parameters()

# keep track of each pattern type created
indexes = {p: 0 for p in parameters.patterns}

image_count = 0
for i in range(imgs_per_pattern):
    for j in range(num_patterns):
        
        pattern = parameters.patterns[j]
        indexes[pattern] += 1
        idx = indexes[pattern] 
        
        # required because their are two types of spirals implemented
        if pattern == 'spiral':
            if np.random.choice([0,1]):
                pattern = 'archimedean'
            else:
                pattern = 'golden'
        
        random_parameters = parameters.choose_random(pattern)
        
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
    
        shape.filepath = f'{PATH_TO_IMAGE_FOLDER}/{shape.label}{idx}.png'
        shape.maskpath = f'{PATH_TO_MASKS_FOLDER}/{shape.label}_masks{idx}.png'
        
        # an image must be created before a corresponding mask can be created
        shape.create_image()
        shape.create_mask()
    
        if dispay_images:
            
            img = Image(filename=shape.filepath)
            display(img)
    
            mask = Image(filename=shape.maskpath)
            display(mask)
        
        # break out of loops if the requested number of images have been created
        image_count += 1
        if image_count >= num_images:
            break
    if image_count >= num_images:
        break
