#User defined imports
from python_files.Predator import Predator
from python_files.Prey import Prey
from PredatorPreyGridEnvironment import PredatorPreyGridEnvironment


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
        
        
            