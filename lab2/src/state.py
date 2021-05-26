from CONSTANT import *

class State:
    def __init__(self):
        self.ID = getId()
        self.IsEnd = False
        self.edgeMap = {}


    def addPath(self,edge,nfaState):
        if self.edgeMap.__contains__(edge):
            self.edgeMap[edge].append(nfaState)
        else:
            self.edgeMap[edge] = []
            self.edgeMap[edge].append(nfaState)

