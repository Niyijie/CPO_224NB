from state import *
from regex import *

if __name__ == '__main__':
    regex = regex('a+')
    regex.compile()
    ret = regex.isMatch('aa')
    print(ret)