#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:48:19 2017

@author: david
"""

import unittest
from python_files.GridAbstractions import GridEnvironment
from python_files.Coordinate import Coord
from python_files.GridPawnSubclasses import Predator, Prey

class PreyTest(unittest.TestCase):
    
    def setUp(self):
        self.env = GridEnvironment()
        
    def test_add_single_prey(self):
        pred1 = Predator('1', Coord(0,0), self.env, 6)
        prey1 = Prey('2', Coord(2,3), self.env, speed = 3, perception_radius = 6)
        prey1.perceive()
        self.assertEqual(prey1.find_nearest_predator(), pred1)
        
        
        
    def test_add_multiple_prey(self):
        pred1 = Predator('1', Coord(0,0), self.env, 8)
        prey1 = Prey('1', Coord(2,3), self.env, perception_radius = 8)
        prey1.perceive()
        #print(pred1._beliefs)
        self.assertEqual(prey1.find_nearest_predator(), pred1)
        
        prey2 = Prey('2', Coord(9,5), self.env, perception_radius = 8, speed = 10)
        pred2 = Predator('3', Coord(0,7), self.env, perception_radius = 2)
        prey2.perceive()
        self.assertEqual(prey2.find_nearest_predator(), None)
        prey2.move(Coord(9,9))
        
    def test_get_naive_best_move(self):
        pred1 = Predator('1', Coord(0,0), self.env, perception_radius = 8)
        prey1 = Prey('1', Coord(0,3), self.env, perception_radius = 10)
        prey1.perceive()
        best_naive_move = prey1.get_naive_best_move(pred1.current_coord)
        print('best move: {}'.format(best_naive_move))
        self.assertEqual(best_naive_move, self.env._get_coord(Coord(0,4)))
        
        pred2 = Predator('2', Coord(5,5), self.env, perception_radius = 8)
        prey2 = Prey('2', Coord(6,9), self.env, perception_radius = 10)
        prey2.perceive()
        self.assertEqual(prey2.get_naive_best_move(pred2.current_coord), self.env._get_coord(Coord(7,9)))
        
        pred3 = Predator('3', Coord(9,9), self.env, perception_radius = 8)
        prey2.perceive()
        nearest_pred = prey2.find_nearest_predator()
        self.assertEqual(nearest_pred, pred3)
        self.assertEqual(prey2.get_naive_best_move(nearest_pred.current_coord), self.env._get_coord(Coord(5,9)))
        
        
if __name__ == '__main__':
    unittest.main()
        