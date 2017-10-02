# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:44:05 2017

@author: 13383861
"""
#test module for Environment and grid pawn
import unittest
from python_files.GridAbstractions import GridEnvironment, GridPawn, GridPawnAgent
from python_files.Coordinate import Coord

class GridPawnEnvironmentTest(unittest.TestCase):
    
    def setUp(self):
        self.env = GridEnvironment()
        
    def test_set_up_env(self):
        self.assertEqual(self.env.rows, 10)
        self.assertEqual(self.env.columns, 10)
        self.assertEqual(self.env.get_unoccupied_coords(), self.env.coords)
        self.assertEqual(self.env.get_occupied_coords(), [])
        self.assertEqual(self.env.grid_pawns,[])
        self.assertEqual(self.env.get_neighbor_coords(Coord(0,0)), [Coord(0,1), Coord(1,0)])
        self.assertTrue(all(list(filter(lambda x: x in self.env.get_neighbor_coords(Coord(3,3)), [Coord(3,2),Coord(3,4),Coord(2,3),Coord(4,3)]))))
        
    def test_bfs(self):
        print('\n\n\n\n\n')
        print('bfs result: ', self.env.bfs(Coord(0,0), Coord(3,3),self.env.get_neighbor_coords))
        self.assertEqual(self.env.bfs(Coord(0,0), Coord(3,3), self.env.get_neighbor_coords)[0], 6)

        self.assertEqual(self.env.bfs(Coord(0,0), Coord(0,3),self.env.get_neighbor_coords), (3,list(map(lambda x: self.env._get_coord(x), [Coord(0,3), Coord(0,2), Coord(0,1), Coord(0,0)]))))
        
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
        self.assertEqual(pawn2.current_coord, Coord(0,0))
        with self.assertRaises(Exception):
            pawn1.move(Coord(0,0))
        self.assertTrue(pawn1.move(Coord(1,1)))
        
    def test_add_pawnAgent(self):
        pawn1 = GridPawnAgent('1',Coord(0,0), self.env)
        self.assertEqual(self.env.occupied_coords, [self.env._get_coord(Coord(0,0))])
        self.assertEqual(self.env.grid_pawns, [pawn1])
        
    def test_move_pawnAgent(self):
        pawn1 = GridPawnAgent('1',Coord(0,0), self.env)
        pawn2 = GridPawnAgent('2',Coord(5,5), self.env)
        pawn3 = GridPawnAgent('3',Coord(5,6), self.env)
        
        self.assertEqual(self.env.grid_pawns, [pawn1,pawn2, pawn3])
        self.assertEqual(self.env.get_occupied_coords(), [self.env._get_coord(Coord(0,0)),self.env._get_coord(Coord(5,5)), self.env._get_coord(Coord(5,6))])
        
        pawn1.move(Coord(1,0))
        self.assertFalse(self.env._get_coord(Coord(0,0)) in self.env.occupied_coords)
        print(self.env.print_board())
        
        
    def test_perceive_pawnAgent(self):
        pawn1 = GridPawnAgent('1', Coord(4,4), self.env, speed = 10)
        pawn2 = GridPawnAgent('1', Coord(6,6), self.env)
        pawn1.perceive()
        self.assertTrue(pawn1._beliefs, {})
        pawn1.perceive()
        self.assertEqual(pawn1._beliefs, {pawn2: self.env._get_coord(Coord(6,6))})
        print(pawn1._beliefs)
        print(pawn2._beliefs)
        self.assertTrue(pawn2._beliefs == {})
        pawn2.perceive()
        self.assertEqual(pawn2._beliefs, {pawn1:self.env._get_coord(Coord(4,4))})
        
        pawn1.move(Coord(0,0))
        pawn1.perceive()
        self.assertEqual(pawn1._beliefs, {pawn2:None})
        self.assertEqual(pawn2._beliefs, {pawn1:self.env._get_coord(Coord(4,4))})
        pawn2.perceive()
        self.assertEqual(pawn2._beliefs, {pawn1:None})
        
        
if __name__ == '__main__':
    unittest.main()
        
        