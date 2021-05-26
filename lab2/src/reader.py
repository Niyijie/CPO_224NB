class Reader(object):
    def __init__(self,partten):
        self.string = partten
        self.cur = 0

    def tail(self):
        return self.string[-1]

    def peak(self):
        if self.cur == len(self.string):
            return '\0'

        return self.string[self.cur]

    def next(self):
        if self.cur == len(self.string):
            return '\0'
        index = self.cur
        self.cur += 1
        return self.string[index]

    def hasNext(self):
        return self.cur < len(self.string)