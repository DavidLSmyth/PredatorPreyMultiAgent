import logging
import datetime

from autologging import logged, traced, TRACE


#User defined imports
from python_files.GridPawnSubclasses import Prey, Predator
from python_files.PredatorPreyGridEnvironment import PredatorPreyGridEnvironment

#set up logging config
#logging file should exist in logging module
logging.basicConfig(datefmt='%Y/%m/%d %I:%M:%S %p', level=TRACE,
                    filename='''../logging_output/PredPreySim.log''', format="%(levelname)s:%(name)s:%(funcName)s:%(message)s")


@logged
class RunSimulation:
    '''Runs a predator-prey simulation on a PredatorPreyGridEnvironment.
    Subclasses specify homogenous/heterogenous systems.'''
    def __init__(self, predators: 'list(Predator)', prey: 'list(Prey)', env: PredatorPreyGridEnvironment):
        self.env = env
        self.predators = predators
        self.prey = prey

#        if(len(self.predators) + len(self.prey)) > self.env.rows/2 or(
#                len(self.predators) + len(self.prey)) > self.env.columns/2:
#            raise Warning('''Environment will be very cluttered, consider using fewer predators and prey. {} predators and {} prey'''.format(len(self.predators), len(self.prey)))
#        if(len(self.predators) + len(self.prey)) >= self.env.rows + self.env.columns:
#            raise Exception('''Grid is not big enough to accomodate {} prey and {} predators'''.format(len(self.prey), len(self.predators)))
        self.__log.info('\n\n\n -------------------- Logging new run {} --------------------'.format(datetime.datetime.now()))
        self.__log.info('initialising environment: {} predators and {} prey'.format(len(self.predators), len(self.prey)))
        self.__log.info('initial setup: ')
        self.__log.info(self.env.self.__log.info_board())


    def time_step(self):
        '''Performs a time step in the simulation - each grid agent gets a chance 
        to make a move. Moves should be calculated before they are made'''
        #first perceive the environment
        for agent in self.predators + self.prey:
            agent.perceive()
        #allow each predator and prey to make a move. exceptions should
        #occur when predators and prey try to move to the same grid location
        for agent in self.predators + self.prey:            
            try:
                if isinstance(agent, Prey):
                    agent.actuate('simple_evade_strategy')
                elif isinstance(agent, Predator):
                    agent.actuate('simple_hunt_strategy')
                else:
                    self.__log.info('could not identify agent')
            except Exception as e:
                self.__log.info(e)
        self.__log.info(self.env.self.__log.info_board())
        
    def run_input(self):
        inp = ''
        while inp != 'q':
            self.time_step()
            inp = input('Press q to quit: ')
            
            
            
            
            