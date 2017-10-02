#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:52:42 2017

@author: david
"""
import unittest

from PredatorPreyMultiAgent.Coordinate import Coord

class TestCoordinate(unittest.TestCase):
    
    def test_x(self):
        new_coord = Coord(2,2)
        self.assertEqual(new_coord.get_x(), 2)
        new_coord.set_x(10)
        self.assertEqual(new_coord.get_x(),10)
        self.assertFalse(new_coord.get_occupied())
        
    def test_str(self):
        new_coord = Coord(1,1)
        self.assertEqual(new_coord.__str__(), str(new_coord.get_x())+','+str(new_coord.get_y()))
        
    def test_y(self):
        new_coord = Coord(1,1)
        self.assertEqual(new_coord.get_y(), 1)
        new_coord.set_y(5)
        self.assertEqual(new_coord.get_y(), 5)
        
    def test_get_dist(self):
        coord1 = Coord(1,1)
        coord2 = Coord(2,2)
        coord3 = Coord(10,10)
        self.assertEqual(coord1.get_dist(coord2), 2)
        self.assertEqual(coord1.get_dist(coord3), 18)
        self.assertEqual(coord3.get_dist(None),None)
        
        
if __name__ == '__main__':
    unittest.main()