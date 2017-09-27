# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:14:59 2017

@author: 13383861
"""

from Coordinate import Coord
from Environment import GridEnvironment

class GridPawn:
    
    def __init__(self, coord:Coord, environment:GridEnvironment):
        '''initialises the pawn's environment and places the pawn in the environment'''
        self.environment = environment
        if(self.environment.coord_occupied(coord)):
            raise Exception('Coordinate {} is already occupied', coord.__str__())
        else:
            self.environment.place_pawn(self, coord)
            self.current_coord = coord
            
    
    def move(self, coord):
        try:
            self.environment.move_pawn(coord)
            self.current_coord = coord
        except Exception as e:
            print(e)
            