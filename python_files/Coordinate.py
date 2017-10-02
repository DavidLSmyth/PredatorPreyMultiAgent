#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:51:23 2017

@author: david
"""

class Coord:
    '''A class which contains coordinates which make up a grid structure'''
    def __init__(self, init_x, init_y, occupied = False, occupied_val = None):
        self._x = init_x
        self._y = init_y
        self._occupied = occupied
        self.occupied_val = occupied_val
        
    def __lt__(self,other):
        return [True if self.get_dist(other)>0 else False]
    
    def __eq__(self, other):
        '''Equality is taken in terms of x coords and y coords, nothing specified for 
        occupancy status'''
        if isinstance(other, Coord):
            if(other.get_x() == self.get_x() and other.get_y() == self.get_y()):
                return True
        return False
        
    def __str__(self):
        return str(self.get_x())+','+str(self.get_y())
    
    def __repr__(self):
        return 'Coord({},{},{},{})'.format(self.get_x(), self.get_y(), self._occupied, self.occupied_val)

    def get_dist(self,other_coord):
        '''returns the Manhattan distance from current Coord to other Coord'''
        if(isinstance(other_coord, Coord)):
            return abs(self.get_x() - other_coord.get_x()) + abs(self.get_y() - other_coord.get_y())
        else:
            raise NotImplementedError('Cannot get the distance of object of type {} to object of type{}'.format(type(self), type(other_coord)))
        
    def get_x(self):
        return self._x
    
    def set_x(self, new_x):
        if not (isinstance(new_x, int)):
            raise TypeError('X value must be of type int, not type {}'.format(type(new_x)))
        else:
            self._x = new_x
    
    def get_y(self):
        return self._y
    
    def set_y(self, new_y):
        if not (isinstance(new_y, int)):
            raise TypeError('X value must be of type int, not type {}'.format(type(new_y)))
        else:
            self._y = new_y
            
    def get_value(self):
        if(self.get_occupied()):
            return self.occupied_val
        else:
            return None
            
    def set_occupied(self,new_value):
        self._occupied = new_value
        
    def get_occupied(self):
        return self._occupied
            
            