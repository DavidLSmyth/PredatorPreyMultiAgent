#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:33:28 2017

@author: david
"""

import unittest
from python_files.GridAbstractions import GridEnvironment
from python_files.Coordinate import Coord
from python_files.Predator import Predator
from python_files.Prey import Prey

class PredatorTest(unittest.TestCase):
    
    def setUp(self):
        self.env = GridEnvironment()
        
    def test_add_single_predator(self):
        pred1 = Predator('1', Coord(0,0), self.env, 6)
        prey1 = Prey('2', Coord(2,3), self.env, speed = 3)
        pred1.perceive()
        self.assertEqual(pred1.find_nearest_prey(), prey1)

        
        
        
    def test_add_multiple_predator(self):
        pred1 = Predator('1', Coord(0,0), self.env, 8)
        prey1 = Prey('2', Coord(2,3), self.env, speed = 20)
        pred1.perceive()
        #print(pred1._beliefs)
        self.assertEqual(pred1.find_nearest_prey(), prey1)
        pred2 = Predator('3', Coord(0,1), self.env, 2)
        self.assertEqual(pred2.find_nearest_prey(), None)
        prey1.move(Coord(9,9))
        
        print(self.env.print_board())
        #predator has not perveived so still believes prey is near it
        self.assertEqual(pred1.find_nearest_prey(), prey1)
        
        pred1.perceive()
        #once predator has perceived, finds prey has moved
        self.assertEqual(pred1.find_nearest_prey(), None)
        #self.assertTrue(any(pred1.simple_hunt_strategy() in [Coord(0,1), Coord(0,2), Coord(1,2)], [Coord(0,1), Coord(1,1), Coord(1,2)], [Coord(1,0), Coord(1,1), Coord(1,2)]

        
if __name__ == '__main__':
    unittest.main()
        