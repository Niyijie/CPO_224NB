import unittest
from hypothesis import given
import hypothesis.strategies as st

from lab2.src.regex import *


class TestMutable(unittest.TestCase):

    def test_star(self):
        regex = Regex('a*')
        regex.compile()
        self.assertEqual(regex.isMatch('aaaaa'), True)

    def test_plus(self):
        regex = Regex('a+')
        regex.compile()
        self.assertEqual(regex.isMatch('aaaaa'), True)

    def test_dot(self):
        regex = Regex('a.')
        regex.compile()
        self.assertEqual(regex.isMatch('aa'), True)

    def test_digital(self):
        regex = Regex('\\d\\d')
        regex.compile()
        self.assertEqual(regex.isMatch('22'), True)

    def test_space(self):
        regex = Regex('abc\\s\\s')
        regex.compile()
        self.assertEqual(regex.isMatch('abc  '), True)


    def test_character(self):
        regex = Regex('\\w\\wb')
        regex.compile()
        self.assertEqual(regex.isMatch('1ab'), True)

    def test_line(self):
        regex = Regex('\\n')
        regex.compile()
        self.assertEqual(regex.isMatch('n'), True)

    def test_hat(self):
        regex = Regex('^abcd')
        regex.compile()
        self.assertEqual(regex.isMatch('abcddd'), True)

    def test_doller(self):
        regex = Regex('abcd$')
        regex.compile()
        self.assertEqual(regex.isMatch('abacdddabcd'), True)

    def test_rect(self):
        regex = Regex('[abc]')
        regex.compile()
        self.assertEqual(regex.isMatch('dhgeardhrty'), True)
        regex.compile()
        self.assertEqual(regex.isMatch('kbkk'), True)
        regex.compile()
        self.assertEqual(regex.isMatch('qweeryt'), False)




if __name__ == '__main__':
    unittest.main()
