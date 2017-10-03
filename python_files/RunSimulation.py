#User defined imports
from python_files.Predator import Predator
from python_files.Prey import Prey
from python_files.PredatorPreyGridEnvironment import PredatorPreyGridEnvironment


class RunSimulation:
    '''Runs a predator-prey simulation on a PredatorPreyGridEnvironment.
    Subclasses specify homogenous/heterogenous systems.'''
    def __init__(self, predators: 'list(Predator)', prey: 'list(Prey)', env):
        self.env = env
        self.predators = predators
        self.prey = prey

        if(len(self.predators) + len(self.prey)) > self.env.rows/2 or(
                len(self.predators) + len(self.prey)) > self.env.columns/2:
            raise Warning('''Environment will be very cluttered,
                          consider using fewer predators and prey''')
        if(len(self.predators) + len(self.prey)) >= self.env.rows + self.env.columns:
            raise Exception('''Grid is not big enough to accomodate {}
            prey and {} predators'''.format(len(self.prey), len(self.predators)))
        print('initial setup: ')
        print(self.env.print_board())


    def time_step(self):
        '''Performs a time step in the simulation - each grid agent gets a chance 
        to make a move. Moves should be calculated before they are made'''
        #first perceive the environment
        for agent in self.predators + self.prey:
            agent.perceive()
            agent.perceive()
        #allow each predator and prey to make a move. exceptions should
        #occur when predators and prey try to move to the same grid location
        print(self.predators + self.prey)
        for agent in self.predators + self.prey:            
            try:
                agent.actuate()
            except Exception as e:
                print(e)
        print(self.env.print_board())
        
    def run_input(self):
        inp = ''
        while inp != 'q':
            self.time_step()
            inp = input('Press q to quit: ')
            
            
            
            
            