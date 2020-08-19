#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:17:20 2020

@author: Elliot
"""
import Golden
import Archimedean
import Tile
import Explosion
import Branch
import numpy as np

from IPython.display import Image, display

pattern='b'
num_imgs = 1

if pattern == 'g': # golden spiral parameters
    N = np.arange(35, 45) # number of samples from golden ratio sequence
    b = np.arange(1, 1.2, 0.01) # how tightly the spirals curves (I think...)
    a = np.arange(1, 3, 0.1) # scaling constant
    step = np.arange(0.18, 0.25, 0.01) # length between samples
    sigma = np.arange(0, 1, 0.5) # noise in xy coordinates
    num_arms = np.arange(1, 11) # number of spiral arms
    line_width = np.arange(0.5, 8, 0.5) # width of each spiral arm
    
elif pattern == 'a': # archimedean spiral parameters
    N = np.arange(140, 231, 10)
    t = np.arange(15,70)
    x = np.arange(3,10)
    y = np.arange(3,10)
    alpha = np.arange(1,5)
    spiral_width = np.arange(0.1, 0.6, 0.1)
    sigma = np.arange(0, 1.5, 0.1)
    
elif pattern == 'e': # explosion parameters
    degrees = np.arange(0.1,15, 0.1)
    n_joints = np.arange(1, 5)
    distance = np.arange(25, 40)
    offset = np.arange(0, 25)
    offset_noise = np.arange(0, 5)
    shear_sigma = 0.3
    length_noise = np.arange(0, 30)
    angle_noise = np.arange(0, 10)
    line_width = np.arange(1, 4, 0.1)

elif pattern == 't': # tile parameters
    n = np.arange(10, 20)
    m = np.arange(10, 20)
    s = np.arange(0, 0.2, 0.05)
    xs = np.arange(0, 0.9, 0.1)
    ys = np.arange(0, 0.9, 0.1)
    line_width = np.arange(1, 6, 0.25)
    
elif pattern == 'b': # branch parameters    
    n_iter=np.arange(2, 4)
    degrees=np.arange(20, 50) 
    distance=np.arange(10, 25) 
    length_noise=np.arange(5, 10) 
    angle_noise=np.arange(np.pi / 100, np.pi / 10, 0.05)
    line_width=np.arange(1, 5) 


for idx in range(num_imgs):
    
    if pattern == 'g': # golden spiral
        shape = Golden.Golden(N=N,
                        b=b,
                        a=a,
                        step=step,
                        sigma=sigma,
                        num_arms=num_arms,
                        line_width=line_width)
        
    elif pattern == 'a': # archimedean spiral 
        shape = Archimedean.Archimedean(N=N,
                                            t=t,
                                            x=x,
                                            y=y,
                                            alpha=alpha,
                                            spiral_width=spiral_width,
                                            sigma=sigma)
        
    elif pattern == 'e': # explosion
        shape = Explosion.Explosion(degrees=degrees,
                                    n_joints=n_joints,
                                    distance=distance, 
                                    offset=offset,
                                    offset_noise=offset_noise,
                                    shear_sigma=shear_sigma,
                                    length_noise=length_noise, 
                                    angle_noise=angle_noise,
                                    line_width=line_width)
        
    elif pattern == 't': # tile 
        shape = Tile.Tile(n=n, 
                          m=m, 
                          s=s, 
                          xs=xs, 
                          ys=ys, 
                          line_width=line_width)
        
    elif pattern == 'b': # branch
        shape = Branch.Branch(n_iter=n_iter, 
                              degrees=degrees, 
                              distance=distance, 
                              length_noise=length_noise, 
                              angle_noise=angle_noise, 
                              line_width=line_width)
    
    # set image dimensions
    shape.WIDTH=600
    shape.HEIGHT=600
    
    shape.create_image(idx)
    
print(f'data/{shape.label}/{shape.label}{idx}.png')
img = Image(filename=f'data/{shape.label}/{shape.label}{idx}.png')
display(img)