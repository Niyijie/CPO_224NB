## CPO_lab3

1. title: Computational Process Organization Lab 3
2. group name : 224_NB
3. group member : Ni Yijie 202320064;Sun Qing 202320057
4. laboratory work number: 4
5. Objectives:
Design and develop a Python library for manipulation over the computational process.
• Develop unit tests.
• Another goals depend on the laboratory work variant and may combine one or more of the following: lazy evaluation; 
   manual control over the computational process; control over the concurrent process; meta-speciﬁcation of the computational process;
   embedded domain-speciﬁc language; supervisors; low-level hardware modeling; aspect-oriented programming; metaprogramming; etc.
6. Futures with worker pool Developing concurrent applications is hard. 
   Today widely spread approach to do this is the future – a high-level interface for 
   asynchronously executing functions or methods. As an example, you can see concurrent.
   futures in the standard Python library. In this variant, you should implement your library 
   for the future. Requirements:
(a) All futures should be executed in a global worker pool.
(b) The execution strategy:
    • execute futures in a results request sequence (if results already requested);
    • execute futures in a submission sequence (if results are not requested yet).
(c) Futures should provide the following API:
   • IsDone() – return True if future evaluation is complete;
   • InProgress() – return True if future evaluated right now;
   • Result(timeout=None)
        – return the future execution result (if the future is done);
        – raise the exception (if the future is done and raise an exception);
        – block until the future is done (if the timeout is None and future is not done);
        – raise TimeoutError after timeout (if the timeout is not None and the future is not done).
   • Cancel() – cancel a future (if the future not executed).
(d) To prove correctness, you should use unit tests.
(e) To prove a concurrent execution and execution strategy, you should demonstrate it in examples. If you can check it by automatic unit tests – it will be preferred.
7. contribution summary for each member
    Ni Yijie completed the data structure design and code writing.
    Sun Qing completed data testing and documentation.
8. work demonstration
    8.1 we use pycharm to write code and test it
    8.2 we use github to control our code version
    8.3 we can run it in terminal
9. Conclusion: In this experiment, we practiced a thread pool.
   In the process of implementation, we referred to the Future library of Python and realized
   a simple library. Our library thread pool can do some simple work and can set priorities so
   that higher-priority tasks are executed first. In addition, for some abnormal cases our 
   library also has some processing, to ensure the stability of the program.
