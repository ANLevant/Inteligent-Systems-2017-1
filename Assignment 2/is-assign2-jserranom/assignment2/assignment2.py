'''
Created on 23 de mar. de 2017

@author: Alejandro Serrano
'''
'''Start of package'''

import abc
import random
import copy

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
    def __init__(self, level):
        self.move = None
        self.level = level
        
    def addMove(self, move):
        '''Adds a player move to the current state, throws an exception if'''
        if self.move == None:
            self.move = move
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
            if(position.level == None or position.level < self.level):
                position.level = (self.level+1)
            
            '''Expands nodes only when checked for moves to save some memory'''
            if(linkDirection == 'N'):          
                self.north = position
                if (not recursive):
                    position.linkPosition(self, 'S', True)  
            if(linkDirection == 'NE'):
                self.northEast = position
                if (not recursive):
                    position.linkPosition(self, 'SW', True)
                    position.linkPosition(self.east, 'S', True)
                    position.linkPosition(self.north, 'W', True)
            if(linkDirection == 'E'):           
                self.east = position            
                if (not recursive):
                    position.linkPosition(self, 'E', True)
            if(linkDirection == 'SE'):       
                self.southEast = position
                if (not recursive):
                    position.linkPosition(self, 'NW', True)
                    position.linkPosition(self.east, 'N', True)
                    position.linkPosition(self.south, 'W', True)
            if(linkDirection == 'S'):           
                self.south = position 
                if (not recursive):
                    position.linkPosition(self, 'N', True)
            if(linkDirection == 'SW'):           
                self.southWest = position    
                if (not recursive):
                    position.linkPosition(self, 'NE', True)
                    position.linkPosition(self.west, 'N', True)
                    position.linkPosition(self.south, 'E', True)
            if(linkDirection == 'W'):         
                self.west = position      
                if (not recursive):
                    position.linkPosition(self, 'E', True)
            if(linkDirection == 'NW'):        
                self.northWest = position
                if (not recursive):
                    position.linkPosition(self, 'SE', True)
                    position.linkPosition(self.west, 'S', True)
                    position.linkPosition(self.north, 'E', True)
        else:
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
            if cutoff_test != None:
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
                state = game.make_move(move, state)
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
    
class LastStone(Game):
    def __init__(self, stones):
        self.initial = Struct(to_move=0, heap = stones)

    def legal_moves(self, state):
        "Return a list of the allowable moves at this point."
        return range(1, min(3, state.heap) + 1)

    def make_move(self, move, state):
        "Return the state that results from making a move from a state."
        return Struct(to_move = 1 - state.to_move,
                      heap = state.heap - move)
        
    def utility(self, state, player):
        "Return the value of this final state to player."
        if state.to_move == player:
            return -1
        else:
            return 1
        
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
    
class ThreeHeapLastStone(Game):
    def __init__(self, heaps):
        self.initial = Struct(to_move=0, heaps = heaps)

    def legal_moves(self, state):
        "Return a list of the allowable moves at this point."        
        legalMoves = []
        
        for x in range (0,3):
            if(state.heaps[x] != 0):
                legalMoves.append((x,range(1, min(3, state.heaps[x]) + 1)))
                
        return legalMoves

    def make_move(self, move, state):
        "Return the state that results from making a move from a state."
        heaps = copy.copy(state.heaps)
        heaps[move[0]] = state.heaps[move[0]] - move[1]
        return Struct(to_move = 1 - state.to_move,
                      heaps = heaps)
        
    def utility(self, state, player):
        "Return the value of this final state to player."
        if state.to_move == player:
            return -1
        else:
            return 1
        
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
        
        succesorMoves = []
        
        for heapMoves in self.legal_moves(state):
            for move in heapMoves[1]:
                wholeMove = (heapMoves[0], move)
                succesorMoves.append((wholeMove, self.make_move(wholeMove, state)))
        return succesorMoves
    
class OpenFieldTicTacToe:
    def __init__(self, fieldTree):
        self.initial = Struct(to_move=0, fieldTree = fieldTree)
    
    def legal_moves(self, state):
        
        '''Expands nodes only when checked for moves to save some memory'''
        if(state.fieldTree.north == None):
            northPosition = CheckerboardPosition()            
            state.fieldTree.linkPosition(northPosition, 'N')
        if(state.fieldTree.northEast == None):
            northEastPosition = CheckerboardPosition()             
            state.fieldTree.linkPosition(northEastPosition, 'NE')
        if(state.fieldTree.east == None):
            eastPosition = CheckerboardPosition() 
            state.fieldTree.linkPosition(eastPosition, 'E')
        if(state.fieldTree.southEast == None):
            southEastPosition = CheckerboardPosition() 
            state.fieldTree.linkPosition(southEastPosition, 'SE')
        if(state.fieldTree.south == None):
            southPosition = CheckerboardPosition()            
            state.fieldTree.linkPosition(southPosition, 'S') 
        if(state.fieldTree.southWest == None):
            southWestPosition = CheckerboardPosition() 
            state.fieldTree.linkPosition(southWestPosition, 'SW')
        if(state.fieldTree.initial.west == None):
            westPosition = CheckerboardPosition() 
            state.fieldTree.linkPosition(westPosition, 'W')
        if(state.fieldTree.northWest.move == None):
            northWestPosition = CheckerboardPosition() 
            state.fieldTree.linkPosition(northWestPosition, 'NW')
        
        '''Adds empty nodes to the possible moves'''
       
            
        return range()

    def make_move(self, move, state):
        
        inputCode = move.split('|')
        
        for code in inputCode:
            if(code == 'H'):
                state.fieldTree.addMove(state.to_move)
                break
            elif (code == 'N-'):
                if(state.fieldTree.north == None):
                    northPosition = CheckerboardPosition()            
                    state.fieldTree.linkPosition(northPosition, 'N')
                state.fieldTree = state.fieldTree.north
            elif (code == 'NE-'):
                if(state.fieldTree.north == None):
                    northEastPosition = CheckerboardPosition()            
                    state.fieldTree.linkPosition(northEastPosition, 'NE')
                state.fieldTree = state.fieldTree.northEast
            elif (code == 'E-'):
                if(state.fieldTree.east == None):        
                    eastPosition = CheckerboardPosition()  
                    state.fieldTree.linkPosition(eastPosition, 'E')
                state.fieldTree = state.fieldTree.east
            elif (code == 'SE-'):
                if(state.fieldTree.southEast == None):
                    southEastPosition = CheckerboardPosition()            
                    state.fieldTree.linkPosition(southEastPosition, 'SE')
                state.fieldTree = state.fieldTree.southEast
            elif (code == 'S-'):
                if(state.fieldTree.south == None):
                    southPosition = CheckerboardPosition()            
                    state.fieldTree.linkPosition(southPosition, 'S')
                state.fieldTree = state.fieldTree.south
            elif (code == 'SW-'):
                if(state.fieldTree.southWest == None):
                    southWestPosition = CheckerboardPosition()            
                    state.fieldTree.linkPosition(southWestPosition, 'SW')
                state.fieldTree = state.fieldTree.southWest
            elif (code == 'W-'):
                if(state.fieldTree.west == None):
                    westPosition = CheckerboardPosition()            
                    state.fieldTree.linkPosition(westPosition, 'W')
                state.fieldTree = state.fieldTree.west
            elif (code == 'NW-'):
                if(state.fieldTree.northWest == None):
                    northWestPosition = CheckerboardPosition()            
                    state.fieldTree.linkPosition(northWestPosition, 'NW')
                state.fieldTree = state.fieldTree.northWest     
        
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
class Assignment2():
    def __init__(self):
        self.githubCode = GithubCode()
        
    '''Function based on Nim Sum algorithm'''
    def eval_fn_last_stone(self, state, player):
        binaryRepresentation = list('{0:0b}'.format(state.heap))
        
        count = 1
        if(binaryRepresentation ==['0']):
            return 2
        while count < len(binaryRepresentation):
            
            if(binaryRepresentation[count] != '0'):
                return 0
            
            count+= 1
        
        return 1
    
    '''Function based on Nim Sum algorithm'''
    def eval_fn_three_heap_last_stone(self, state, player):
        binaryRepresentationFirst = list('{0:0b}'.format(state.heaps[0]))
        binaryRepresentationSecond = list('{0:0b}'.format(state.heaps[1]))
        binaryRepresentationThird = list('{0:0b}'.format(state.heaps[2]))
        
        count = 1
        
        moveableValue = False
        if(binaryRepresentationFirst == binaryRepresentationSecond):
            if(binaryRepresentationThird ==['0']):
                return 2
            while count < len(binaryRepresentationThird):
            
                if(binaryRepresentationThird[count] != '0'):
                    return 0
                
                count+= 1
        elif(binaryRepresentationSecond == binaryRepresentationThird):
            if(binaryRepresentationFirst ==['0']):
                return 2
            while count < len(binaryRepresentationFirst):
            
                if(binaryRepresentationFirst[count] != '0'):
                    return 0
                
                count+= 1
        elif(binaryRepresentationFirst == binaryRepresentationThird):
            if(binaryRepresentationSecond ==['0']):
                return 2
            while count < len(binaryRepresentationSecond):
            
                if(binaryRepresentationSecond[count] != '0'):
                    return 0
                
                count+= 1
        else:
            
            binaryRepresentationFirst.reverse()
            binaryRepresentationSecond.reverse()
            binaryRepresentationThird.reverse()
            
            count = 0
            while(count < max(len(binaryRepresentationFirst),len(binaryRepresentationSecond),len(binaryRepresentationThird)) and not moveableValue):
                aux = 0;
                if(len(binaryRepresentationFirst) > count):
                    aux += float(binaryRepresentationFirst[count])
                if(len(binaryRepresentationSecond) > count):
                    aux += float(binaryRepresentationSecond[count])
                if(len(binaryRepresentationThird) > count):
                    aux += float(binaryRepresentationThird[count])
                    
                aux = int(aux%2)
                
                if(aux != 0):
                    return 0
                
                count += 1
        
        return 1
        
    def smart_player_last_stone(self, game, state):
        return self.githubCode.alphabeta_search(state, game, float('inf'),None, self.eval_fn_last_stone)
    
    def smart_player_three_last_stone(self, game, state):
        return self.githubCode.alphabeta_search(state, game, float('inf'),None, self.eval_fn_three_heap_last_stone)
    
    def smart_player_open_field_tic_tac_toe(self, game, state):
        return self.githubCode.alphabeta_search(state, game, float('inf'),None, self.eval_fn_three_heap_last_stone)
    
    def play(self):
        result = self.githubCode.play_game(LastStone(15), self.smart_player_last_stone, self.githubCode.alphabeta_player)
        if result == 1:
            print "Smart player wins"
        else:
            print "Smart player loses"
            
    def playTest(self):
        result = self.githubCode.play_game(LastStone(10), self.githubCode.query_player, self.githubCode.alphabeta_player)
        if result == 1:
            print "Player wins"
        else:
            print "CPU wins"
            
    def playThreeHeapsTest(self):
        result = self.githubCode.play_game(ThreeHeapLastStone([10,10,10]), self.smart_player_three_last_stone, self.githubCode.alphabeta_player)
        if result == 1:
            print "Smart player wins"
        else:
            print "Smart player loses"
    
    def playThreeHeaps(self):
        result = self.githubCode.play_game(ThreeHeapLastStone([10,10,10]), self.smart_player_three_last_stone, self.githubCode.query_player)
        if result == 1:
            print "CPU wins"
        else:
            print "Player wins"
            
    def playOpenFieldTicTacToeTest(self):
        firstPosition = CheckerboardPosition()
            
        result = self.githubCode.play_game(OpenFieldTicTacToe(firstPosition), self.smart_player_three_last_stone, self.githubCode.query_player)
        if result == 1:
            print "CPU wins"
        else:
            print "Player wins"
            
    def playOpenFieldTicTacToe(self):
            
        matrixField = []
            
        matrixField.append([])
            
        result = self.githubCode.play_game(OpenFieldTicTacToe(matrixField), self.smart_player_three_last_stone, self.githubCode.query_player)
        if result == 1:
            print "CPU wins"
        else:
            print "Player wins"
        
assignment2 = Assignment2()
assignment2.playThreeHeapsTest()