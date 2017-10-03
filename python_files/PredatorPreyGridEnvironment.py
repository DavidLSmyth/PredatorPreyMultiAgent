#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 20:31:30 2017

@author: david
"""
from python_files.GridAbstractions import GridEnvironment
from python_files.GridPawnSubclasses import Predator
from python_files.Coordinate import Coord

class PredatorPreyGridEnvironment(GridEnvironment):
    '''A class containing a grid which is populated by predators and prey'''
    def __init__(self,rows=10, columns=10):
        super().__init__(rows, columns)
        
    #@override
    def get_neighbor_coords(self, coord:Coord):
        '''returns all non-diagonal adjacent nodes that do not contain predators. Used for BFS to find prey but avoid other predators'''
        return list(filter(lambda x: coord.get_dist(x) == 1, list(filter(lambda x: not isinstance(x.get_value(), Predator),self.coords))))
        
    def bfs(self, start_coord, end_coord):
        '''performs breadth first search for prey, avoiding other predators'''
        return super().bfs(start_coord, end_coord, self.get_neighbor_coords)