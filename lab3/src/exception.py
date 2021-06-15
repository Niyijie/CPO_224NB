class TimeoutException(Exception):
    '''
        this is a exception for timeout
    '''
    def __init__(self,key):
        self.key = key

    def __str__(self):
        print("task:" + str(self.key) + ",timeout!")


class CanceledException(Exception):
    '''
        this is a exception for timeout
    '''
    def __init__(self,key):
        self.key = key

    def __str__(self):
        print("task:" + str(self.key) + ",canceled!")

