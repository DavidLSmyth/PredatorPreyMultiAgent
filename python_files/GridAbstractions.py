from python_files.Coordinate import Coord

class GridPawn:
    '''An abstract class which creates a pawn on the grid and allows the pawn to move around on the grid. The pawn may only exist on the grid'''
    def __init__(self, name, coord:Coord, env):
        '''initialises the pawn's environment and places the pawn in the environment'''
        self.env = env
        self.name = 'Pn'+name
        if(self.env.coord_occupied(coord)):
            raise CoordOccupiedException('Coordinate {} is already occupied', coord.__str__())
        else:
            env_coord = self.env.place_pawn(self, coord)
            self.current_coord = env_coord
    
    def move(self, coord)->'Bool':
        '''Attempts to move the GridPawn to the given coordinate. Returns true if successfully moved
        otherwise returns false'''
        try:
            env_coord = self.env.move_pawn(self,coord)
            if env_coord:
                self.current_coord = env_coord
                return True
        except (CoordOccupiedException, CoordOccupiedException) as e:
            raise Exception('Invalid move')
            
    def __str__(self):
        return 'GridPawn({},{})'.format(self.name,self.current_coord)
    
    def __repr__(self):
        return self.name+str(self.current_coord)
            
    
class GridPawnAgent(GridPawn):
    def __init__(self, name, coord: Coord, environment, perception_radius = 3, speed = 1):
        super().__init__(name, coord, environment)
        #a dicionary of beliefs about current environment - holds other pawns and percieved position
        self._beliefs = {}
        self.perception_radius = perception_radius
        self.name = 'Pa'+name
        #max number of squares predator can move in any given direction in one turn
        self.speed = speed
        
    def _find_available_squares(self, radius):
        '''returns all unoccupied coordinates of distance less than radius. Auxiliary method'''
        return list(filter(lambda x: self.current_coord.get_dist(x)<=radius, self.env.get_unoccupied_coords()))
    
    def find_available_moves(self):
        '''returns all unoccupied coordinates of distance less than speed'''
        return(self._find_available_squares(self.speed))
    
    def move(self, coord:Coord):
        if coord in self.find_available_moves():
            super().move(coord)
        else:
            raise Exception('Invalid move')
    
    def perceive(self):
        '''Updates prey/other predator position if prey is within perception_radius squares'''
        for grid_pawn in list(filter(lambda x: x!=self,self.env.grid_pawns)):
            if self.grid_pawn_in_radius(grid_pawn):
                #agent knows where other grid pawn is
                self._beliefs[grid_pawn] = grid_pawn.current_coord
            else:
                #agent still knows about grid_pawn but doesn't know its exact position
                self._beliefs[grid_pawn] = None
        
                     
    def grid_pawn_in_radius(self, pawn:GridPawn):
        '''Returns true if there is another grid pawn in the current grid pawn's perception radius'''
        if pawn.current_coord._x-self.perception_radius<=self.current_coord._x <= pawn.current_coord._x +self.perception_radius:
            if pawn.current_coord._y-self.perception_radius<=self.current_coord._y<=pawn.current_coord._y+self.perception_radius:
                return True
            else:
                return False
    
class GridEnvironment:
    '''Creates a grid environment'''
    def __init__(self, rows=10, columns=10):
        '''constructs a rowsXColumns grid environment. Coordinates are in the range (0->(rows-1),(0->(columns-1)))'''
        self.rows = rows
        self.columns = columns
        self.coords = [Coord(x,y) for x in range(rows) for y in range(columns)]
        self.occupied_coords = []
        self.grid_pawns = []
        
    def __repr__(self):
        return 'GridEnvironment({},{})'.format(self.rows, self.columns)
    
    def get_occupied_coords(self):
        return self.occupied_coords
    
    def get_unoccupied_coords(self):
        return list(filter(lambda x: x not in self.occupied_coords, self.coords))
    
    def place_pawn(self,pawn: GridPawn, coord: Coord):
        '''Places a pawn on the grid at position coord if the coordinate is free'''
        coord = self._get_coord(coord)
        if not self.coord_occupied(coord):
            if pawn in self.grid_pawns:
                raise Exception('Pawn is already in the grid; move it with move_pawn')                
            else:
                self.grid_pawns.append(pawn)
                self.occupied_coords.append(coord)
                coord.set_occupied(True)
                coord.occupied_val = pawn
                return coord
        else:
            raise CoordOutOfBoundsException('Coordinate {} is already occupied.'.format(coord.__str__()))
        
    def remove_pawn(self,pawn: GridPawn):
        '''removes a given pawn from the grid'''
        if pawn in self.grid_pawns:
            self.grid_pawns.remove(pawn)
            self.occupied_coords.remove(pawn.current_coord)
            pawn.current_coord.set_occupied(False)
            pawn.current_coord.occupied_val=None
            print('Successfully removed pawn {} from environment'.format(pawn.name))
            del pawn
            
        else:
            raise Exception('Pawn is not on grid; cannot remove')
            
    def move_pawn(self, pawn: GridPawn, coord: Coord):
        '''Moves a pawn that has already been placed on the grid to a new position'''
        if pawn in self.grid_pawns:
            coord = self._get_coord(coord)
            if not self.coord_occupied(coord):
                print('moving pawn {} to coordinate {}'.format(pawn.__str__(),coord.__str__()))
                pawn.current_coord.set_occupied(False)
                pawn.current_coord.occupied_val = None
                self.occupied_coords.remove(pawn.current_coord)
                self.occupied_coords.append(coord)
                coord.set_occupied(True)
                coord.occupied_val = pawn
                return coord
            else:
                raise CoordOccupiedException('Coord {} is already occupied, cannot move pawn'.format(coord.__str__()))
        else:
            raise Exception('Please place pawn on the grid first using place_pawn')
        
    def verify_valid_coord(self, coord:Coord):
        if 0<=coord.get_x()<self.rows and 0<=coord.get_y()<self.columns:
            return True
        else:
            return False

    
    def coord_occupied(self,coord):
        if self.verify_valid_coord(coord):
            coord = self._get_coord(coord)
            return(coord.get_occupied())
        else:
            raise CoordOutOfBoundsException('Coordinate out of bounds')
            
    def _get_coord(self,coord):
        '''helper method to return the coord beloning to the current class'''
        return [x for x in self.coords if x == coord][0]
    
    def print_board(self) -> str:
        padding = '  0  |'
        
        print_string = '\n'+'-'*len(padding)*self.rows + '\n'
        for x_coord in range(self.columns):
            print_string+='|'
            for y_coord in range(self.rows):
                if self.coord_occupied(self._get_coord(Coord(x_coord, y_coord))):
                    pawn = self._get_coord(Coord(x_coord, y_coord)).get_value()
                    print_string+=' {} |'.format(pawn.name)
                else:
                    print_string+=padding
            print_string+='\n'+'-'*len(padding)*self.rows + '\n'
        return print_string
    
    def get_neighbor_coords(self, coord:Coord):
        '''returns all non-diagonal adjacent nodes'''
        return list(filter(lambda x: coord.get_dist(x) == 1, self.get_unoccupied_coords()))
        
    
    def bfs(self, start_coord: Coord, end_coord: Coord, get_neighbor_function = None):
        '''Returns the shortest path(s) from one coordinate to another. Search coords are given all all available coords.
        Params: start_coord -> valid grid coordinate which 
        '''
        if self.verify_valid_coord(start_coord) and self.verify_valid_coord(end_coord):
            pass
        else:
            raise Exception('Coordinates provided arent valid: {} {}'.format(start_coord, end_coord))
        
        if not get_neighbor_function:
            get_neighbor_function = self.get_neighbor_coords
        
        dist_to_end = 0
        #start with start_coord in queue
        Q = [start_coord]
        visited_nodes = []
        #{coord: predecessor}
        #need to use repr because Coord is not hashable
        predecessors = {start_coord.__str__(): None}
        
        while Q != [] and end_coord not in visited_nodes:
            #if we have already visited end_coord, it will be a shortest path since 
            #bfs works in layers
            print('Q: ', Q)
            current_node = Q.pop()
            print('Exploring current node: ',current_node)
            print('dist_to_end: {}'.format(dist_to_end))
            #for each of the current node's neighbors:
            for node in get_neighbor_function(current_node):
                #if the node has not yet been visited, append the node to the queue
                if node not in visited_nodes and node not in Q:
                    predecessors[node.__str__()] = current_node.__str__()
                    print('enqueing {}'.format(node))
                    Q.insert(0,node)
                #mark current node as visited
                visited_nodes.append(current_node)
                #distance_to_end increments when a node has been visited
        
        
        
        if end_coord in visited_nodes:
            #reconstruct path
            path = [self._get_coord(eval('Coord('+end_coord.__str__()+')'))]
            current_predecessor = predecessors[end_coord.__str__()]
            print(path)
            while current_predecessor != None:
                print(current_predecessor)
                #print(self._get_coord(Coord(current_predecessor.split(',')[0],current_predecessor.split(',')[0])))
                path.append(self._get_coord(eval('Coord('+current_predecessor+')')))
                current_predecessor  = predecessors[current_predecessor]
                dist_to_end+=1
            return (dist_to_end,path)
        else:
            #no path found
            return False
                
    
class CoordOutOfBoundsException(Exception):
    pass

class CoordOccupiedException(Exception):
    pass


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
    