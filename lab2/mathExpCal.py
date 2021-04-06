"""
1. Mathematical expression
Sub variants deﬁne how you should implement interpretation:
(a) Parse input string in a tree (node - functions; leaf - constant) and reduce it in a result (from leaves to root)
(b) Find in input string simple expressions (‘a’, ‘1+2‘, ‘f(1)‘), and replate it by its result.
Input language is a sting like a + 2 - sin(-0.3)*(b - c).
Should support user-speciﬁc functions by passing something like {"foo": lambda x:
Run-time error should be processed correctly.
You should use the default Python logging module to make the interpreter work transparent.
Visualization as a dataﬂow graph (see Fig. 4.3) and as a dataﬂow graph with trace annotation (see listing 1).
 A speciﬁc graph representation depends on your sub-variant.
"""

from math import *

op_priority = {'+': 2, '-': 2, '*': 4, '/': 4, '(': 1}
operators = ['+', '-', '*', '/', '(', ')', ',']

one_para_func = ["sin","cos","tan"]
mul_para_func = ['+', '-', '*', '/', 'log', 'pow']

class MathExpCal(object):
    def __init__(self, exp_str):
        self.exp_str = exp_str
        self.symList = []
        self.val_dic = dict()

    """convert string to expression"""
    def parseStr_to_exp(self):
        if self.exp_str is None or self.exp_str == '':
            return None
        # handle error input
        exp_str = self.exp_str.replace(' ', '')
        ope_stack = list()
        i = -1
        while i < len(exp_str)-1:
            i = i + 1
            # get each character in str
            ch = exp_str[i]

            # sin cos ... or other operator
            val_str = ''
            flag2 = 0
            while (ch >= 'a') and (ch <= 'z'):
                val_str += ch   # compose a complete cal symbol
                if i + 1 <= len(exp_str)-1 and\
                        (exp_str[i+1] >= 'a') and\
                        (exp_str[i+1] <= 'z'):
                    i = i + 1
                    ch = exp_str[i]
                    continue
                else:
                    if len(val_str) == 1:
                        self.symList.append(val_str)
                    else:
                        ope_stack.append(val_str)
                    flag2 = 1
                    break
            if flag2 == 1:
                continue

            # get number
            flag1 = 0
            while (ch >= '0') and (ch <= '9') or ch == '.':
                val_str += ch   # compose a complete cal symbol
                if i + 1 <= len(exp_str)-1 and\
                        (((exp_str[i+1] >= '0') and
                          (exp_str[i+1] <= '9')) or exp_str[i+1] == '.'):
                    i = i + 1
                    ch = exp_str[i]
                    continue
                else:
                    self.symList.append(val_str)
                    flag1 = 1
                    break
            if flag1 == 1:
                continue

            # pass , symbol
            if ch == ',':
                continue

            if ch == '(':
                ope_stack.append(ch)
                continue

            if len(ope_stack) == 0:
                ope_stack.append(ch)
                continue
            # if meet ) cal the value until meet (
            if ch == ')':
                while ope_stack[-1] != '(':
                    self.symList.append(ope_stack.pop())
                ope_stack.pop()
                if len(ope_stack) and (ope_stack[-1] not in operators):
                    self.symList.append(ope_stack.pop())
                continue

            while len(ope_stack) and op_priority[ope_stack[-1]] >= op_priority[ch]:
                self.symList.append(ope_stack.pop())
            ope_stack.append(ch)

        while len(ope_stack):
            self.symList.append(ope_stack.pop())

    def calculate(self, **kwargs):
        cal_stack = list()
        self.val_dic = kwargs
        for op in self.symList:
            if op in one_para_func:
                if op == 'sin':
                    cal_stack.append(sin(cal_stack.pop()))
                elif op == 'cos':
                    cal_stack.append(cos(cal_stack.pop()))
                elif op == 'tan':
                    cal_stack.append(tan(cal_stack.pop()))
            elif op in mul_para_func:
                r_value = cal_stack.pop()
                l_value = cal_stack.pop()
                if op == '+':
                    cal_stack.append(l_value + r_value)
                elif op == '-':
                    cal_stack.append(l_value - r_value)
                elif op == '*':
                    cal_stack.append(l_value * r_value)
                elif op == '/':
                    cal_stack.append(l_value / r_value)
                elif op == 'log':
                    cal_stack.append(log(l_value, r_value))
                elif op == 'pow':
                    cal_stack.append(pow(l_value, r_value))
            elif op not in self.val_dic.keys():
                cal_stack.append(float(op))
            elif len(op) == 1:
                cal_stack.append(self.val_dic[op])
            else:
                # if is func
                func = self.val_dic[op]
                args_nums = func.__code__.co_argcount

                dic = dict()
                for j in range(args_nums):
                    dic[j] = cal_stack.pop()
                v = func(*dic.values())
                cal_stack.append(v)
        return cal_stack.pop()