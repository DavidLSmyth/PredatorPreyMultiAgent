#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:55:34 2017

@author: david
"""

from python_files.RunSimulation import RunSimulation
from python_files.PredatorPreyGridEnvironment import PredatorPreyGridEnvironment
from python_files.GridPawnSubclasses import Prey, Predator

class HomogenousRunSimulation(RunSimulation):
    
    def __init__(self, env: PredatorPreyGridEnvironment, no_predators: int, 
                 no_prey:int, pred_perception_radius: int, pred_speed: int, 
                 prey_perception_radius: int, prey_speed: int):
        
        #self, name, coordinate: Coord, environment: GridEnvironment,
        #         perception_radius=3, speed=1
        predator_list = [Predator(str(i), env.get_random_free_square(), 
                                  env, perception_radius = pred_perception_radius, speed = pred_speed) for i in range(no_predators)]
    
        prey_list = [Prey(str(i), env.get_random_free_square(), 
                                  env, perception_radius = prey_perception_radius, speed = prey_speed) for i in range(no_prey)]
    
        super().__init__(predator_list, prey_list, env)
        
    
