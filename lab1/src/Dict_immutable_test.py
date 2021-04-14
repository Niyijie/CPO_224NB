import unittest
from hypothesis import given
import hypothesis.strategies as st

from Dict_immutable import *
from lab1.src.Dict_immutable import __len__


class TestIMmutable(unittest.TestCase):

    def test_put(self):
        dict = HashDict()
        put(dict,1, 2)
        self.assertEqual(get(dict,1), 2)
        put(dict,"1", 3)
        self.assertEqual(get(dict,"1"), 3)
        # put none
        put(dict,None, 1)
        self.assertEqual(get(dict,None), 1)

    def test_remove(self):
        dict = HashDict()
        put(dict,"1",3)
        put(dict,1,2)
        self.assertEqual(to_dict(dict), {"1":3,1:2})
        remove(dict,"1")
        self.assertEqual(get(dict,"1"), None)
        self.assertEqual(to_dict(dict), {1:2})

    def test_from_dict(self):
        dict = HashDict()
        from_dict(dict,{1: 1, 2: 2, 3: 3})
        self.assertEqual(to_dict(dict), {1: 1, 2: 2, 3: 3})

    def test_to_dict(self):
        dict = HashDict()
        put(dict,1, 2)
        put(dict,"2", 3)
        put(dict,None, 2)
        put(dict,None, 5) # replace the old one
        to_dict(dict)
        self.assertEqual(to_dict(dict), {1: 2, "2": 3, None: 5})

    def test_from_list(self):
        dict = HashDict()
        from_list(dict,[1,2,3,4])
        self.assertEqual(to_list(dict), [1,2,3,4])

    def test_to_list(self):
        dict1 = HashDict()
        dict2 = {1: 1, 2: 2, 3: 5, 4: 4}
        from_dict(dict1,dict2)
        self.assertEqual(to_list(dict1), [1, 2, 5, 4])

    def test_len(self):
        dict = HashDict()
        self.assertEqual(__len__(dict), 0)
        put(dict,1, 2)
        self.assertEqual(__len__(dict), 1)
        put(dict,2, 3)
        self.assertEqual(__len__(dict), 2)
        # if the key is same it will replace the old one
        put(dict,2, 5)
        self.assertEqual(__len__(dict), 2)
        remove(dict,1)
        self.assertEqual(__len__(dict), 1)

    def test_find(self):
        # find not even
        dict = HashDict()
        from_dict(dict,{1: 1, 2: 2, 3: 3, 4: 4, 5: 5})
        self.assertEqual(find(dict,0), [2,4])
        # find even
        self.assertEqual(find(dict,1), [1,3,5])

    def test_map(self):
        dict1 = {1: 123, 5: 321,3:None}
        dict2 = {1: '123', 5: '321',3:None}
        dict = HashDict()
        from_dict(dict,dict1)
        self.assertEqual(map(dict,str), dict2)

    def test_reduce(self):
        dict = HashDict()
        self.assertEqual(reduce(dict,lambda st, e: st + e, 0), 0)
        dict1 = {1: 100, 2: 200}
        dict2 = HashDict()
        from_dict(dict2,dict1)
        self.assertEqual(reduce(dict2,lambda st, e: st + e, 0), 300)

    def test_iter(self):
        lst = [1, 2, 3, 4, 5]
        dict = HashDict()
        from_list(dict, lst)
        tmp = []
        try:
            get_next = iterator(dict)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(lst, tmp)
        self.assertEqual(to_list(dict), tmp)

        get_next = iterator(None)
        self.assertRaises(StopIteration, lambda: get_next())


    @given(a=st.lists(st.integers()))
    def test_identity(self, a):
        dict = HashDict()
        dict_a = HashDict()
        from_list(dict_a,a)
        # ea = ae = a (e is empty)
        self.assertEqual(mconcat(mempty(dict),dict_a),dict_a)
        self.assertEqual(mconcat(dict_a,mempty(dict)),dict_a)

    @given(a=st.lists(st.integers()), b=st.lists(st.integers()), c=st.lists(st.integers()))
    def test_associativity(self, a, b, c):
        dict = HashDict()
        dict_a = HashDict()
        dict_b = HashDict()
        dict_c = HashDict()
        # init dict
        from_list(dict_a,a)
        from_list(dict_b,b)
        from_list(dict_c,c)
        # (a+b)+c
        a_b = mconcat(dict_a, dict_b)
        ab_c = mconcat(a_b, dict_c)
        # a+(b+c)
        b_c = mconcat(dict_b, dict_c)
        a_bc = mconcat(dict_a, b_c)
        self.assertEqual(to_dict(ab_c), to_dict(a_bc))

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        dict = HashDict()
        from_list(dict,a)
        b = to_list(dict)
        self.assertEqual(a, b)

    @given(st.lists(st.integers()))
    def test_python_len_and_dict_len_equality(self, a):
        dict = HashDict()
        from_list(dict,a)
        self.assertEqual(__len__(dict), len(a))

if __name__ == '__main__':
    unittest.main()
