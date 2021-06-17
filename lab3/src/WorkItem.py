from CONSTANT import *
from exception import *

class WorkItem(object):
    def __init__(self,future,fn,args,kwargs,priority=0):
        self.future = future
        # function to be executed
        self.fn = fn
        # function's argument
        self.args = args
        self.kwargs = kwargs
        self.priority = priority
        #self.run()

    def run(self):
        self.future.setState(RUNNING)
        if self.args is not None:
            result = self.fn(*self.args)
        else:
            result = self.fn()
        self.future.setResult(result)
