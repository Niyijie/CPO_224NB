import unittest
from hypothesis import given
import hypothesis.strategies as st

from lab2.src.regex import *


class TestMutable(unittest.TestCase):

    def test_star(self):
        regex = Regex()
        regex.compile('a*')
        self.assertEqual(regex.isMatch('aaaaa'), True)
        regex.compile('a*bbbc')
        self.assertEqual(regex.isMatch('aaaaabbbc'), True)
        regex.compile('a*bbbc')
        self.assertEqual(regex.isMatch('bbbc'), True)
        regex.compile('a*bbbc')
        self.assertEqual(regex.isMatch('cbbbc'), False)

    def test_plus(self):
        regex = Regex()
        regex.compile('a+')
        self.assertEqual(regex.isMatch('aaaaa'), True)
        regex.compile('a+')
        self.assertEqual(regex.isMatch('sadw'), False)
        regex.compile('a+bbb')
        self.assertEqual(regex.isMatch('aaabbb'), True)

    def test_dot(self):
        regex = Regex()
        regex.compile('a.')
        self.assertEqual(regex.isMatch('aa'), True)
        regex.compile('a...cef')
        self.assertEqual(regex.isMatch('a123cef'), True)
        regex.compile('a...cef')
        self.assertEqual(regex.isMatch('x123cef'), False)

    def test_digital(self):
        regex = Regex()
        regex.compile('\\d\\d')
        self.assertEqual(regex.isMatch('22'), True)
        regex.compile('a\\de')
        self.assertEqual(regex.isMatch('a8e'), True)

    def test_space(self):
        regex = Regex()
        regex.compile('abc\\s\\s')
        self.assertEqual(regex.isMatch('abc  '), True)
        regex.compile('\\sefc')
        self.assertEqual(regex.isMatch(' efc'), True)
        regex.compile('\\sefc')
        self.assertEqual(regex.isMatch('efc'), False)


    def test_character(self):
        regex = Regex()
        regex.compile('\\w\\wb')
        self.assertEqual(regex.isMatch('1ab'), True)
        regex.compile('\\w\\wb')
        self.assertEqual(regex.isMatch('1ac'), False)

    def test_diagonal(self):
        regex = Regex()
        regex.compile('\\n')
        self.assertEqual(regex.isMatch('n'), True)
        regex.compile('\\n')
        self.assertEqual(regex.isMatch('x'), False)

    def test_hat(self):
        regex = Regex()
        regex.compile('^abcd')
        self.assertEqual(regex.isMatch('abcddd'), True)
        regex.compile('^abcd')
        self.assertEqual(regex.isMatch('xabcddd'), False)

    def test_doller(self):
        regex = Regex()
        regex.compile('abcd$')
        self.assertEqual(regex.isMatch('abacdddabcd'), True)
        regex.compile('abcd$')
        self.assertEqual(regex.isMatch('abacdddabcdx'), False)

    def test_rect(self):
        regex = Regex()
        regex.compile('[abc]')
        self.assertEqual(regex.isMatch('dhgeardhrty'), True)
        regex.compile('[abc]')
        self.assertEqual(regex.isMatch('kbkk'), True)
        regex.compile('[abc]')
        self.assertEqual(regex.isMatch('qweeryt'), False)

    # test [^]
    def test_hatRect(self):
        regex = Regex()
        regex.compile('[^abc]')
        self.assertEqual(regex.isMatch('abc'), False)
        regex.compile('[^abc]')
        self.assertEqual(regex.isMatch('kkk'), True)
        regex.compile('[^abc]')
        self.assertEqual(regex.isMatch('adwerx'), True)


if __name__ == '__main__':
    unittest.main()
