# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:27:28 2017

@author: 13383861
"""
from GridPawnEnvironmentTest import GridPawn, GridEnvironment
from Prey import Prey
from Coordinate import Coord

class Predator(GridPawn):
    def __init__(self, name, coordinate: Coord, environment: GridEnvironment, perception_radius = 3):
        '''Creates a predator that can pervieve 3 blocks NESW. If anything comes into range while the predator is alive, it knows
        that it exists but may not be able to keep track of its position if the predator moves out of perception range.'''
        super().__init__(coordinate, environment)
        #no idea where prey is at first, no idea where other predators are either
        self._beliefs = {'prey': {}, 'other_pred_pos':{}}
        self.perception_radius = perception_radius
        self.perceived_prey_position = None
        self.name = 'Pd'+name
    
    def actuate(self):
       '''Does something to the environment'''
       pass

    def perceive_grid_coord(self, coord:Coord):
        grid_coord = self.environment._get_coord(coord)
        if grid_coord.get_occupied():
            if isinstance(grid_coord.occupied_val, Prey):
                self.beliefs['prey_pos'] = grid_coord
            elif isinstance(grid_coord.occupied_val, Predator):
                self.beliefs['other_pred_pos'][grid_coord.occupied_val] = grid_coord.occupied_val.current_coord
                
            
    def grid_pawn_in_radius(self, pawn:GridPawn):
        if pawn.current_coord._x-3<=self.current_coord._x <= coord._x +3:
            if coord._y-3<=self.current_coord._y<=coord._y+3:
                return True
            else:
                return False
            
            
        
        
    def perceive(self):
        '''Updates prey/other predator position if prey is within perception_radius squares'''
        for grid_pawn in self.env.grid_pawns:
            if isinstance(grid_pawn, Predator):
                #update position if detected in radius
                if self.coord_in_radius(grid_pawn):
                    self.beliefs['other_pred_pos'][grid_pawn] = grid_pawn.current_coord
                else:
                    #if predator grid pawn has already been detected, update position to unkown
                    if grid_pawn in self._beliefs['other_pred_pos']:
                        self._beliefs['other_pred_pos'][grid_pawn] = None
                        
            elif isinstance(grid_pawn, Prey):
                 if self.coord_in_radius(grid_pawn)       
         
        
        
    def recieve_message(self):
        '''Receives message from other predator(s)'''
        pass
    
    def send_message(self):
        '''sends message to other predator(s)'''
        pass