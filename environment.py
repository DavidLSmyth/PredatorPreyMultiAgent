from Coordinate import Coord
class Predator:
    
    def __init__(self,coordinate, environment, perception_radius = 4):
        self._beliefs = []
        self.environment = environment
        if(self.environment.get_coord_details()):
            raise Exception('Coordinate {} is already occupied', coordinate.__str__())
        if coordinate in self.environment.coordinates:
            self.environment.
            self.coordinate = Coord(x_coord, y_coord, True)
        else:
            raise Exception('Coordinate out of bounds')
        self.perception_radius = perception_radius
        self.perceived_prey_position = None
    
    def actuate(self):
        #call move
        pass
    
    def move(self, new_coordinate):
        if new_coordinate in environment.coordinates and not self.environment.get_coord_details:
            #check the coordinate is not yet occupied and not out of bounds
            self.coordinate = new_coordinate
        else:
            raise Exception('Invalid coordinate choice')
    
    def perceive(self):
        '''Updates prey position if prey is within perception_radius squares'''
        
       
    def get_coordinates(self):
        return (coordinate.get_x(), coordinate.get_y())
    
    def recieve_message(self):
        pass
    
    def send_message(self):
        pass
    
class Prey:
    def __init__(self):
        pass
    
    def move(self):
        pass

    
class Environment:
    '''Creates a grid environment'''
    def __init__(self, rows=10, columns=10):
        '''constructs a rowsXColumns grid environment'''
        self.rows = rows
        self.columns = columns
        self.coordinates = [Coord(x,y) for x in range(rows) for y in range(columns)]
        
    def modify_coord(coord):
        if coord in 
    
    def __repr__(self):
        pass
    
    def get_coord_details(coordinate):
        if 0<x<self.columns and 0<y<rows:
            return(coordinate.get_occupied())
        
    




class SimulationRunner:
    def __init__(self,rows=10, columns=10, no_predators = 2, no_prey = 1):
        self.environment = Environment(rows, columns)
        self.predator_agents = [Predator(,self.environment) for i in range(no_predators)]
        self.prey_agents= [Prey() for i in range(no_prey)]
        for predator_agent in self.predator_agents:
            self.environment.add_predator_agent(predator_agent)
        for prey_agent in self.prey_agents:
            self.environment.add_prey_agent(prey_agent)
    
    def run_simulation(self):
        #while prey has not been captured:
            #allow predators to move
            #allow prey to move
    