import unittest
import time
from MyProcessPoolExecutor import *
from exception import *

def task(n, second):
    print("threadid: " + str(threading.current_thread()) + "running the task")
    time.sleep(second)
    return n ** 2

class TestFuture(unittest.TestCase):

    def test_IsDone(self):
        excutors = MyProcessPoolExecutor(4)
        # task 1 wait for 1 second
        f1 = excutors.submit(task, 2, 1) # f1 wait 1 second
        time.sleep(3)
        self.assertEqual(f1.IsDone(), True)
        # task2
        f2 = excutors.submit(task, 2, 3)  # f2 wait 3 seconds
        f3 = excutors.submit(task, 4, 10) # f3 wait 10 seconds
        self.assertEqual(f2.IsDone(), False)
        self.assertEqual(f3.IsDone(), False)
        time.sleep(5)
        # f2 need 3 seconds to finish task so there is True
        self.assertEqual(f2.IsDone(), True)
        # f3 need 10 seconds to finish task so there is False
        self.assertEqual(f3.IsDone(), False)

    def test_result(self):
        excutors = MyProcessPoolExecutor(4)
        # f1 can finish task
        f1 = excutors.submit(task,1,1)
        f1.Result()
        self.assertEqual(f1.result, 1)
        # f2
        f2 = excutors.submit(task,3,4) # need 4 seconds to finish task
        self.assertEqual(f2.result, None)
        f2.Result()
        self.assertEqual(f2.result, 9)

    def test_timeout(self):
        excutors = MyProcessPoolExecutor(4)
        # f1 can finish task
        f1 = excutors.submit(task,1,1)
        f1.Result()
        self.assertEqual(f1.result, 1)
        # f2 will raise timeoutError exception
        try:
            f2 = excutors.submit(task,3,4) # need 4 seconds to finish task
            f2.Result(1) # time out is 1 seconds
        except MyTimeoutException:
            print("f2 raise MyTimeoutException")
        # f3 will not raise exception
        f3 = excutors.submit(task, 4, 5)  # need 4 seconds to finish task
        f3.Result(10)  # time out is 10 seconds

    def test_IsProgress(self):
        excutors = MyProcessPoolExecutor(4)
        # f1
        f1 = excutors.submit(task,1,5)
        time.sleep(1)
        self.assertEqual(f1.IsProgress(), True)
        time.sleep(1)
        self.assertEqual(f1.IsProgress(), True)
        time.sleep(1)
        self.assertEqual(f1.IsProgress(), True)
        time.sleep(4)
        self.assertEqual(f1.IsProgress(), False)

    def test_Cancel(self):
        excutors = MyProcessPoolExecutor(4)
        # f1
        f1 = excutors.submit(task,1,5)
        with self.assertRaises(CanceledException):
            f1.Cancel()
            f1.Result()
        # f2
        f2 = excutors.submit(task,2,3)
        self.assertEqual(f2.Cancel(),True)
        # f3 if running cancel will failed
        f3 = excutors.submit(task,3,3)
        time.sleep(1)
        self.assertEqual(f3.Cancel(),False)
        # f4 if task finished cancel will failed
        f4 = excutors.submit(task,4,3)
        time.sleep(5)
        self.assertEqual(f4.Cancel(),False)

    def test_priority(self):
        excutors = MyProcessPoolExecutor(3)
        # f1
        f1 = excutors.submit(task,1,5,priority=1)
        f2 = excutors.submit(task,2,5,priority=3)
        time.sleep(1)
        f3 = excutors.submit(task,3,5,priority=2)
        f4 = excutors.submit(task,4,5,priority=4)
        time.sleep(1)
        '''
          this test we have 3 threads to deal 4 task
          f3 and f4 are at the same time submit
          but f4 priority is 4 and f3 priority is 2
          so f4 will be deal ahead of f3
        '''
        self.assertEqual(f4.IsProgress(),True)
        self.assertEqual(f3.IsProgress(),False)


if __name__ == '__main__':
    unittest.main()



