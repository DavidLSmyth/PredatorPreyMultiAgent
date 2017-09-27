# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:44:05 2017

@author: 13383861
"""
#test module for Environment and grid pawn
import unittest
from Environment import GridEnvironment
from GridPawn import GridPawn

class GridPawnEnvironmentTest(unittest.TestCase):
    
    def setUp(self):
        self.env = GridEnvironment()
        
    def test_set_up_env(self):
        self.assertEqual(self.env.rows, 10)
        self.assertEqual(self.env.columns, 10)
        self.assertEqual(self.env.get_unoccupied_coords(), self.env.coordinates)
        self.assertEqual(self.env.get_unoccupied_coords(), [])
        self.assertEqual(self.env.grid_pawns,[])
        
        
if __name__ == '__main__':
    unittest.main()
        
        