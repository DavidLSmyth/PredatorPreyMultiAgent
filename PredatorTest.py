#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:33:28 2017

@author: david
"""

import unittest
from GridAbstractions import GridEnvironment, GridPawn, CoordOccupiedException, CoordOutOfBoundsException
from Coordinate import Coord

class GridPawnEnvironmentTest(unittest.TestCase):
    
    def setUp(self):
        self.env = GridEnvironment()