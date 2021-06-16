import os
import random
import threading
import time
from concurrent import futures
from concurrent.futures.process import ProcessPoolExecutor

from futures import *
from MyProcessPoolExecutor import *

def task(n):
    print("threadid: " + str(threading.current_thread()) + "running the task")
    time.sleep(random.randint(1,5))
    return n**2

if __name__ == '__main__':
    # executor = ProcessPoolExecutor(max_workers=3)  # 不填则默认为cpu的个数
    # futures = []
    # for i in range(11):
    #     future = executor.submit(task, i)  # submit()方法返回的是一个future实例，要得到结果需要用future.result()
    #     futures.append(future)
    # executor.shutdown(True)  # 类似用from multiprocessing import Pool实现进程池中的close及join一起的作用
    # print('+++>')
    # for future in futures:
    #     print(future.result())
    # condition = threading.Condition()
    # ret = condition.wait()
    # print(123)

    future = Future()
    excutors = MyProcessPoolExecutor(4)
    # for i in range(10):
        #excutors.submit(task,i)
    f1 = excutors.submit(task, 1)
    f2 = excutors.submit(task, 2)
    f3 = excutors.submit(task, 3)
    print(f1.Result())
    print(f2.Result())
    print(f3.Result())

    time.sleep(3)
    #
    # condition = threading.Condition()
    # ret = condition.wait()
    # print(123)





