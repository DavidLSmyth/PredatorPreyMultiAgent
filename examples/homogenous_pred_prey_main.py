#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:04:00 2017

@author: david
"""
import sys
sys.path.append('..')
sys.path.append('../..')
#user defined
from PredatorPreyMultiAgent.python_files.HomogenousRunSimulation import HomogenousRunSimulation
from PredatorPreyMultiAgent.python_files.PredatorPreyGridEnvironment import PredatorPreyGridEnvironment

def main():
    env = PredatorPreyGridEnvironment(10,10)
    sim = HomogenousRunSimulation(env, 2, 2, 5, 2, 1, 1)
    sim.run_input()


if __name__ == '__main__':
    main()