from Coordinate import Coord
from GridPawn import GridPawn

    
class GridEnvironment:
    '''Creates a grid environment'''
    def __init__(self, rows=10, columns=10):
        '''constructs a rowsXColumns grid environment. Coordinates are in the range (0->(rows-1),(0->(columns-1)))'''
        self.rows = rows
        self.columns = columns
        self.coordinates = [Coord(x,y) for x in range(rows) for y in range(columns)]
        self.occupied_coords = []
        self.grid_pawns = []
    
    def get_occupied_coords(self):
        return self.occupied_coords
    
    def get_unoccupied_coords(self):
        return list(filter(lambda x: x not in self.occupied_coords, self.coordinates))
    
    def place_pawn(self,pawn: GridPawn, coord: Coord):
        if not self.coord_occupied(coord) and not pawn in self.grid_pawns:
            self.grid_pawns.append(pawn)
            self.occupied_coords.append(coord)
            coord.set_occupied(True)
        else:
            raise Exception('Coordinate is already occupied or is not in the grid bounds. Cannot move pawn to specified coordinate')
        
    def remove_pawn(self,pawn: GridPawn):
        if pawn in self.grid_pawns:
            self.grid_pawns.remove(pawn)
            self.occupied_coords.remove(pawn.current_coord)
            pawn.current_coord.set_occupied(False)
        else:
            raise Exception('Pawn is not on grid; cannot remove')
            
    def move_pawn(self, pawn: GridPawn, coord: Coord):
        if pawn in self.grid_pawns:
            if not self.coord_occupied(coord):
                self.occupied_coords.remove(pawn.current_coord)
                self.occupied_coords.append(coord)
        else:
            raise Exception('Please place pawn on the grid first using place_pawn')
        
    def verify_valid_coord(self, coord:Coord):
        if 0<=coord.get_x()<self.rows and 0<=coord.get_y()<self.columns:
            return True
        else:
            return False
    
    def __repr__(self):
        pass
    
    def coord_occupied(self,coord):
        if self.verify_valid_coord(coord):
            return(coord.get_occupied())
        else:
            raise Exception('Coordinate out of bounds')
    



#
#class SimulationRunner:
#    def __init__(self,rows=10, columns=10, no_predators = 2, no_prey = 1):
#        self.environment = Environment(rows, columns)
#        self.predator_agents = [Predator(,self.environment) for i in range(no_predators)]
#        self.prey_agents= [Prey() for i in range(no_prey)]
#        for predator_agent in self.predator_agents:
#            self.environment.add_predator_agent(predator_agent)
#        for prey_agent in self.prey_agents:
#            self.environment.add_prey_agent(prey_agent)
#    
#    def run_simulation(self):
#        #while prey has not been captured:
#            #allow predators to move
#            #allow prey to move
    