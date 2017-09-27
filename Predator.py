# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:27:28 2017

@author: 13383861
"""
from Coordinate import Coord
from Environment import GridEnvironment
from GridPawn import GridPawn

class Predator(GridPawn):
    def __init__(self,coordinate: Coord, environment: GridEnvironment, perception_radius = 4):
        self._beliefs = []
        self.environment = environment
        if(self.environment.get_coord_details()):
            raise Exception('Coordinate {} is already occupied', coordinate.__str__())
        if coordinate in self.environment.coordinates:
            #self.environment.
            self.coordinate = Coord(x_coord, y_coord, True)
        else:
            raise Exception('Coordinate out of bounds')
        self.perception_radius = perception_radius
        self.perceived_prey_position = None
    
    def actuate(self):
        #call move
        pass
    
    def move(self, new_coordinate):
        if new_coordinate in environment.coordinates and not self.environment.get_coord_details:
            #check the coordinate is not yet occupied and not out of bounds
            self.coordinate = new_coordinate
        else:
            raise Exception('Invalid coordinate choice')
    
    def perceive(self):
        '''Updates prey position if prey is within perception_radius squares'''
        
       
    def get_coordinates(self):
        return (coordinate.get_x(), coordinate.get_y())
    
    def recieve_message(self):
        pass
    
    def send_message(self):
        pass