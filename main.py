#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:17:20 2020

@author: Elliot
"""

import Golden
import Archimedean
import IPython.display
from IPython.display import Image

num_imgs = 10

WIDTH=600
HEIGHT=600
width_factor = 0.5
height_factor = 0.5

for idx in range(num_imgs):
    spiral = Archimedean.Archimedean(WIDTH, HEIGHT, width_factor, height_factor)
    # spiral = Golden.Golden(WIDTH, HEIGHT, width_factor, height_factor)
    spiral.create_image(idx)
    
a = Image(filename='data/spirals/spiral0.png')
# b = Image(filename='data/spirals/spiral1.png')
# c = Image(filename='data/spirals/spiral2.png')
display(a) #b, c