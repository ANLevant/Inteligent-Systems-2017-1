'''
Created on 23 de mar. de 2017

Package to define Data Structures
@author: Alejandro Serrano
'''

import abc
import copy
'''Class Node is defined'''
class Node:
    '''Function that initialize a Node with the function parameters setted as
    attributes for the Node'''
    def __init__(self, index, label, nodeTrace):
        self.index = index
        self.label = label
        self.nodeTrace = nodeTrace
        self.moveState = None
        self.nextNode = None
    '''Function that adds or replaces the Metadata attribute'''
    def __addMetadata__(self, moveState):
        self.moveState = copy.copy(moveState)
    '''Function that returns the Metadata attribute'''
    def __getMetadata__(self):
        return self.moveState
    '''Function that adds or replaces the Metadata attribute, which is the parents of the actual node up to the root'''
    def __addNodeTrace__(self, nodeTrace):
        self.nodeTrace = nodeTrace
    '''Function that returns the NodeTrace attribute, which is the parents of the actual node up to the root'''
    def __getNodeTrace__(self):
        return self.nodeTrace
    '''Function that adds or replaces the Label attribute, which is a unique mark to identify each node'''
    def __addLabel__(self, label):
        self.label = label
    '''Function that returns the Label attribute, which is a unique mark to identify each node'''
    def __getLabel__(self):
        return self.label
    '''Function that adds or replaces the NextNode attribute'''
    def __addNextNode__(self, nextNode):
        if(self.nextNode == None):
            self.nextNode = nextNode
        else:
            self.nextNode.__addNextNode__(nextNode)
    '''Function that returns the NextNode attribute'''
    def __getNextNode__(self):
        return self.nextNode
    '''Function that adds or replaces the Index attribute, which is the hierarchic level of this node'''
    def __addIndex__(self, index):
        self.index = index
    '''Function that returns the Index attribute, which is the hierarchic level of this node'''
    def __getIndex__(self):
        return self.index
    '''Function that returns a String representation of this a Node object'''        
    def __str__(self):
        if(self.nextNode != None):
            return 'Index: '+str(self.index)+'\nLabel: '+str(self.label)+'\nNodeTrace: '+str(self.nodeTrace)+'\nmoveState: '+str(self.moveState)+'\nnextNode: '+str(self.nextNode.__getLabel__())
        else:
            return 'Index: '+str(self.index)+'\nLabel: '+str(self.label)+'\nNodeTrace: '+str(self.nodeTrace)+'\nmoveState: '+str(self.moveState)+'\nnextNode: '+str(None)
'''Class DataStructure is defined'''
class DataStructure:
    '''Function that starts the data structure with a single empty node'''
    def __init__(self):
        self.firstNode = Node(0, 0, [])
    '''Function that returns first node and removes it from the DataStructure'''
    @abc.abstractmethod
    def __pop__(self):
        '''Uninmplemented Method'''
    '''Function that puts a new node in the datastructure'''
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
    '''Function that starts the queue with a single empty node'''
    def __init__(self):
        self.firstNode = None
    '''Function that returns first node and removes it from the queue'''
    def __pop__(self):
        aux = self.firstNode
        if(self.firstNode != None):
            self.firstNode = self.firstNode.nextNode
        return aux
    '''Function that puts a new node, leaving it at the end of the queue'''
    def __put__(self, nextNode):
        if(self.firstNode == None):
            self.firstNode = nextNode
        else:
            self.firstNode.__addNextNode__(nextNode)
'''Class Stack'''
class Stack(DataStructure):
    '''Function that starts the stack with a single empty node'''
    def __init__(self):
        self.firstNode = None
    '''Function that returns first node and removes it from the stack'''
    def __pop__(self):
        aux = self.firstNode
        if(self.firstNode != None):
            self.firstNode = aux.__getNextNode__()
        return aux
    '''Function that puts a new node, leaving it at the end of the stack'''
    def __put__(self, nextNode):
        nextNode.__addNextNode__(self.firstNode)
        self.firstNode = nextNode
'''Class Priorized Queue TODO'''