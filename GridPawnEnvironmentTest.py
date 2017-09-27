# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:44:05 2017

@author: 13383861
"""
#test module for Environment and grid pawn
import unittest
from GridAbstractions import GridEnvironment, GridPawn, CoordOccupiedException, CoordOutOfBoundsException
from Coordinate import Coord

class GridPawnEnvironmentTest(unittest.TestCase):
    
    def setUp(self):
        self.env = GridEnvironment()
        
    def test_set_up_env(self):
        self.assertEqual(self.env.rows, 10)
        self.assertEqual(self.env.columns, 10)
        self.assertEqual(self.env.get_unoccupied_coords(), self.env.coords)
        self.assertEqual(self.env.get_occupied_coords(), [])
        self.assertEqual(self.env.grid_pawns,[])
        
    def test_add_single_pawn(self):
        pawn1 = GridPawn('1',Coord(0,0), self.env)
        self.assertEqual(pawn1.current_coord,Coord(0,0))
        self.assertEqual(self.env.get_occupied_coords(), [Coord(0,0)])
        self.assertEqual(self.env.grid_pawns, [pawn1])
        
    def test_add_multiple_pawns(self):
        pawn1 = GridPawn('1',Coord(0,0), self.env)
        pawn2 = GridPawn('2',Coord(0,1), self.env)
        pawn3 = GridPawn('3',Coord(9,9), self.env)
        self.assertEqual(self.env.grid_pawns,[pawn1, pawn2, pawn3])
        self.assertEqual(self.env.get_occupied_coords(), [Coord(0,0), Coord(0,1), Coord(9,9)])
        
        self.env.remove_pawn(pawn1)
        self.assertTrue(set(self.env.grid_pawns)==set([pawn2,pawn3]))
        self.assertEqual(self.env.get_unoccupied_coords(), [x for x in self.env.coords if x not in self.env.get_occupied_coords()])
        
    def test_move_pawns(self):
        pawn1 = GridPawn('1',Coord(0,0), self.env)
        pawn2 = GridPawn('2',Coord(0,1), self.env)
        pawn3 = GridPawn('3',Coord(9,9), self.env)
        pawn1.move(Coord(5,5))
        self.assertEqual(pawn1.current_coord, Coord(5,5))
        self.assertTrue(pawn1.current_coord in self.env.get_occupied_coords())
        pawn2.move(Coord(0,0))
        print(pawn2)
        self.assertEqual(pawn2.current_coord, Coord(0,0))
        self.assertFalse(pawn1.move(Coord(0,0)))
        self.assertTrue(pawn1.move(Coord(1,1)))
    
    def test_print_board(self):
        pawn1 = GridPawn('1',Coord(0,0), self.env)
        pawn2 = GridPawn('2',Coord(0,1), self.env)
        pawn3 = GridPawn('3',Coord(9,9), self.env)
        print(self.env.print_board())
        
if __name__ == '__main__':
    unittest.main()
        
        