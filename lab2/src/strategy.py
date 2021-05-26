from CONSTANT import *


class MatchStrategy(object):
    def __init__(self):
        self.isReverse = False

    def isMatch(c, edge):
        return False

class CharMatchStrategy(MatchStrategy):
    def isMatch(self,c, edge):
        return c.__eq__(edge)


class MatchStrategyManager(object):
    def __init__(self):
        self.matchStrategyMap = {}
        charMatchStrategy = CharMatchStrategy()

        # 放到策略表中
        self.matchStrategyMap[CHAR] = charMatchStrategy

    def getStrategy(self,edge):
        if self.matchStrategyMap.__contains__(edge):
            return self.matchStrategyMap.get(edge)
        if len(edge) == 1:
            return self.matchStrategyMap.get(CHAR)
        else:
            return self.matchStrategyMap.get(CHARSET)