# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:39:04 2017

@author: 13383861
"""
#stdlib
import random
#user defined
from python_files.GridAbstractions import GridEnvironment, GridPawnAgent
from python_files.Coordinate import Coord
    
class Prey(GridPawnAgent):
    def __init__(self, name, coordinate: Coord, environment: GridEnvironment, perception_radius = 3, speed = 1):
        '''Creates a prey that can pervieve 2 blocks NESW. If anything comes into range while the predator is alive, it knows
        that it exists but may not be able to keep track of its position if the predator moves out of perception range.'''
        super().__init__(name, coordinate, environment, perception_radius = perception_radius, speed = speed)
        #no idea where predators are at first, no idea where other prey are either
        self._beliefs = {'other_pred_pos':{}}
        self.hunted = False
        self.name = 'Py'+name
        self.escape_strategies = ['random_movement']
    
    def __repr__(self):
        return('Prey({},{},{},{},{})'.format(self.name.replace('Py',''), self.current_coord, self.env, self.perception_radius, self.speed))

    def random_movement(self):
        move_choice = random.choice(self.find_available_moves())
        print(self, ' is randomly moving to {}'.format(move_choice))
        self.move(move_choice)
        
    #def evade(self):
        
        
    def implement_strategy(self, strategy_option: 'member of self.hunt_strategies' = None):
        if strategy_option:
            if strategy_option in self.hunt_strategies:
                eval('self.'+strategy_option+'()')
        else:
            #execute default - ToDo
            self.random_movement()
            
    def receive_message(self):
        pass