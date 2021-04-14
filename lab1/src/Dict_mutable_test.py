import unittest
from hypothesis import given
import hypothesis.strategies as st

from Dict_mutable import *


class TestMutable(unittest.TestCase):

    def test_put(self):
        dict = HashDict()
        dict.put(2, 6)
        self.assertEqual(dict.get(2), 6)
        dict.put("3", 5)
        self.assertEqual(dict.get("3"), 5)
        # put none
        dict.put(None, 1)
        self.assertEqual(dict.get(None), 1)

    def test_remove(self):
        dict = HashDict()
        dict.put("1",3)
        dict.put("4",2)
        self.assertEqual(dict.to_dict(), {"1":3,"4":2})
        dict.remove("1")
        self.assertEqual(dict.get("1"), None)
        self.assertEqual(dict.to_dict(), {"4":2})

    def test_from_dict(self):
        dict = HashDict()
        dict.from_dict({1: 1, 2: 2, 3: 3})
        self.assertEqual(dict.to_dict(), {1: 1, 2: 2, 3: 3})

    def test_to_dict(self):
        dict = HashDict()
        dict.put(1, 2)
        dict.put("2", 3)
        dict.put(None, 2)
        dict.to_dict()
        self.assertEqual(dict.to_dict(), {1: 2, "2": 3, None: 2})

    def test_from_list(self):
        dict = HashDict()
        dict.from_list([1,2,3,4])
        self.assertEqual(dict.to_list(), [1,2,3,4])

    def test_to_list(self):
        dict1 = HashDict()
        dict2 = {1: 1, 2: 2, 3: 3, 4: 4}
        dict1.from_dict(dict2)
        self.assertEqual(dict1.to_list(), [1, 2, 3, 4])

    def test_len(self):
        dict = HashDict()
        self.assertEqual(dict.__len__(), 0)
        dict.put(1, 2)
        self.assertEqual(dict.__len__(), 1)
        dict.put(2, 3)
        self.assertEqual(dict.__len__(), 2)
        # if the key is same it will replace the old one
        dict.put(2, 5)
        self.assertEqual(dict.__len__(), 2)
        dict.remove(1)
        self.assertEqual(dict.__len__(), 1)

    def test_find(self):
        # find not even
        dict = HashDict()
        dict.from_dict({1: 1, 2: 2, 3: 4, 4: 6, 5: 9})
        self.assertEqual(dict.find(0), [2,4,6])
        # find even
        self.assertEqual(dict.find(1), [1,9])

    def test_map(self):
        dict1 = {1: 123, 5: 321}
        dict2 = {1: '123', 5: '321'}
        dict = HashDict()
        dict.from_dict(dict1)
        self.assertEqual(dict.map(str), dict2)

    def test_reduce(self):
        dict = HashDict()
        self.assertEqual(dict.reduce(lambda st, e: st + e, 0), 0)
        dict1 = {1: 100, 2: 200}
        dict2 = HashDict()
        dict2.from_dict(dict1)
        self.assertEqual(dict2.reduce(lambda st, e: st + e, 0), 300)

    def test_iter(self):
        dict = HashDict()
        dict.from_dict({1: 1, "2": 2, 3: 3, 4: 4})
        dict2 = {}
        for v in dict.values:
            if v and v.deleted == 0:
                dict2[v.key] = dict.get(v.key)
        self.assertEqual(dict.to_dict(), dict2)
        i = iter(HashDict())
        self.assertRaises(StopIteration, lambda: next(i))

    @given(a=st.lists(st.integers()))
    def test_identity(self, a):
        dict = HashDict()
        dict_a = HashDict()
        dict_a.from_list(a)
        # ea = ae = a (e is empty)
        self.assertEqual(dict.mconcat(dict.mempty(),dict_a),dict_a)
        self.assertEqual(dict.mconcat(dict_a,dict.mempty()),dict_a)

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_associativity(self, a, b, c):
        dict = HashDict()
        dict_a = HashDict()
        dict_b = HashDict()
        dict_c = HashDict()
        # init dict
        dict_a.from_list(a)
        dict_b.from_list(b)
        dict_c.from_list(c)
        # (a+b)+c
        a_b = dict.mconcat(dict_a, dict_b)
        ab_c = dict.mconcat(a_b, dict_c)
        # a+(b+c)
        b_c = dict.mconcat(dict_b, dict_c)
        a_bc = dict.mconcat(dict_a, b_c)
        self.assertEqual(ab_c.to_dict(), a_bc.to_dict())

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        dict = HashDict()
        dict.from_list(a)
        b = dict.to_list()
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_dict_len_equality(self, a):
        dict = HashDict()
        dict.from_list(a)
        self.assertEqual(dict.__len__(), len(a))

if __name__ == '__main__':
    unittest.main()
