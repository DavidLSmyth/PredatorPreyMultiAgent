#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:04:00 2017

@author: david
"""
import sys
sys.path.append('..')
sys.path.append('../..')
#user defined
from python_files.HomogenousRunSimulation import HomogenousRunSimulation
from python_files.PredatorPreyGridEnvironment import PredatorPreyGridEnvironment

def main():
    env = PredatorPreyGridEnvironment(15,15)
    #env: PredatorPreyGridEnvironment, no_predators: int, 
    #             no_prey:int, pred_perception_radius: int, pred_speed: int, 
    #             prey_perception_radius: int, prey_speed: int
    sim = HomogenousRunSimulation(env, 3, 1, 3, 2, 8, 1)
    sim.run_input()


if __name__ == '__main__':
    main()