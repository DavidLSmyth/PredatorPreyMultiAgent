# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:27:28 2017

@author: 13383861
"""

import operator

from python_files.GridAbstractions import GridEnvironment, GridPawnAgent
from python_files.Prey import Prey
from python_files.Coordinate import Coord

class Predator(GridPawnAgent):
    def __init__(self, name, coordinate: Coord, environment: GridEnvironment, perception_radius = 3, speed = 1):
        '''Creates a predator that can pervieve 3 blocks NESW. If anything comes into range while the predator is alive, it knows
        that it exists but may not be able to keep track of its position if the predator moves out of perception range.'''
        super().__init__(name,coordinate, environment)
        #no idea where prey is at first, no idea where other predators are either
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
       
    def find_nearest_prey(self):
        '''returns the prey and believed coordinates of the nearest prey, None if no prey found in perveive radius'''
        print('{} searching for nearest prey'.format(self))
        #initialise nearest_prey_coords as the furthest possible distance in the grid
        perceived_nearest_prey_dist = Coord(self.env.columns,self.env.rows).get_dist(Coord(0,0))
        perceived_nearest_prey = None
        print('beliefs: ',self._beliefs)
        #print(sorted(self._beliefs.items(), key = lambda x: x[1].get_dist(self)))
        for prey_key, prey_value in self._beliefs.items():
            #if the distance from the nearest prey to the predator is less than the current
            #nearest prey, update current_prey
            print('prey_value: ',prey_value)
            if isinstance(prey_key, Prey) and isinstance(prey_value, Coord):
                if prey_value.get_dist(self.current_coord) <= perceived_nearest_prey_dist:
                    perceived_nearest_prey = prey_key
        print(self.__str__(), 'detected nearest prey: {} - seaching for shortest path to prey'.format(perceived_nearest_prey.__str__()))
        return perceived_nearest_prey
        
       
    
    def simple_hunt_strategy(self):
        '''For this 'turn', predator has already perceived environment and received messages from other predators. The simple hunt 
        strategy is implemented as follows: 
            For any given predator, find the nearest prey and chase it down.'''
        nearest_prey = self.find_nearest_prey()
        if(nearest_prey):
            self.chase_prey(nearest_prey)
        else:
            #move to a random unoccupied square
            pass
        
    def chase_prey(self, prey):
        '''Given a detected prey, chase them down via the shortest path to the prey. Currently doesn't take into account that other 
        predators can get in the way. Returns the shortest path from predator to nearest prey'''
        if isinstance(prey, Prey) and prey in self._beliefs:
            return self.env.bfs(self.current_coord, prey.current_coord)
        else:
            raise Exception('Prey {} not in self._beliefs'.format(prey))

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