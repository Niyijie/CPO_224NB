import queue

from exception import *
from futures import *
from WorkItem import *

def runner(work_queue, priority=False):
    while True:
        work_item = work_queue.get(block=True)
        if work_item is not None:
            work_item.run()
            del work_item
            work_queue.task_done()
            continue


class MyProcessPoolExecutor(object):
    # workers default is 2
    def __init__(self,max_workers=2):
        # max_wokers must bigger than 0,if error input initial it 2
        if max_workers <=0:
            max_workers = 2
        self.max_workers = max_workers
        self.work_queue = queue.Queue()
        self.threadsSet = set()
        # create threads pool
        for i in range(max_workers):
            t = threading.Thread(target=runner, args=(self.work_queue,))
            t.daemon = True
            t.start()
            self.threadsSet.add(t)

    def submit(self,*args, **kwargs):
        if len(args) == 0:
            raise ArgsErrorException()
        if len(args) == 1:
            fn = args
            args = None
        if len(args) >= 2:
            fn, *args = args
        future = Future()
        item = WorkItem(future,fn,args,kwargs)
        self.work_queue.put(item)
        return future

