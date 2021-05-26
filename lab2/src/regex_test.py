import unittest
from hypothesis import given
import hypothesis.strategies as st

from lab2.src.regex import *


class TestMutable(unittest.TestCase):

    def test_star(self):
        regex = Regex()
        # test match
        regex.compile('a*')
        self.assertEqual(regex.match('aaaaa'), (0,4))
        regex.compile('a*bbbc')
        self.assertEqual(regex.match('aaaaabbbc'), (0,8))
        regex.compile('a*bbbc')
        self.assertEqual(regex.match('bbbc'), (0,3))
        regex.compile('a*bbbc')
        self.assertEqual(regex.match('cbbbc'), None)
        # test search
        regex.compile('a*')
        self.assertEqual(regex.search('baaa'), (1,3))
        regex.compile('a*bbbc')
        self.assertEqual(regex.search('aaaaabbbc'), (0,8))
        regex.compile('a*bbbc')
        self.assertEqual(regex.search('xxxbbbc'), (3,6))

    def test_plus(self):
        regex = Regex()
        # test match
        regex.compile('a+')
        self.assertEqual(regex.match('aaaaa'), (0,4))
        regex.compile('a+')
        self.assertEqual(regex.match('sadw'), None)
        regex.compile('a+bbb')
        self.assertEqual(regex.match('aaabbb'), (0,5))
        # test search
        regex.compile('a+bbb')
        self.assertEqual(regex.search('aaabbb'), (0,5))
        regex.compile('a+bb')
        self.assertEqual(regex.search('xxxaaabb'), (3,7))


    def test_dot(self):
        regex = Regex()
        # test match
        regex.compile('a.')
        self.assertEqual(regex.match('aa'), (0,1))
        regex.compile('a...cef')
        self.assertEqual(regex.match('a123cef'), (0,6))
        regex.compile('a...cef')
        self.assertEqual(regex.match('x123cef'), None)
        # test search
        regex.compile('a.')
        self.assertEqual(regex.search('xxaa'), (2,3))
        regex.compile('a..xx.')
        self.assertEqual(regex.search('xxaa8xx9'), (2,7))
        regex.compile('a..xx.')
        self.assertEqual(regex.search('xxaa87x9'), None)

    def test_digital(self):
        regex = Regex()
        # test match
        regex.compile('\\d\\d')
        self.assertEqual(regex.match('22'), (0,1))
        regex.compile('a\\de')
        self.assertEqual(regex.match('a8e'), (0,2))
        # test search
        regex.compile('a\\de')
        self.assertEqual(regex.search('xxa8e'), (2,4))
        regex.compile('\\d')
        self.assertEqual(regex.search('xxa8e'), (3,3))

    def test_space(self):
        regex = Regex()
        # test match
        regex.compile('abc\\s\\s')
        self.assertEqual(regex.match('abc  '), (0,4))
        regex.compile('\\sefc')
        self.assertEqual(regex.match(' efc'), (0,3))
        regex.compile('\\sefc')
        self.assertEqual(regex.match('efc'), None)
        # test search
        regex.compile('\\sefc')
        self.assertEqual(regex.search('efc'), None)
        regex.compile('\\sefc')
        self.assertEqual(regex.search('abcd efc'), (4,7))


    def test_character(self):
        regex = Regex()
        # test match
        regex.compile('\\w\\wb')
        self.assertEqual(regex.match('1ab'), (0,2))
        regex.compile('\\w\\wb')
        self.assertEqual(regex.match('1ac'), None)
        # test search
        regex.compile('\\w\\wb')
        self.assertEqual(regex.search('1ab'), (0,2))
        regex.compile('\\w\\wb')
        self.assertEqual(regex.search('xx1ab'), (2,4))

    def test_diagonal(self):
        regex = Regex()
        # test match
        regex.compile('\\n')
        self.assertEqual(regex.match('n'), (0,0))
        regex.compile('\\n')
        self.assertEqual(regex.match('x'), None)
        # test search
        regex.compile('\\o')
        self.assertEqual(regex.search('abcdeo'), (5,5))
        regex.compile('\\n')
        self.assertEqual(regex.search('abcde1234'), None)

    def test_hat(self):
        regex = Regex()
        # test match
        regex.compile('^abcd')
        self.assertEqual(regex.match('abcddd'), (0,3))
        regex.compile('^abcd')
        self.assertEqual(regex.match('xabcddd'), None)
        # test search
        regex.compile('^abcd')
        self.assertEqual(regex.search('abcddd'), (0,3))
        regex.compile('^abcd')
        self.assertEqual(regex.search('xxxabcddd'), None)

    def test_doller(self):
        regex = Regex()
        # test match
        regex.compile('abcd$')
        self.assertEqual(regex.match('abacdddabcd'), (7,10))
        regex.compile('abcd$')
        self.assertEqual(regex.match('abacdddabcdx'), None)
        # test search
        regex.compile('abcd$')
        self.assertEqual(regex.search('abacdddabcdx'), None)
        regex.compile('abcd$')
        self.assertEqual(regex.search('qweabacdddabcd'), (10,13))

    def test_rect(self):
        regex = Regex()
        # test match
        regex.compile('[abc]')
        self.assertEqual(regex.match('dhgeardhrty'), None)
        regex.compile('[abc]')
        self.assertEqual(regex.match('kbkk'), None)
        regex.compile('[abc]')
        self.assertEqual(regex.match('abccqweeryt'), (0,0))
        # test search
        regex.compile('[abc]')
        self.assertEqual(regex.search('xxxabccqweeryt'), (3,3))
        regex.compile('[anc]')
        self.assertEqual(regex.search('xxxqweeryt'), None)

    # test [^]
    def test_hatRect(self):
        regex = Regex()
        # text search
        regex.compile('[^abc]')
        self.assertEqual(regex.match('abc'), None)
        regex.compile('[^abc]')
        self.assertEqual(regex.match('kkk'), (0,0))
        regex.compile('[^abc]')
        self.assertEqual(regex.match('adwerx'), None)
        # text search
        regex.compile('[^abc]')
        self.assertEqual(regex.match('abc'), None)
        # text search
        regex.compile('[^abc]')
        self.assertEqual(regex.match('mabc'), (0,0))

    # # test {n}
    # def test_repeat_n(self):
    #     print(123)

if __name__ == '__main__':
    unittest.main()
