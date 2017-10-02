# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:27:28 2017

@author: 13383861
"""

import operator

from GridAbstractions import GridPawn, GridEnvironment
from Prey import Prey
from Coordinate import Coord

class Predator(GridPawn):
    def __init__(self, name, coordinate: Coord, environment: GridEnvironment, perception_radius = 3):
        '''Creates a predator that can pervieve 3 blocks NESW. If anything comes into range while the predator is alive, it knows
        that it exists but may not be able to keep track of its position if the predator moves out of perception range.'''
        super().__init__(name,coordinate, environment)
        #no idea where prey is at first, no idea where other predators are either
        self._beliefs = {'prey': {}, 'other_pred_pos':{}}
        self.perception_radius = perception_radius
        self.name = 'Pd'+name
    
    def actuate(self):
       '''Does something to the environment'''
       #first perceive the environment
       self.perceive()
       #recieve any messages from other predators
       self.recieve_message()
       #now implement a strategy to hunt the prey
       self.implement_strategy()
       
    
    def simple_hunt(self):
        '''For this 'turn', predator has already perceived environment and received messages from other predators'''
        #identify which prey is closest
        prey_coords = self._beliefs['prey']
        nearest_prey_coords = Coord(self.env.columns,self.env.rows).get_dist(Coord(0,0))
        nearest_prey = None
        print('beliefs: ',self._beliefs)
        print(sorted(self._beliefs.items(), key = lambda x: x[1].get_dist(self)))
        for prey_key, prey_value in self._beliefs['prey'].items():
            if prey_value.get_dist(self) <= nearest_prey_coords:
                nearest_prey = prey_key
        #now hunt prey_key
       

#    def perceive_grid_coord(self, coord:Coord):
#        grid_coord = self.environment._get_coord(coord)
#        if grid_coord.get_occupied():
#            if isinstance(grid_coord.occupied_val, Prey):
#                self.beliefs['prey_pos'] = grid_coord
#            elif isinstance(grid_coord.occupied_val, Predator):
#                self.beliefs['other_pred_pos'][grid_coord.occupied_val] = grid_coord.occupied_val.current_coord
#                
            
#    def grid_pawn_in_radius(self, pawn:GridPawn):
#        if pawn.current_coord._x-3<=self.current_coord._x <= coord._x +3:
#            if coord._y-3<=self.current_coord._y<=coord._y+3:
#                return True
#            else:
#                return False
            
            
        
#        
#    def perceive(self):
#        '''Updates prey/other predator position if prey is within perception_radius squares'''
#        for grid_pawn in self.env.grid_pawns:
#            if isinstance(grid_pawn, Predator):
#                #update position if detected in radius
#                if self.coord_in_radius(grid_pawn):
#                    self.beliefs['other_pred_pos'][grid_pawn] = grid_pawn.current_coord
#                else:
#                    #if predator grid pawn has already been detected, update position to unkown
#                    if grid_pawn in self._beliefs['other_pred_pos']:
#                        self._beliefs['other_pred_pos'][grid_pawn] = None
#                        
#            elif isinstance(grid_pawn, Prey):
#                 if self.coord_in_radius(grid_pawn):
#                     self.beliefs['other_pred_pos'][grid_pawn] = grid_pawn.current_coord
#                 else:
#                    #if prey grid pawn has already been detected, update position to unkown
#                    if grid_pawn in self._beliefs['other_pred_pos']:
#                        self._beliefs['other_pred_pos'][grid_pawn] = None
         
        
        
    def recieve_message(self):
        '''Receives message from other predator(s)'''
        pass
    
    def send_message(self):
        '''sends message to other predator(s)'''
        pass