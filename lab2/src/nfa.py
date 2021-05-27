from lab2.src.CONSTANT import *
from lab2.src.state import *

class NFA(object):
    def __init__(self, start:State, end:State):
        self.start = start
        self.end = end

    def repeatStar(self):
        # 建立重复多次分支
        self.repeatPlus()
        # 重复0次，直接指向end
        self.addSToE()

    # 重复0次  从start节点指向end节点
    def addSToE(self):
        self.start.addPath(EPSILON,self.end)

    # 重复1-n次
    def repeatPlus(self):
        # 创建新的起始和结束节点
        newStart = State()
        newEnd = State()
        newStart.addPath(EPSILON,self.start)
        self.end.addPath(EPSILON,newEnd)
        # 重新指向start
        self.end.addPath(EPSILON,self.start)
        # 改变引用使其成为新的图
        self.start = newStart
        self.end = newEnd

    def addSeriesGraph(self,nfaGraph):
        self.end.addPath(EPSILON,nfaGraph.start)
        self.end = nfaGraph.end

    def addParallelGraph(self,edge):
        mid = State()
        self.start.addPath(edge,mid)

    # @args_0
    # def visualize(self):
    #     res = []
    #     res.append("digraph G {")
    #     res.append(" rankdir=LR;")
    #     for v in self.inputs:
    #         res.append(" {}[shape=rarrow];".format(v))
    #     for v in self.outputs:
    #         res.append(" {}[shape=rarrow];".format(v))
    #     for i, n in enumerate(self.nodes):
    #         res.append(' n_{}[label="{}"];'.format(i, n.name))
    #     for i, n in enumerate(self.nodes):
    #         for v in n.inputs:
    #             if v in self.inputs:
    #                 res.append(' {} -> n_{};'.format(v, i))
    #         for j, n2 in enumerate(self.nodes):
    #             if i == j: continue
    #             for v in n.inputs:
    #                 if v in n2.outputs:
    #                     res.append(' n_{} -> n_{}[label="{}"];'.format(j, i, v))
    #         for v in n.outputs:
    #             if v in self.outputs:
    #                 res.append(' n_{} -> {};'.format(i, v))
    #     res.append("}")
    #     return "\n".join(res)