import threading

from CONSTANT import *
from exception import *


class Futures(object):
    def __init__(self):
        self.state = PENDING
        self.result = None
        self.condition = threading.Condition()
        self.id = getId()

    def IsDone(self):
        return FINISHED == self.state

    def IsProgress(self):
        return RUNNING == self.state

    def Result(self,timeout=None):
        if self.state == FINISHED:
            self.setState(FINISHED)
            return self.result
        elif self.state == CANCELED:
            raise CanceledException(self.id)
        else:
            self.condition.wait(timeout)
            if self.state == FINISHED:
                self.setState(FINISHED)
                return self.result
            elif self.state == CANCELED:
                raise CanceledException(self.id)
            else:
                raise TimeoutError(self.id)

    def Cancel(self):
        if self.state != FINISHED:
            self.setState(CANCELED)

    def setState(self,state):
        self.state = state

    def setResult(self,result):
        self.result = result
        self.setState(FINISHED)
