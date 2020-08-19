#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:56:50 2020

@author: Elliot
"""

import numpy as np

class L_System():
    
    systems = [{'axiom': 'F', 
                'rules': {'F': 'F[-F]F[+F]', '+': '+', '-': '-', '[': '[', ']': ']'}},
               {'axiom': 'X', 
                'rules': {'F': 'FF', 'X': 'F+[-F-XF-X][+FF][--XF[+X]][++F-X]', '+': '+', '-': '-', '[': '[', ']': ']'}},
               {'axiom': 'X', 
                'rules': {'F': 'FX[FX[+XF]]', 'X': 'FF[+XZ++X-F[+ZX]][-X++F-X]', 'Z': '[+F-X-F][++ZX]', '+': '+', '-': '-', '[': '[', ']': ']'}},
               {'axiom': 'X', 
                'rules': {'F': 'FXF[-F[-FX]+FX]', 'X': 'F++F', '+': '+', '-': '-', '[': '[', ']': ']'}},
               {'axiom': 'X', 
                'rules': {'F': 'FF', 'X': '-F[+F][-X]+F-F[++X]-X', '+': '+', '-': '-', '[': '[', ']': ']'}},
               {'axiom': 'F', 
                'rules': {'F': 'F[-F][+F]', '+': '+', '-': '-', '[': '[', ']': ']'}},
               {'axiom': 'F', 
                'rules': {'F': 'FF+[+F-F-F]-[-F+F+F]', '+': '+', '-': '-', '[': '[', ']': ']'}},
               {'axiom': 'X', 
                'rules': {'X': 'F-[[X]+X]+F[+FX]-X', 'F': 'FF', '+': '+', '-': '-', '[': '[', ']': ']'}},
               {'axiom': 'F', 
                'rules': {'F': 'FF-[XY]+[XY]', 'X': '+FY', 'Y': '-FX', '+': '+', '-': '-', '[': '[', ']': ']'}},
               {'axiom': 'F', 
                'rules': {'F': 'F[+FF][-FF]F[-F][+F]F', '+': '+', '-': '-', '[': '[', ']': ']'}}]
    
    def __init__(self, iterations):
        self.system = np.random.choice(self.systems)
        self.axiom = self.system['axiom']
        self.rules = self.system['rules']
        self.iterations = iterations
        self.instructions = self.create_system()
        
    def processString(self, oldStr):
        newStr = ""
        for ch in oldStr:
            newStr = newStr + self.rules[ch]

        return newStr

    def create_system(self):
        startString = self.axiom
        endString = ""
        for i in range(self.iterations):
            endString = self.processString(startString)
            startString = endString

        return endString