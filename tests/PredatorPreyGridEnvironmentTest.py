#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 20:41:45 2017

@author: david
"""
#stdlib
import unittest

#3rd party

#user defined
from python_files.PredatorPreyGridEnvironment import PredatorPreyGridEnvironment
from python_files.Coordinate import Coord
from python_files.Predator import Predator
from python_files.Prey import Prey

class TestPredatorPreyGridEnvironment(unittest.TestCase):
    
    def setUp(self):
        self.env = PredatorPreyGridEnvironment()
    
    def test_get_neighbor_coords(self):
        '''makes sure that the get_neighbor_coords method can detect neightboring nodes as long as another predator is not occupying them'''
        self.assertTrue(all(list(filter(lambda x: x in self.env.get_neighbor_coords(Coord(0,0)), [Coord(0,1), Coord(1,0)]))))
        pred1 = Predator('1', Coord(1,1),self.env)
        pred2 = Predator('2', Coord(0,1), self.env)
        self.assertTrue(all(list(filter(lambda x: x in self.env.get_neighbor_coords(pred1.current_coord), [Coord(1,0), Coord(2,1), Coord(1,2)]))))
        prey1 = Prey('3', Coord(2,1), self.env)
        self.assertTrue(all(list(filter(lambda x: x in self.env.get_neighbor_coords(pred1.current_coord), [Coord(1,0), Coord(2,1), Coord(1,2)]))))
        #all(list(filter(lambda x: x in self.env.get_neighbor_coords(Coord(3,3)), [Coord(3,2),Coord(3,4),Coord(2,3),Coord(4,3)]))))
        pred3 = Predator('4', Coord(1,2), self.env)
        self.assertTrue(all(list(filter(lambda x: x in self.env.get_neighbor_coords(pred1.current_coord), [Coord(1,0), Coord(2,1)]))))
    
    def test_bfs(self):
        pred1 = Predator('1', Coord(0,0),self.env)
        pred2 = Predator('2', Coord(0,1), self.env)
        prey1 = Prey('1', Coord(0,2),self.env)
        #should be 1,0 1,1 1,2
        print('\n\n\n Testing bfs')
        bfs_res = self.env.bfs(pred1.current_coord, prey1.current_coord)[1]
        self.assertEqual(bfs_res, list(map(lambda x: self.env._get_coord(x),[Coord(0,2), Coord(1,2), Coord(1,1), Coord(1,0), Coord(0,0)])))
        
    def test_best_move(self):
        pred1 = Predator('1', Coord(0,0),self.env, 5)
        pred2 = Predator('2', Coord(0,1), self.env)
        prey1 = Prey('1', Coord(0,2),self.env)
        pred1.perceive()
        nearest_prey = pred1.find_nearest_prey()
        pred1.perceive()
        self.assertEqual(nearest_prey, prey1)
        prey_location_details = pred1.get_prey_path(nearest_prey)
        best_move = pred1.get_best_move(prey_location_details)
        self.assertEqual(best_move, self.env._get_coord(Coord(1,0)))
        
        
        
        
        
        
        
        
        