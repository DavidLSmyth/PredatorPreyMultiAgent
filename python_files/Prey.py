# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:39:04 2017

@author: 13383861
"""
from GridAbstractions import GridPawn, GridEnvironment
from Coordinate import Coord
    
class Prey:
    def __init__(self, name, coordinate: Coord, environment: GridEnvironment, perception_radius = 3):
        '''Creates a prey that can pervieve 2 blocks NESW. If anything comes into range while the predator is alive, it knows
        that it exists but may not be able to keep track of its position if the predator moves out of perception range.'''
        super().__init__(coordinate, environment)
        #no idea where predators are at first, no idea where other prey are either
        self._beliefs = {'other_pred_pos':{}}
        self.perception_radius = perception_radius
        self.hunted = False
        self.name = 'Py'+name
    
    def move(self):
        pass