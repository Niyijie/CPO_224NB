from lab2.src.state import *
from lab2.src.nfa import *
from lab2.src.reader import *
from lab2.src.strategy import *

class Regex(object):
    def __init__(self):
        self.reader = None
        self.nfa = None
        self.matchStrategyManager = MatchStrategyManager()
        # use for ^
        self.isHat = False
        # use for $
        self.isDoller = False
        # use for []
        self.isRact = False
        # match index
        self.startIndex = -1
        self.endIndex = -1

    def compile(self,partten):
        self.reader = Reader(partten)
        self.nfa = None
        self.isRact = False
        self.isHat = False
        self.isDoller = False
        self.reader.cur = 0
        nfaGraph = self.regex2nfa()
        # 标记NFA的end节点为终止节点
        nfaGraph.end.IsEnd = True
        self.nfa = nfaGraph

    def parseRepeat_n_m(self,edge,nfaGraph):
        s = ''
        while self.reader.peak() != '}':
            s += self.reader.peak()
            self.reader.next()
        lst = s.split(',')
        # case {n}
        if len(lst) == 1:
            num = int(lst[0])
            for i in range(num-1):
                mid = State()
                nfaGraph.end.addPath(edge,mid)
                nfaGraph.end = mid
        else:
            # case {n,} {,m} {n,m}
            print(123)



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
            # if [^abc] we will matches characters with abd removed
            if self.reader.peak() == '^':
                newStr = 'qwertyuiopasdfghjklzxcvbnm1234567890 '
                while self.reader.hasNext():
                    ch = self.reader.peak()
                    newStr = newStr.replace(ch,'')
                    self.reader.next()
                # use new character set
                self.reader = Reader(newStr)
        while self.reader.hasNext():
            ch = self.reader.next()
            edge = None
            if ch == '.':
                edge = '.'
            elif ch == ']':
                continue
            elif ch == '{':
                self.parseRepeat_n_m(self.reader.get(self.reader.cur-2),nfaGraph)
                continue
            elif ch == '}':
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
        if self.isRact:
            end = State()
            for nextState in nfaGraph.start.edgeMap.values():
                nextState[0].addPath(EPSILON,end)
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

    def match(self,text:str):
        start = self.nfa.start
        # self.startIndex = 0
        if self.isDoller:
            text = text[::-1]
        # index
        startIndex = 0
        endIndex = -1
        # find the match index
        l = len(text)
        for i in range(l):
            subStr = text[:(l-i)]
            ret = self.isMatch(subStr,0,start)
            if ret:
                endIndex = l-i-1
                break
        # return match range
        if endIndex == -1:
            return None
        else:
            if self.isDoller:
                return (l-endIndex-1,l-1+1)
            return (startIndex,endIndex+1)

    def search(self,text:str):
        start = self.nfa.start
        # self.startIndex = 0
        if self.isDoller:
            text = text[::-1]
        # index
        startIndex = 0
        endIndex = -1
        # find the match index
        l1 = len(text)
        for i in range(l1):
            startIndex = i
            subStr1 = text[i:]
            l2 = len(subStr1)
            for j in range(l2):
                subStr2 = subStr1[:(l2-j)]
                ret = self.isMatch(subStr2,0,start)
                if ret:
                    endIndex = l1-j-1
                    if self.isDoller:
                        return (l1 - endIndex - 1, l1 - 1+1)
                    return (startIndex, endIndex+1)
            if self.isHat or self.isDoller:
                break
        if endIndex == -1:
            return None

    def isMatch(self,text,pos,curState:State):
        if pos == len(text):
            stateLst = []
            if curState.edgeMap.__contains__(EPSILON):
                stateLst = curState.edgeMap.get(EPSILON)
            for nextState in stateLst:
                if self.isMatch(text,pos,nextState):
                    return True
            if curState.IsEnd:
                return True
            return False

        for edge in curState.edgeMap.keys():
            if EPSILON.__eq__(edge):
                for nextState in curState.edgeMap.get(edge):
                    if self.isMatch(text,pos,nextState):
                        return True
            else:
                matchStrategy = self.matchStrategyManager.getStrategy(edge)
                if not matchStrategy.isMatch(text[pos], edge):
                    continue
                elif self.isRact and not '.'.__eq__(edge):
                    self.nfa.start.IsEnd = True
                for nextState in curState.edgeMap.get(edge):
                    if self.isMatch(text,pos+1,nextState):
                        return True
        return False