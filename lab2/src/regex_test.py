import unittest
from hypothesis import given
import hypothesis.strategies as st

from lab2.src.regex import *


class TestMutable(unittest.TestCase):

    def test_star(self):
        regex = Regex()
        regex.compile('a*')
        self.assertEqual(regex.isMatch('aaaaa'), True)

    def test_plus(self):
        regex = Regex()
        regex.compile('a+')
        self.assertEqual(regex.isMatch('aaaaa'), True)

    def test_dot(self):
        regex = Regex()
        regex.compile('a.')
        self.assertEqual(regex.isMatch('aa'), True)

    def test_digital(self):
        regex = Regex()
        regex.compile('\\d\\d')
        self.assertEqual(regex.isMatch('22'), True)

    def test_space(self):
        regex = Regex()
        regex.compile('abc\\s\\s')
        self.assertEqual(regex.isMatch('abc  '), True)


    def test_character(self):
        regex = Regex()
        regex.compile('\\w\\wb')
        self.assertEqual(regex.isMatch('1ab'), True)

    def test_line(self):
        regex = Regex()
        regex.compile('\\n')
        self.assertEqual(regex.isMatch('n'), True)

    def test_hat(self):
        regex = Regex()
        regex.compile('^abcd')
        self.assertEqual(regex.isMatch('abcddd'), True)

    def test_doller(self):
        regex = Regex()
        regex.compile('abcd$')
        self.assertEqual(regex.isMatch('abacdddabcd'), True)

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
