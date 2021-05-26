from lab2.src.state import *
from lab2.src.nfa import *
from lab2.src.reader import *
from lab2.src.strategy import *


class regex(object):
    def __init__(self,partten):
        self.reader = Reader(partten)
        self.nfa = None
        self.matchStrategyManager = MatchStrategyManager()
        self.forceQuit = False

    def compile(self):
        nfaGraph = self.regex2nfa()
        # 标记NFA的end节点为终止节点
        nfaGraph.end.IsEnd = True
        self.nfa = nfaGraph

    def regex2nfa(self):
        nfaGraph = None
        while self.reader.hasNext():
            ch = self.reader.next()
            edge = None
            if ch == '.':
                edge = '.'
            elif ch == '^':
                nextCh = self.reader.next()
                edge = '^' + nextCh
            elif ch == '\\':
                nextCh = self.reader.next()
                if nextCh == 'd':
                    edge = "\\d"
                elif nextCh == 's':
                    edge = '\\s'
                elif nextCh == 'w':
                    edge = '\\w'
                else:
                    edge = nextCh
            else:
                edge = ch

            if edge is not None:
                start = State()
                end = State()
                start.addPath(edge,end)
                newNfa = NFA(start,end)
                self.checkRepeat(newNfa)
                if nfaGraph == None:
                    nfaGraph = newNfa
                else:
                    nfaGraph.addSeriesGraph(newNfa)

        return nfaGraph

    def checkRepeat(self,nfa:NFA):
        ch = self.reader.peak()
        if ch == '*':
            nfa.repeatStar()
            self.reader.next()
        elif ch == '+':
            nfa.repeatPlus()
            self.reader.next()

    def isMatch(self,text):
        start = self.nfa.start
        return self.match(text,0,start)

    def match(self,text,pos,curState:State):
        if self.forceQuit:
            return True
        if pos == len(text):
            stateLst = []
            if curState.edgeMap.__contains__(EPSILON):
                stateLst = curState.edgeMap.get(EPSILON)
            for nextState in stateLst:
                if self.match(text,pos,nextState):
                    return True
            if curState.IsEnd:
                return True
            return False

        for edge in curState.edgeMap.keys():
            if EPSILON.__eq__(edge):
                for nextState in curState.edgeMap.get(edge):
                    if self.match(text,pos,nextState):
                        return True
            else:
                if edge[0] == '^':
                    matchStrategy = self.matchStrategyManager.getStrategy(edge[0])
                else:
                    matchStrategy = self.matchStrategyManager.getStrategy(edge)
                if not matchStrategy.isMatch(text[pos], edge):
                    continue
                elif edge[0] == '^':
                    self.forceQuit = True
                    return True
                for nextState in curState.edgeMap.get(edge):
                    if self.match(text,pos+1,nextState):
                        return True
        return False

