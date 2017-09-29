#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:33:28 2017

@author: david
"""

import unittest
from GridAbstractions import GridEnvironment, GridPawn, CoordOccupiedException, CoordOutOfBoundsException
from Coordinate import Coord
from Predator import Predator

class GridPawnEnvironmentTest(unittest.TestCase):
    
    def setUp(self):
        self.env = GridEnvironment()
        
    def test_add_single_predator(self):
        pred1 = Predator('1', Coord(0,0), self.env, 3)
        