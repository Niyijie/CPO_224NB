'''
NFA classes are classes that describe matching rules
If you can go smoothly from the start node to the end node,
the match is successful
'''

from lab2.src.state import *

class NFA(object):
    def __init__(self, start:State, end:State):
        self.start = start
        self.end = end

    def repeatStar(self):
        # Create branches that repeat multiple times
        self.repeatPlus()
        # I'm going to repeat it 0 times, directly to end
        self.addSToE()

    # Repeat 0 times from the start node to the end node
    def addSToE(self):
        self.start.addPath(EPSILON,self.end)

    # Repeat 1 to n times
    def repeatPlus(self):
        # Create new start and end nodes
        newStart = State()
        newEnd = State()
        newStart.addPath(EPSILON,self.start)
        self.end.addPath(EPSILON,newEnd)
        # Refer to start
        self.end.addPath(EPSILON,self.start)
        # Change the reference to make it a new diagram
        self.start = newStart
        self.end = newEnd

    def addSeriesGraph(self,nfaGraph):
        self.end.addPath(EPSILON,nfaGraph.start)
        self.end = nfaGraph.end

    def addParallelGraph(self,edge):
        mid = State()
        self.start.addPath(edge,mid)