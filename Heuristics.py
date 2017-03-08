'''Package to define Data Structures'''
import abc
'''Class that represents a possible Heuristic'''
class Heuristics:
    def __init__(self):
        print('Starting heuristic')
    @abc.abstractmethod
    def __getHeuristicValueForNode__(self, node):
        '''Metodo no implementado'''
class ManhattanHeuristic(Heuristics):
    def __init__(self):
        print('Using Manhattan Heuristic')
    def __getHeuristicValueForNode__(self, node):
        return 0
