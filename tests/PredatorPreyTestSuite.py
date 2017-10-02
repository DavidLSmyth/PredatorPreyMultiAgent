#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:06:38 2017

@author: david
"""

import unittest
import sys
#user defined
from PredatorTest import PredatorTest
from GridPawnEnvironmentTest import GridPawnEnvironmentTest
from CoordinateTest import TestCoordinate

test_grid_pawn_env = unittest.TestLoader().loadTestsFromTestCase(GridPawnEnvironmentTest)
test_predator = unittest.TestLoader().loadTestsFromTestCase(PredatorTest)
test_coord = unittest.TestLoader().loadTestsFromTestCase(TestCoordinate)
test_suite = unittest.TestSuite([test_grid_pawn_env,test_predator, test_coord]) 
runner_result = unittest.TextTestRunner(verbosity=2).run(test_suite).wasSuccessful()
#.run(testsuite)
#ret = not runner.run(test_suite).wasSuccessful()
sys.exit(not runner_result)