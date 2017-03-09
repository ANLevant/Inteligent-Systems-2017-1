'''Package to define Data Structures'''
import abc
'''Class that represents a possible Heuristic'''
class MyHeuristics:
    def __init__(self):
        print('Starting heuristic')
    @abc.abstractmethod
    def __getHeuristicValueForNode__(self, node):
        '''Metodo no implementado'''
class ManhattanHeuristic(MyHeuristics):
    def __init__(self):
        print('Using Manhattan Heuristic')
    def __getHeuristicValueForNode__(self, node):
        return 0
class ZeroHeuristic(MyHeuristics):
    def __init__(self):
        print('Using Zero Heuristic')
    def __getHeuristicValueForNode__(self, node):
        return 0
class NumberOfRepeatedPolarsHeuristic(MyHeuristics):
    def __init__(self):
        print('Using Zero Heuristic')
    def __getHeuristicValueForNode__(self, node):
        tileCount = 0;
        matrix = node.__getMetadata__()
        row0 = matrix[0]
        row1 = matrix[len(matrix)-1]
        auxCount1 = 0
        auxCount2 = auxCount1 + 1
        while(auxCount1 < len(row0)):
            while(auxCount2 < len(row0)):
                if(row0[auxCount1] == row0[auxCount2] ):
                    tileCount += 1
                if(row1[auxCount1] == row1[auxCount2] ):
                    tileCount += 1
                auxCount2+=1
            auxCount1+=1
            auxCount2=auxCount1+1
        return tileCount
