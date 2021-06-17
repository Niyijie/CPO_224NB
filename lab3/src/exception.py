class MyTimeoutException(Exception):
    '''
        this is a exception for timeout
    '''
    def __init__(self,id):
        self.id = id

    def __str__(self):
        print("task:" + str(self.id) + ",timeout!")


class CanceledException(Exception):
    '''
        this is a exception for timeout
    '''
    def __init__(self,id):
        self.id = id

    def __str__(self):
        print("task:" + str(self.id) + ",canceled!")

class ArgsErrorException(Exception):
    '''
        this is a exception for timeout
    '''
    def __init__(self):
        print("submit args must bigger than 0")


