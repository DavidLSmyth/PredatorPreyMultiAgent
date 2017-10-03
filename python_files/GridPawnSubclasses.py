# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 12:27:28 2017

@author: 13383861
"""

from python_files.GridAbstractions import GridEnvironment, GridPawnAgent
from python_files.Coordinate import Coord

class Predator(GridPawnAgent):
    def __init__(self, name, coordinate: Coord, environment: GridEnvironment,
                 perception_radius=3, speed=1):
        '''Creates a predator that can pervieve 3 blocks NESW. If anything comes
        into range while the predator is alive, it knows that it exists but may
        not be able to keep track of its position if the predator moves out of
        perception range.'''
        super().__init__(name, coordinate, environment,
                         perception_radius=perception_radius, speed=speed)
        #no idea where prey is at first, no idea where other predators are either
        self.name = 'Pd'+name
        self.strategies = ['simple_hunt_strategy']
        
    def __repr__(self):
        return('Predator({},{},{},{},{})'.format(
            self.name.replace('Pd', ''),
            self.current_coord, self.env, self.perception_radius, self.speed))
        


    def find_nearest_prey(self):
        '''returns the prey and believed coordinates of the nearest prey,
        None if no prey found in perveive radius'''
        return self.find_nearest_Agent(Prey)

    def get_best_move(self, prey_location_details):
        '''Gives the best move given a shortest path to prey'''
        path_to_prey = prey_location_details[1]
        possible_moves = list(filter(lambda x: x in self.find_available_moves(), path_to_prey))
        print('possible predator moves: {}'.format(possible_moves))
        #best move is the one that gets predator as close as possible to prey - 
        #this is as far down the detected shortest path to the prey as possible
        best_move_index = [self.current_coord.get_dist(x) for x in possible_moves].index(max([self.current_coord.get_dist(x) for x in possible_moves]))
        print('moving to square {}'.format(possible_moves[best_move_index]))
        return possible_moves[best_move_index]

    def simple_hunt_strategy(self):
        '''For this 'turn', predator has already perceived environment and received messages from other predators. The simple hunt 
        strategy is implemented as follows: 
            For any given predator, find the nearest prey and chase it down.'''
        nearest_prey = self.find_nearest_prey()
        if(nearest_prey):
            prey_location_details = self.get_prey_path(nearest_prey)
            if prey_location_details:
                self.move(self.get_best_move(prey_location_details))
            else:
                #this should mean that predator is boxed in and has no available moves - try a 
                #random movement in case of a bug
                #print('could not find a path from {} to nearest prey {}'.format(self,nearest_prey))
                self.random_movement()
        else:
            #move to a random unoccupied square
            #print(self.__str__()+'could not find prey')
            self.random_movement()
            
        
    def get_prey_path(self, prey):
        '''Given a detected prey, chase them down via the shortest path to the prey.
        Returns the shortest path from predator to nearest prey'''
        if isinstance(prey, Prey) and prey in self._beliefs:
            return self.env.bfs(self.current_coord, prey.current_coord)
        else:
            raise Exception('Prey {} not in self._beliefs'.format(prey))
            
            
    def receive_message(self):
        '''Receives message from other predator(s)'''
        pass
    
    def send_message(self):
        '''sends message to other predator(s)'''
        pass

class Prey(GridPawnAgent):
    def __init__(self, name, coordinate: Coord, environment: GridEnvironment, perception_radius = 3, speed = 1):
        '''Creates a prey that can pervieve 2 blocks NESW. If anything comes into range while the predator is alive, it knows
        that it exists but may not be able to keep track of its position if the predator moves out of perception range.'''
        super().__init__(name, coordinate, environment, perception_radius = perception_radius, speed = speed)
        #no idea where predators are at first, no idea where other prey are either
        self._beliefs = {'other_pred_pos':{}}
        self.hunted = False
        self.name = 'Py'+name
        self.strategies = ['simple_evade_strategy','random_movement']
    
    def __repr__(self):
        return('Prey({},{},{},{},{})'.format(self.name.replace('Py',''), self.current_coord, self.env, self.perception_radius, self.speed))

    def find_nearest_predator(self):
        '''returns the predator and believed coordinates of the nearest predator,
        None if no predators found in perceive radius'''
        return self.find_nearest_Agent(Predator)
        
    def simple_evade_strategy(self):
        print('{} implementing simple evade strategy'.format(self))
        nearest_predator = self.find_nearest_predator()
        if(nearest_predator):
            print('Nearest Predator {} detected'.format(nearest_predator))
            #beliefs holds coordinates for nearest predator
            perceived_predator_location_details = self._beliefs[nearest_predator]
            if perceived_predator_location_details:
                #make the best move given the location of the nearest predator
                 if self.move(self.get_naive_best_move(perceived_predator_location_details)):
                     print('{} moving strategically'.format(self))
                     pass
                 else:
                     print('{} moving randomly'.format(self))
                     self.random_movement()
        else:
            print('couldnt find nearest predator, moving randomly')
            self.random_movement()
                     
    def get_naive_best_move(self, perceived_predator_location):
        '''Returns the best move for Prey to make in order to avoid a Predator. Naively 
        tries to maximise distance between itself and the nearest predator that it has detected.'''
        naive_best_move_index = list(map(lambda x: perceived_predator_location.get_dist(x), 
                                   self.find_available_moves())).index(
            max(list(map(lambda x: perceived_predator_location.get_dist(x),
                         self.find_available_moves()))))
        return self.find_available_moves()[naive_best_move_index]
        
            
    def receive_message(self):
        pass
