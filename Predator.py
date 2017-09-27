# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:27:28 2017

@author: 13383861
"""
from GridPawnEnvironmentTest import GridPawn, GridEnvironment
from Coordinate import Coord

class Predator(GridPawn):
    def __init__(self,coordinate: Coord, environment: GridEnvironment, perception_radius = 4):
        super().__init__(coordinate, environment)
        self._beliefs = []
        self.perception_radius = perception_radius
        self.perceived_prey_position = None
    
    def actuate(self):
       '''Does something to the environment'''
       pass

    def perceive(self):
        '''Updates prey position if prey is within perception_radius squares'''
        pass
        
    def recieve_message(self):
        '''Receives message from other predator(s)'''
        pass
    
    def send_message(self):
        '''sends message to other predator(s)'''
        pass