
from CONSTANT import *
from exception import *
from futures import *

class WorkItem(object):
    def __init__(self,future:Future,fn,args:list,priority=MIN_PRIORITY)->None:
        self.future = future
        # function to be executed
        self.fn = fn
        # function's argument
        self.args = args
        self.priority = priority

    def run(self)->None:
        self.future.setState(RUNNING)
        if self.args is not None:
            result = self.fn(*self.args) # type: ignore
        else:
            result = self.fn()
        self.future.setResult(result)

    def setPriority(self,priority:int)->None:
        self.priority = priority

    def __lt__(self, other):
        """ define < operation """
        return self.priority > other.priority