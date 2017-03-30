'''Created on 23 de mar. de 2017

@author: Alejandro Serrano
'''
'''Start of package'''

import abc
import random
import copy
from time import sleep

class Game:
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement
    legal_moves, make_move, utility, and terminal_test. You may
    override display and successors or you can inherit their default
    methods. You will also need to set the .initial attribute to the
    initial state; this can be done in the constructor."""
    @abc.abstractmethod
    def legal_moves(self, state):
        "Return a list of the allowable moves at this point."
    @abc.abstractmethod
    def make_move(self, move, state):
        "Return the state that results from making a move from a state."
    @abc.abstractmethod
    def utility(self, state, player):
        "Return the value of this final state to player."
    @abc.abstractmethod
    def terminal_test(self, state):
        "Return True if this is a final state for the game."
        return not self.legal_moves(state)
    def to_move(self, state):
        "Return the player whose move it is in this state."
        return state.to_move
    def display(self, state):
        "Print or otherwise display the state."
        print state
    def successors(self, state):
        "Return a list of legal (move, state) pairs."
        return [(move, self.make_move(move, state))
                for move in self.legal_moves(state)]
    def __repr__(self):
        return '<%s>' % self.__class__.__name__

'''Class for modeling a position on the Open Field Tic Tac Toe Problem'''
class CheckerboardPosition:
    
    maxLevel = 0
    '''This makes it easy to know if a node exists and fetch it'''
    nodesDictionary = {}
    
    def __init__(self, coordinates):
        self.move = None
        self.north = None
        self.northEast = None
        self.east = None
        self.southEast = None
        self.south = None
        self.southWest = None
        self.west = None
        self.northWest = None
        '''first positon = N-S, seond, NE-SW, third E-W, fourth NW-SE '''
        self.moveChain = [Struct(chainOrientation='N-S', chainCount = 0),Struct(chainOrientation='NE-SW', chainCount = 0), Struct(chainOrientation='E-W', chainCount = 0), Struct(chainOrientation='NW-SE', chainCount = 0)]
        self.level = 0
        self.coordinates = coordinates
        
    def addToNodesDictionary(self):
        if(self.coordinates not in CheckerboardPosition.nodesDictionary):
            CheckerboardPosition.nodesDictionary[self.coordinates] = self
        
    def addLevel(self,level):
        self.level = level
        if(self.level > CheckerboardPosition.maxLevel):
                CheckerboardPosition.maxLevel = self.level
        
    def addMove(self, move):
        '''Adds a player move to the current state, throws an exception if'''
        print('self.coordinates'+str(self.coordinates))
        
        if self.move == None:
            self.move = move
            self.moveChain[0].chainCount = 1
            self.moveChain[1].chainCount = 1
            self.moveChain[2].chainCount = 1
            self.moveChain[3].chainCount = 1
            
            if(self.north != None and self.north.move == self.move):
                self.moveChain[0].chainCount += self.north.moveChain[0].chainCount
                self.north.moveChain[0] = self.moveChain[0]
                
                print('Orientation '+ str('N'))
                print('self.moveChain[0].chainCount '+ str(self.moveChain[0].chainCount))
            if(self.northEast != None and self.northEast.move == self.move):
                self.moveChain[1].chainCount += self.northEast.moveChain[1].chainCount
                self.northEast.moveChain[1] = self.moveChain[1]
                
                print('Orientation'+ str('NE'))
                print('self.moveChain[2].chainCount ' + str(self.moveChain[1].chainCount))
            if(self.east != None and self.east.move == self.move):
                self.moveChain[2].chainCount += self.east.moveChain[2].chainCount
                self.east.moveChain[2] = self.moveChain[2]
                
                print('Orientation'+ str('E'))
                print('self.moveChain[2].chainCount '+ str(self.moveChain[2].chainCount))
            if(self.southEast != None and self.southEast.move == self.move):
                self.moveChain[3].chainCount += self.southEast.moveChain[3].chainCount
                self.southEast.moveChain[3] = self.moveChain[3]

                print('Orientation'+ str('SE'))                
                print('self.moveChain[3].chainCount'+ str(self.moveChain[3].chainCount))
            if(self.south != None and self.south.move == self.move):
                self.moveChain[0].chainCount += self.south.moveChain[0].chainCount
                self.south.moveChain[0] = self.moveChain[0]
                
                print('Orientation'+ str('S'))
                print('self.moveChain[0].chainCount'+ str(self.moveChain[0].chainCount))
            if(self.southWest != None and self.southWest.move == self.move):
                self.moveChain[1].chainCount += self.southWest.moveChain[1].chainCount
                self.southWest.moveChain[1] = self.moveChain[1]
                
                print('Orientation'+ str('SW'))
                print('self.moveChain[1].chainCount'+ str(self.moveChain[1].chainCount))
            if(self.west != None and self.west.move == self.move):
                self.moveChain[2].chainCount += self.west.moveChain[2].chainCount
                self.west.moveChain[2] = self.moveChain[2]
                
                print('Orientation'+ str('W'))
                print('self.moveChain[2].chainCount'+ str(self.moveChain[2].chainCount))
            if(self.northWest != None and self.northWest.move == self.move):
                self.moveChain[3].chainCount += self.northWest.moveChain[3].chainCount
                self.northWest.moveChain[3] = self.moveChain[3]
                
                print('Orientation'+ str('NW'))
                print('self.moveChain[3].chainCount'+ str(self.moveChain[3].chainCount))
                
        else:
            raise ValueError('This position was already marked')
        
    def addNorthPosition(self, checkerboardPosition):
        '''Adds a CheckerBoardPosition object to the north position'''
        if(isinstance(checkerboardPosition, CheckerboardPosition)):
            self.north = checkerboardPosition
        else:
            raise ValueError('Position object must be a CheckerboardPosition')
        
    def addNorthEastPosition(self, checkerboardPosition):
        '''Adds a CheckerBoardPosition object to the north position'''
        if(isinstance(checkerboardPosition, CheckerboardPosition)):
            self.northEast = checkerboardPosition
        else:
            raise ValueError('Position object must be a CheckerboardPosition')
        
    def addEastPosition(self, checkerboardPosition):
        '''Adds a CheckerBoardPosition object to the north position'''
        if(isinstance(checkerboardPosition, CheckerboardPosition)):
            self.east = checkerboardPosition
        else:
            raise ValueError('Position object must be a CheckerboardPosition')
        
    def addSouthEastPosition(self, checkerboardPosition):
        '''Adds a CheckerBoardPosition object to the north position'''
        if(isinstance(checkerboardPosition, CheckerboardPosition)):
            self.southEast = checkerboardPosition
        else:
            raise ValueError('Position object must be a CheckerboardPosition')
        
    def addSouthPosition(self, checkerboardPosition):
        '''Adds a CheckerBoardPosition object to the north position'''
        if(isinstance(checkerboardPosition, CheckerboardPosition)):
            self.south = checkerboardPosition
        else:
            raise ValueError('Position object must be a CheckerboardPosition')
        
    def addSouthWestPosition(self, checkerboardPosition):
        '''Adds a CheckerBoardPosition object to the north position'''
        if(isinstance(checkerboardPosition, CheckerboardPosition)):
            self.southWest = checkerboardPosition
        else:
            raise ValueError('Position object must be a CheckerboardPosition')
        
    def addWestPosition(self, checkerboardPosition):
        '''Adds a CheckerBoardPosition object to the north position'''
        if(isinstance(checkerboardPosition, CheckerboardPosition)):
            self.west = checkerboardPosition
        else:
            raise ValueError('Position object must be a CheckerboardPosition')
        
    def addNorthWestPosition(self, checkerboardPosition):
        '''Adds a CheckerBoardPosition object to the north position'''
        if(isinstance(checkerboardPosition, CheckerboardPosition)):
            self.northWest = checkerboardPosition
        else:
            raise ValueError('Position object must be a CheckerboardPosition')
                    
    def linkPosition(self, position, linkDirection, recursive):
        '''Careful with this function, it can mix the links of other positions!'''
        
        if(isinstance(position, CheckerboardPosition)):
            
            '''If position has no level or was discovered by a position father in the grid, updates level'''
            if((position.level == 0 or position.level < self.level) and not recursive):
                position.addLevel(self.level+1)
            
            '''Expands nodes only when checked for moves to save some memory'''
            if(linkDirection == 'N'):          
                self.north = position
                if (not recursive):
                    position.linkPosition(self, 'S', True)  
                    if(self.northEast):
                        position.linkPosition(self.northEast, 'E', True)
                    if(self.northWest):
                        position.linkPosition(self.northWest, 'W', True)
                    if(self.east):
                        position.linkPosition(self.northEast, 'SE', True)
                    if(self.west):
                        position.linkPosition(self.northWest, 'SW', True)
            if(linkDirection == 'NE'):
                self.northEast = position
                if (not recursive):
                    position.linkPosition(self, 'SW', True)
                    if(self.east):
                        position.linkPosition(self.east, 'S', True)
                    if(self.north):
                        position.linkPosition(self.north, 'W', True)
            if(linkDirection == 'E'):           
                self.east = position            
                if (not recursive):
                    position.linkPosition(self, 'W', True)
                    if(self.northEast):
                        position.linkPosition(self.northEast, 'N', True)
                    if(self.southEast):
                        position.linkPosition(self.southEast, 'S', True)
                    if(self.north):
                        position.linkPosition(self.north, 'NW', True)
                    if(self.south):
                        position.linkPosition(self.south, 'SW', True)
            if(linkDirection == 'SE'):       
                self.southEast = position
                if (not recursive):
                    position.linkPosition(self, 'NW', True)
                    if(self.east):
                        position.linkPosition(self.east, 'N', True)
                    if(self.south):
                        position.linkPosition(self.south, 'W', True)
            if(linkDirection == 'S'):           
                self.south = position 
                if (not recursive):
                    position.linkPosition(self, 'N', True)
                    if(self.southEast):
                        position.linkPosition(self.southEast, 'E', True)
                    if(self.southWest):
                        position.linkPosition(self.southWest, 'W', True)
                    if(self.east):
                        position.linkPosition(self.north, 'NE', True)
                    if(self.west):
                        position.linkPosition(self.south, 'NW', True)
            if(linkDirection == 'SW'):           
                self.southWest = position    
                if (not recursive):
                    position.linkPosition(self, 'NE', True)
                    if(self.west):
                        position.linkPosition(self.west, 'N', True)
                    if(self.south):
                        position.linkPosition(self.south, 'E', True)
            if(linkDirection == 'W'):         
                self.west = position      
                if (not recursive):
                    position.linkPosition(self, 'E', True)
                    if(self.southWest):
                        position.linkPosition(self.southWest, 'S', True)
                    if(self.northWest):
                        position.linkPosition(self.northWest, 'N', True)
                    if(self.north):
                        position.linkPosition(self.north, 'NE', True)
                    if(self.south):
                        position.linkPosition(self.south, 'SE', True)
            if(linkDirection == 'NW'):        
                self.northWest = position
                if (not recursive):
                    position.linkPosition(self, 'SE', True)
                    if(self.west):
                        position.linkPosition(self.west, 'S', True)
                    if(self.north):
                        position.linkPosition(self.north, 'E', True)
        elif(not recursive):
            raise ValueError('Position object must be a CheckerboardPosition')
                             
    def getOpenPositions(self, createdNodes):
        '''Returns the whole structure, could lag due to recursivity'''
        
        if (self.north != None and not self.north in createdNodes):
            createdNodes.add(self.north)
            createdNodes.addAll(self.north.getOpenPositions(createdNodes))
        elif (self.northEast != None and not self.northEast in createdNodes):
            createdNodes.add(self.northEast)
            createdNodes.addAll(self.northEast.getOpenPositions(createdNodes))
        elif (self.east != None and not self.east in createdNodes):
            createdNodes.add(self.east)
            createdNodes.addAll(self.east.getOpenPositions(createdNodes))
        elif (self.southEast != None and not self.southEast in createdNodes):
            createdNodes.add(self.southEast)
            createdNodes.addAll(self.southEast.getOpenPositions(createdNodes))
        elif (self.south != None and not self.south in createdNodes):
            createdNodes.add(self.south)
            createdNodes.addAll(self.south.getOpenPositions(createdNodes))
        elif (self.southWest != None and not self.southWest in createdNodes):
            createdNodes.add(self.southWest)
            createdNodes.addAll(self.southWest.getOpenPositions(createdNodes))
        elif (self.west != None and not self.west in createdNodes):
            createdNodes.add(self.west)
            createdNodes.addAll(self.west.getOpenPositions(createdNodes))
        elif (self.northWest != None and not self.northWest in createdNodes):
            createdNodes.add(self.northWest)
            createdNodes.addAll(self.northWest.getOpenPositions(createdNodes))
            
        return createdNodes
    
'''Class for Assignment 2 problems code.'''
class GithubCode:
    def argmin(self, seq, fn):
        """Return an element with lowest fn(seq[i]) score; tie goes to first one.
        >>> argmin(['one', 'to', 'three'], len)
        'to'
        """
        best = seq[0]; best_score = fn(best)
        for x in seq:
            x_score = fn(x)
            if x_score < best_score:
                best, best_score = x, x_score
        return best
    def argmax(self, seq, fn):
        """Return an element with highest fn(seq[i]) score; tie goes to first one.
        >>> argmax(['one', 'to', 'three'], len)
        'three'
        """
        return self.argmin(seq, lambda x: -fn(x))
    def alphabeta_search(self, state, game, d=float('inf'), cutoff_test=None, eval_fn=None):
        """Search game to determine best action; use alpha-beta pruning.
        This version cuts off search and uses an evaluation function."""
        player = game.to_move(state)
        def max_value(state, alpha, beta, depth):
            if cutoff_test(state):
                return eval_fn(state, player)
            v = eval_fn(state, player)
            for (a, s) in game.successors(state):
                v = max(v, min_value(s, alpha, beta, depth+1))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v
    
        def min_value(state, alpha, beta, depth):
            if cutoff_test != None:
                return eval_fn(state, player)
            v = eval_fn(state, player)
            for (a, s) in game.successors(state):
                v = min(v, max_value(s, alpha, beta, depth+1))
                if v <= alpha:
                    return v
                beta = min(beta, v)
            return v
    
        # Body of alphabeta_search starts here:
        # The default test cuts off at depth d or at a terminal state
        cutoff_test = (cutoff_test or
                       (lambda state,depth: depth>d or game.terminal_test(state)))
        eval_fn = eval_fn or (lambda state, player: game.utility(state, player))
        action, state = self.argmax(game.successors(state),
                               lambda ((a, s)): min_value(s, -float('inf'), float('inf'), 0))
        print(action)
        return action
    
    def isnumber(self, x):
        "Is x a number? We say it is if it has a __int__ method."
        return hasattr(x, '__int__')
    
    def num_or_str(self, x):
        """The argument is a string; convert to a number if possible, or strip it.
        >>> num_or_str('42')
        42
        >>> num_or_str(' 42x ')
        '42x'
        """
        if self.isnumber(x): return x
        elif(',' in x):
            x = x.replace('(', '').replace(')', '')
            splitArray = x.split(',')
            return (int(splitArray[0].replace(',', '')), int(splitArray[1].replace(',', '')))
        try:
            return int(x)
        except ValueError:
            try:
                return float(x)
            except ValueError:
                    return str(x).strip()
                
    def query_player(self, game, state):
        "Make a move by querying standard input."
        return self.num_or_str(raw_input('Your move? '))

    def random_player(self, game, state):
        "A player that chooses a legal move at random."
        return random.choice(game.legal_moves(state))
    
    def alphabeta_player(self, game, state):
        return self.alphabeta_search(state, game)
    
    def play_game(self, game, *players):
        "Play an n-person, move-alternating game."
        state = game.initial
        print(state)
        while True:
            for player in players:
                print str(player)
                move = player(game, state)
                state = game.make_move(move, state, False)
                print(state)
                if game.terminal_test(state):
                    return game.utility(state, 0)

class Struct:
    """Create an instance with argument=value slots.
    This is for making a lightweight object whose class doesn't matter."""
    def __init__(self, **entries):
        self.__dict__.update(entries)

    def __cmp__(self, other):
        if isinstance(other, Struct):
            return cmp(self.__dict__, other.__dict__)
        else:
            return cmp(self.__dict__, other)

    def __repr__(self):
        args = ['%s=%s' % (k, repr(v)) for (k, v) in vars(self).items()]
        return 'Struct(%s)' % ', '.join(args)

class OpenFieldTicTacToe:
    def __init__(self, fieldTree):
        self.initial = Struct(to_move=0, fieldTree = fieldTree)
    
    def legal_moves(self, state):
        
        legalMoves = []
        
        '''Expands nodes only when checked for moves to save some memory'''
        if(state.fieldTree.north == None):
            northPosition = CheckerboardPosition((state.fieldTree.coordinates[0], state.fieldTree.coordinates[1]+1))
            northPosition.addToNodesDictionary()
            state.fieldTree.linkPosition(northPosition, 'N', False)
        if(state.fieldTree.northEast == None):
            northEastPosition = CheckerboardPosition((state.fieldTree.coordinates[0]+1, state.fieldTree.coordinates[1]+1))
            northEastPosition.addToNodesDictionary()
            state.fieldTree.linkPosition(northEastPosition, 'NE', False)
        if(state.fieldTree.east == None):
            eastPosition = CheckerboardPosition((state.fieldTree.coordinates[0]+1, state.fieldTree.coordinates[1]))
            eastPosition.addToNodesDictionary()
            state.fieldTree.linkPosition(eastPosition, 'E', False)
        if(state.fieldTree.southEast == None):
            southEastPosition = CheckerboardPosition((state.fieldTree.coordinates[0]+1, state.fieldTree.coordinates[1]-1))
            southEastPosition.addToNodesDictionary()
            state.fieldTree.linkPosition(southEastPosition, 'SE', False)
        if(state.fieldTree.south == None):
            southPosition = CheckerboardPosition((state.fieldTree.coordinates[0], state.fieldTree.coordinates[1]-1))
            southPosition.addToNodesDictionary()
            state.fieldTree.linkPosition(southPosition, 'S', False)
        if(state.fieldTree.southWest == None):
            southWestPosition = CheckerboardPosition((state.fieldTree.coordinates[0]-1, state.fieldTree.coordinates[1]-1))
            southWestPosition.addToNodesDictionary()
            state.fieldTree.linkPosition(southWestPosition, 'SW', False)
        if(state.fieldTree.west == None):
            westPosition = CheckerboardPosition((state.fieldTree.coordinates[0]-1, state.fieldTree.coordinates[1]))
            westPosition.addToNodesDictionary()
            state.fieldTree.linkPosition(westPosition, 'W', False)
        if(state.fieldTree.move == None):
            northWestPosition = CheckerboardPosition((state.fieldTree.coordinates[0]-1, state.fieldTree.coordinates[1]+1))
            northWestPosition.addToNodesDictionary()
            state.fieldTree.linkPosition(northWestPosition, 'NW', False)
        
        '''Adds empty nodes to the possible moves'''
        for coordinates in CheckerboardPosition.nodesDictionary:
            node = copy.copy(CheckerboardPosition.nodesDictionary[coordinates])
            if(coordinates not in  legalMoves and node.move == None):
                legalMoves.append(coordinates)
                for prospectedCoordinateX in range(coordinates[0]-5, coordinates[0]+5):
                    for prospectedCoordinateI in range(coordinates[1]-5, coordinates[1]+5):
                        prospectedTulpe = (prospectedCoordinateX, prospectedCoordinateI)
                        if(prospectedTulpe not in  legalMoves):
                            legalMoves.append(prospectedTulpe)
        return legalMoves

    def make_move(self, move, state, testMove):            
        
        north = None
        northEast = None
        east = None
        southEast = None
        south = None
        southWest = None
        west = None
        northWest = None
        
        '''Checks if the move is on the dictionary, creates it otherwise'''
        if(move in CheckerboardPosition.nodesDictionary):
            targetNode = CheckerboardPosition.nodesDictionary[move]
        else:
            targetNode = CheckerboardPosition(move)
        
        '''Fetches all adjacent nodes to later link them to the move'''
        auxTuple = (move[0], move[1]+1)
            
        if(auxTuple in CheckerboardPosition.nodesDictionary):    
            north = CheckerboardPosition.nodesDictionary[auxTuple]
            
        auxTuple = (move[0]+1, move[1]+1)
            
        if(auxTuple in CheckerboardPosition.nodesDictionary):
            northEast = CheckerboardPosition.nodesDictionary[auxTuple]
        auxTuple = (move[0]+1, move[1])
            
        if(auxTuple in CheckerboardPosition.nodesDictionary):       
            east = CheckerboardPosition.nodesDictionary[auxTuple]
            
        auxTuple = (move[0]+1, move[1]-1)
            
        if(auxTuple in CheckerboardPosition.nodesDictionary):       
            southEast = CheckerboardPosition.nodesDictionary[auxTuple]
            
        auxTuple = (move[0], move[1]-1)
            
        if(auxTuple in CheckerboardPosition.nodesDictionary):       
            south = CheckerboardPosition.nodesDictionary[auxTuple]
            
        auxTuple = (move[0]-1, move[1]-1)
            
        if(auxTuple in CheckerboardPosition.nodesDictionary):       
            southWest = CheckerboardPosition.nodesDictionary[auxTuple]
            
        auxTuple = (move[0]-1, move[1])
            
        if(auxTuple in CheckerboardPosition.nodesDictionary):       
            west = CheckerboardPosition.nodesDictionary[auxTuple]
            
        auxTuple = (move[0]-1, move[1]+1)
            
        if(auxTuple in CheckerboardPosition.nodesDictionary):       
            northWest = CheckerboardPosition.nodesDictionary[auxTuple]
        
        '''Creates copies of all the nodes to avoid altering the actual game state while making calculations'''
        if(testMove):
            
            targetNode = copy.copy(targetNode)
            targetNode.level = (abs(move[0]) + abs(move[1]) )
            
            if(north != None):    
                north = copy.copy(north)
            
            if(northEast != None):
                northEast = copy.copy(northEast)
            
            if(east != None):       
                east = copy.copy(east)
            
            if(southEast != None):       
                southEast = copy.copy(southEast)
                
            if(south != None):       
                south = copy.copy(south)
            
            if(southWest != None):       
                southWest = copy.copy(southWest)
            
            if(west != None):       
                west = copy.copy(west)
            
            if(northWest != None):       
                northWest = copy.copy(northWest)
        else:
            '''The level must move up to continue calculations, but if addLevel method is called, it will modify the actual game state, thus it must only be 
            raised when it is a real move'''
            targetNode.addLevel(abs(move[0]) + abs(move[1]) )
            
        if(targetNode.move == None):
            if(north != None and targetNode.north == None):    
                targetNode.linkPosition(north, 'N', False)
            
            if(northEast != None and targetNode.northEast == None):
                targetNode.linkPosition(northEast, 'NE', False)
            
            if(east != None and targetNode.east == None):   
                targetNode.linkPosition(east, 'E', False)
            
            if(southEast != None and targetNode.southEast == None):
                targetNode.linkPosition(southEast, 'SE', False)
                
            if(south != None and targetNode.south == None):
                targetNode.linkPosition(south, 'S', False)
            
            if(southWest != None and targetNode.southWest == None):
                targetNode.linkPosition(southWest, 'SW', False)
            
            if(west != None and targetNode.west == None):
                targetNode.linkPosition(west, 'W', False)
            
            if(northWest != None and targetNode.northWest == None):
                targetNode.linkPosition(northWest, 'NW', False)
                
            targetNode.addMove(state.to_move)
                
        return Struct(to_move = 1 - state.to_move, fieldTree = state.fieldTree) 
        
        "Return the state that results from making a move from a state."
        
    def utility(self, state, player):
        "Return the value of this final state to player."
        if state.to_move == player:
            return -1
        else:
            return 1
        
    def terminal_test(self, state):
        "Return True if this is a final state for the game."
        
        for countI in range(-CheckerboardPosition.maxLevel, CheckerboardPosition.maxLevel+1):
            for countJ in range(-CheckerboardPosition.maxLevel, CheckerboardPosition.maxLevel+1):
                tupleToCheck = (countI, countJ)
                if(tupleToCheck in CheckerboardPosition.nodesDictionary):
                    #print('tupleToCheck '+str(tupleToCheck))
                    #print('CheckerboardPosition.nodesDictionary[tupleToCheck].moveChain '+str(CheckerboardPosition.nodesDictionary[tupleToCheck].moveChain))
                    for struct in CheckerboardPosition.nodesDictionary[tupleToCheck].moveChain:
                        if(struct.chainCount >= 4):
                            return True
        return False
    
    def to_move(self, state):
        "Return the player whose move it is in this state."
        return state.to_move
    
    def display(self, state):
        "Print or otherwise display the state."
        print state
        
    def successors(self, state):
        "Return a list of legal (move, state) pairs."
        return [(move, self.make_move(move, state, True))
                for move in self.legal_moves(state)]
        
    def __repr__(self):
        return '<%s>' % self.__class__.__name__  
class Assignment2():
    def __init__(self):
        self.githubCode = GithubCode()
    
    def eval_fn_open_field_tic_tac_toe(self, state, player):
        "Return the value of this final state to player."
        if state.to_move == player:
            return -1
        else:
            return 1
    def cutfoff_fn_open_field_tic_tac_toe(self, state):
        if(state.level > (CheckerboardPosition.maxLevel+ 5 )):
            return True
        return False
    def smart_player_open_field_tic_tac_toe(self, game, state):
        return self.githubCode.alphabeta_search(state, game, float('inf'), self.cutfoff_fn_open_field_tic_tac_toe, self.eval_fn_open_field_tic_tac_toe)

    def playOpenFieldTicTacToeTest(self):
        firstPosition = CheckerboardPosition((0,0))
        firstPosition.addToaddToNodesDictionary()
                
        result = self.githubCode.play_game(OpenFieldTicTacToe(firstPosition), self.smart_player_open_field_tic_tac_toe, self.githubCode.query_player)
        if result == 1:
            print "CPU wins"
        else:
            print "Player wins"
            
    def playOpenFieldTicTacToe(self):
            
        firstPosition = CheckerboardPosition((0,0))
        firstPosition.addToNodesDictionary()
            
        result = self.githubCode.play_game(OpenFieldTicTacToe(firstPosition), self.smart_player_open_field_tic_tac_toe, self.githubCode.query_player)
        if result == 1:
            print "CPU wins"
        else:
            print "Player wins"
        
assignment2 = Assignment2()
assignment2.playOpenFieldTicTacToe()
    