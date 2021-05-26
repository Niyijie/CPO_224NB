from state import *
from regex import *

import re

if __name__ == '__main__':
    # regex = regex('a*')
    # regex.compile()
    # ret = regex.isMatch('aaaaa')
    # print(ret)

    # regex = regex('a+')
    # regex.compile()
    # ret = regex.isMatch('aaaaa')
    # print(ret)

    # regex = regex('a.')
    # regex.compile()
    # ret = regex.isMatch('aa')
    # print(ret)

    # regex = regex('\\d\\d')
    # regex.compile()
    # ret = regex.isMatch('11')
    # print(ret)

    regex = regex('\\d\\d\\s')
    regex.compile()
    ret = regex.isMatch('11 ')
    print(ret)

    # print(re.match('[\\w]','1'))
    # print(re.search('[\\w]','1111'))
