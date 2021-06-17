import threading

from CONSTANT import *
from exception import *


class Future(object):
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
        with self.condition:
            if self.state == FINISHED:
                return self.result
            elif self.state == CANCELED:
                raise CanceledException(self.id)
            else:
                # if not finished then wait
                self.condition.wait(timeout)
                if self.state == FINISHED:
                    return self.result
                elif self.state == CANCELED:
                    raise CanceledException(self.id)
                else:
                    # means task has timeout
                    raise MyTimeoutException(self.id)

    def Cancel(self):
        if self.state != FINISHED and self.state != RUNNING:
            self.setState(CANCELED)
            return True
        else:
            return False

    def setState(self,state):
        self.state = state

    def setResult(self,result):
        with self.condition:
            self.result = result
            self.setState(FINISHED)
            self.condition.notify_all()
