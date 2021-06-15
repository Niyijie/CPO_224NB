


class ProcessPoolExecutor(object):
    # workers default is 2
    def __init__(self,max_workers=2):
        self.max_workers = max_workers
