import unittest
from hypothesis import given
import hypothesis.strategies as st

from immutable import *

class TestImmutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(im_size(None),0)
        root0 = binary_tree_node(1)
        root1 = binary_tree_node(1,
                                binary_tree_node(2,binary_tree_node(3)),
                                binary_tree_node(4))
        self.assertEqual(im_size(root0),1)
        self.assertEqual(im_size(root1), 4)

    def test_pre2lst(self):
       # self.assertIsNone(preOrderTraverse(None))
        root = binary_tree_node(1,binary_tree_node(2),binary_tree_node(3))
        pre_lst = preOrderTraverse(root)
        self.assertEqual(pre_lst,[1,2,3])

    def test_reduce(self):
        root1 = binary_tree_node(1,
                                 binary_tree_node(2, binary_tree_node(3)),
                                 binary_tree_node(4))
        self.assertEqual(reduce(root1,reduce_fuc),10)

    def test_fliter(self):
        root1 = binary_tree_node(1,
                                 binary_tree_node(2, binary_tree_node(3)),
                                 binary_tree_node(4))
        self.assertEqual(fliter(root1,filter_func), [1,2,3,4])
    def test_finmax(self):
        root1 = binary_tree_node(1,
                                 binary_tree_node(2, binary_tree_node(3)),
                                 binary_tree_node(4))
        self.assertEqual(find_maxval(root1),4)

    def test_map(self):
        root1 = binary_tree_node(1,
                                 binary_tree_node(2, binary_tree_node(3)),
                                 binary_tree_node(4))
        self.assertEqual(map(root1,f),[2,4,6,8])

    def test_delete(self):
        root1 = binary_tree_node(1,
                                 binary_tree_node(2, binary_tree_node(3)),
                                 binary_tree_node(4))
        self.assertEqual(delete(root1,3),True)

    def test_mempty(self):
        self.assertEqual(mempty(),None)

    def test_mcomcat(self):
        root1 = binary_tree_node(1,
                                 binary_tree_node(2, binary_tree_node(3)),
                                 binary_tree_node(4))
        root2 = binary_tree_node(1,
                                 binary_tree_node(2, binary_tree_node(3)),
                                 binary_tree_node(4))
        root3=mconcat(root1,root2)
        self.assertEqual(preOrderTraverse(root3),[2,4,6,8])


    def test_add(self):
        root1 = binary_tree_node(1)
        add(root1,2)

        self.assertEqual(preOrderTraverse(root1),[1,2])
    def test_tolist(self):
        root1=binary_tree_node(1,
                                 binary_tree_node(2, binary_tree_node(3)),
                                 binary_tree_node(4))

        self.assertEqual(to_list(root1),[1,2,4,3])

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self,a):
        #a = [1, 2, 3, 4]
        b1=binary_tree_node()
        self.assertEqual(to_list(from_list(b1,a)), a)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self,lst):
        #lst = [1, 2, 3, 4]
        b1=binary_tree_node()
        a = from_list(b1,lst)

        self.assertEqual(mconcat(mempty(), a), a)
        self.assertEqual(mconcat(a, mempty()), a)
    @given(a=st.lists(st.integers()),b=st.lists(st.integers()),c=st.lists(st.integers()))
    def test_monoid_associativity(self,a,b,c):
        a1 = binary_tree_node()
        b1 = binary_tree_node()
        c1 = binary_tree_node()
        #(a+b)+c
        a12=from_list(a1,a)
        b12=from_list(b1,b)
        c12=from_list(c1,c)
        x1=mconcat(mconcat(a12,b12),c12)
        #a+(b+c)
        x2=mconcat(a12,mconcat(b12,c12))
        self.assertEqual(x1,x2)

    def test_iterator(self):
        x = [1, 2, 3]
        root = binary_tree_node()
        root= from_list(root, x)
        tmp = []
        try:
            get_next = iterator(root)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(root), tmp)
        get_next = iterator(None)
        self.assertRaises(StopIteration, lambda: get_next())


if __name__ == '__main__':
 unittest.main()