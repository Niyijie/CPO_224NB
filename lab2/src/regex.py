from lab2.src.state import *
from lab2.src.nfa import *
from lab2.src.reader import *
from lab2.src.strategy import *

class Regex(object):
    def __init__(self,partten):
        self.reader = Reader(partten)
        self.nfa = None
        self.matchStrategyManager = MatchStrategyManager()
        # use for ^
        self.isHat = False
        # use for $
        self.isDoller = False
        # use for []
        self.isRact = False

    def compile(self):
        self.nfa = None
        self.isRact = False
        self.isHat = False
        self.isDoller = False
        self.reader.cur = 0
        nfaGraph = self.regex2nfa()
        # 标记NFA的end节点为终止节点
        nfaGraph.end.IsEnd = True
        self.nfa = nfaGraph

    def regex2nfa(self):
        nfaGraph = None
        # check ^ and $
        if self.reader.peak() == '^':
            self.isHat = True
            self.reader.next()
        elif self.reader.tail() == '$':
            self.isDoller = True
            # if doller reverse the pattern  abcd -> dcba
            self.reader.string = self.reader.string[::-1]
            self.reader.next()
        elif self.reader.peak() == '[':
            self.isRact = True
            self.reader.next()

        while self.reader.hasNext():
            ch = self.reader.next()
            edge = None
            if ch == '.':
                edge = '.'
            elif ch == ']':
                continue
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
                    if self.isRact:
                        nfaGraph.addParallelGraph(edge)
                    else:
                        nfaGraph.addSeriesGraph(newNfa)
        if self.isHat or self.isDoller:
            mid = State()
            mid.IsEnd = True
            mid.addPath(EPSILON,nfaGraph.end)
            nfaGraph.end.addPath('.',mid)
        if self.isRact:
            end = State()
            for nextState in nfaGraph.start.edgeMap.values():
                nextState[0].addPath(EPSILON,end)
            mid = State()
            nfaGraph.start.addPath('.',mid)
            mid.addPath(EPSILON,nfaGraph.start)
            nfaGraph.end = end
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
        if self.isDoller:
            text = text[::-1]

        return self.match(text,0,start)

    def match(self,text,pos,curState:State):
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
                matchStrategy = self.matchStrategyManager.getStrategy(edge)
                if not matchStrategy.isMatch(text[pos], edge):
                    continue
                elif self.isRact and not '.'.__eq__(edge):
                    self.nfa.start.IsEnd = True
                for nextState in curState.edgeMap.get(edge):
                    if self.match(text,pos+1,nextState):
                        return True
        return False

