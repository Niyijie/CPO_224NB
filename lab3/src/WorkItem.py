from CONSTANT import *
from exception import *

class WorkItem(object):
    def __init__(self,future,fn,args,priority=MIN_PRIORITY):
        self.future = future
        # function to be executed
        self.fn = fn
        # function's argument
        self.args = args
        self.priority = priority

    def run(self):
        self.future.setState(RUNNING)
        if self.args is not None:
            result = self.fn(*self.args)
        else:
            result = self.fn()
        self.future.setResult(result)

    def setPriority(self,priority):
        self.priority = priority

    def __lt__(self, other):
        """ define < operation """
        return self.priority > other.priority