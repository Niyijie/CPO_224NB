from CONSTANT import *


class MatchStrategy(object):
    def isMatch(c, edge):
        return False

# match simple character
class CharMatchStrategy(MatchStrategy):
    def isMatch(self,c, edge):
        return c.__eq__(edge)

# match dot
class DotMatchStrategy(MatchStrategy):
    def isMatch(self,c, edge):
        return (not c.__eq__('\n')) and (not c.__eq__('\r'))

# match digital
class DigitalMatchStrategy(MatchStrategy):
    def isMatch(self,c, edge):
        return str.isdigit(c)

# match space
class SpaceMatchStrategy(MatchStrategy):
    def isMatch(self,c, edge):
        return (c == '\f' or c == '\n' or c == '\r' or c == '\t' or c == ' ')




class MatchStrategyManager(object):
    def __init__(self):
        self.matchStrategyMap = {}
        # 放到策略表中
        self.matchStrategyMap[CHAR] = CharMatchStrategy()
        self.matchStrategyMap['.'] = DotMatchStrategy()
        self.matchStrategyMap['\\d'] = DigitalMatchStrategy()
        self.matchStrategyMap['\\s'] = SpaceMatchStrategy()


    def getStrategy(self,edge):
        if self.matchStrategyMap.__contains__(edge):
            return self.matchStrategyMap.get(edge)
        if len(edge) == 1:
            return self.matchStrategyMap.get(CHAR)
        else:
            return self.matchStrategyMap.get(CHARSET)