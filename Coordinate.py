#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:51:23 2017

@author: david
"""

class Coord:
    
    def __init__(self, init_x, init_y, occupied = False, *args):
        self._x = init_x
        self._y = init_y
        self._occupied = occupied
        self.args = args
    
    def __eq__(self, other):
        if isinstance(other, Coord):
            if(other.get_x() == self.get_x() and other.get_y() == self.get_y()):
                return True
        return False
        
    def __str__(self):
        return str(self.get_x())+str(self.get_y())
    
    def __repr__(self):
        return (self.get_x(), self.get_y())

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
            
    def set_occupied(self,new_value):
        self._occupied = new_value
        
    def get_occupied(self):
        return self._occupied
            
            