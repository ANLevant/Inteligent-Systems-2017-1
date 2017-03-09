'''Package to define Data Structures'''
import abc
import copy
'''Class Node is defined'''
class Node:
    def __init__(self, index, label, nodeTrace):
        self.index = index
        self.label = label
        self.nodeTrace = nodeTrace
        self.moveState = None
        self.nextNode = None
    def __addMetadata__(self, moveState):
        self.moveState = copy.copy(moveState)
    def __getMetadata__(self):
        return self.moveState
    def __addNodeTrace__(self, nodeTrace):
        self.nodeTrace = nodeTrace
    def __getNodeTrace__(self):
        return self.nodeTrace
    def __addLabel__(self, label):
        self.label = label
    def __getLabel__(self):
        return self.label
    def __addNextNode__(self, nextNode):
        if(self.nextNode == None):
            self.nextNode = nextNode
        else:
            self.nextNode.__addNextNode__(nextNode)
    def __getNextNode__(self):
        return self.nextNode
    def __getIndex__(self):
        return self.index
    def __addIndex__(self, index):
        self.index = index
    def __str__(self):
        if(self.nextNode != None):
            return 'Index: '+str(self.index)+'\nLabel: '+str(self.label)+'\nNodeTrace: '+str(self.nodeTrace)+'\nmoveState: '+str(self.moveState)+'\nnextNode: '+str(self.nextNode.__getLabel__())
        else:
            return 'Index: '+str(self.index)+'\nLabel: '+str(self.label)+'\nNodeTrace: '+str(self.nodeTrace)+'\nmoveState: '+str(self.moveState)+'\nnextNode: '+str(None)
'''Class DataStructure is defined'''
class DataStructure:
    def __init__(self):
        self.firstNode = Node(0, 0, [])
    @abc.abstractmethod
    def __pop__(self):
        '''Metodo no implementado'''
    @abc.abstractmethod
    def __put__(self, node):
        '''Metodo no implementado'''
    def __peek__(self):
        return self.firstNode
    def __isEmpty__(self):
        if(self.firstNode == None):
            return True
        else:
            return False
    def __str__(self):
         return str(self.firstNode)
'''Class Queue is Defined'''
class Queue(DataStructure):
    def __init__(self):
        self.firstNode = None
    def __pop__(self):
        aux = self.firstNode
        if(self.firstNode != None):
            self.firstNode = self.firstNode.nextNode
        return aux
    def __put__(self, nextNode):
        if(self.firstNode == None):
            self.firstNode = nextNode
        else:
            self.firstNode.__addNextNode__(nextNode)
'''Class Stack'''
class Stack(DataStructure):
    def __init__(self):
        self.firstNode = None
    def __pop__(self):
        aux = self.firstNode
        if(self.firstNode != None):
            self.firstNode = aux.__getNextNode__()
        return aux
    def __put__(self, nextNode):
        nextNode.__addNextNode__(self.firstNode)
        self.firstNode = nextNode
'''Class Priorized Queue TODO'''