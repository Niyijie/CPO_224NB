import unittest
from hypothesis import given
import hypothesis.strategies as st

from BinaryTree_Immutable import *

class TestImmutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(im_size(None),0)
        root0 = TreeNode(1,TreeNode(2))
        root1 = TreeNode(1,
                                TreeNode(2,TreeNode(3)),
                                TreeNode(4))
        self.assertEqual(im_size(root0), 2)
        self.assertEqual(im_size(root1), 4)

    def test_preOrder(self):
       # self.assertIsNone(preOrderTraverse(None))
        root = TreeNode(1,TreeNode(2),TreeNode(3))
        pre_list = preOrderTraverse(root)
        self.assertEqual(pre_list,[1,2,3])

    def test_reduce(self):
        root1 = TreeNode(1,
                                 TreeNode(2, TreeNode(3)),
                                 TreeNode(4,TreeNode(5)))
        self.assertEqual(reduce(root1,reduce_fuc),15)

    def test_filter(self):
        root = TreeNode(1,
                                 TreeNode(2, TreeNode(3)),
                                 TreeNode(4))
        self.assertEqual(filter(root), [1,3])

    def test_findmax(self):
        # root1 = TreeNode(1,
        #                          TreeNode(2, TreeNode(3)),
        #                          TreeNode(4))
        # self.assertEqual(find_maxval(root1),4)

        root1 = TreeNode(-10000000, TreeNode(-10000001))
        self.assertEqual(find_maxval(root1), -10000000)

    def test_map(self):
        root1 = TreeNode(1,
                                 TreeNode(2, TreeNode(3)),
                                 TreeNode(4))
        self.assertEqual(map(root1,lambda t: t + 1),[2,3,4,5])

    def test_remove(self):
        root = TreeNode(1,
                                 TreeNode(2, TreeNode(3)),
                                 TreeNode(4))
        self.assertEqual(remove(root,3),True)

    def test_mempty(self):
        self.assertEqual(mempty(),None)

    def test_mconcat(self):
        root1 = TreeNode(1,
                                 TreeNode(2, TreeNode(3)),
                                 TreeNode(4))
        root2 = TreeNode(1,
                                 TreeNode(2, TreeNode(3)),
                                 TreeNode(4))
        root3=mconcat(root1,root2)
        self.assertEqual(preOrderTraverse(root3),[2,4,6,8])
        root4 = TreeNode(1,
                                 TreeNode(2, TreeNode(3)),
                                 TreeNode(4,TreeNode(5)))
        root5=mconcat(root3,root4)

        self.assertEqual(preOrderTraverse(root5),[3,6,9,12,5])

    def test_add(self):
        root = TreeNode(1)
        add(root,2)
        add(root,3)
        self.assertEqual(preOrderTraverse(root),[1,2,3])

    def test_tolist(self):
        root = TreeNode(1,
                                 TreeNode(2, TreeNode(3)),
                                 TreeNode(4))

        self.assertEqual(to_preOrder_list(root),[1,2,3,4])

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self,a):
        # a = [1, 2, 3, 4]
        self.assertEqual(to_list_level_order(from_list(a)), a)

    @given(st.lists(st.integers()))
    def test_monoid_identity(self,lst):
        #lst = [1, 2, 3, 4]
        tree = from_list(lst)
        # check tree1 + tree2 = tree2 + tree1
        self.assertEqual(mconcat(mempty(), tree), tree)
        self.assertEqual(mconcat(tree, mempty()), tree)


    @given(la=st.lists(st.integers()),lb=st.lists(st.integers()),lc=st.lists(st.integers()))
    def test_monoid_associativity(self,la,lb,lc):
        # (tree1+tree2)+tree3
        temp_tree1 = from_list(la)
        temp_tree2 = from_list(lb)
        temp_tree3 = from_list(lc)
        x1=mconcat(mconcat(temp_tree1,temp_tree2),temp_tree3)
        # tree1+(tree2+tree3)
        x2=mconcat(temp_tree1,mconcat(temp_tree2,temp_tree3))
        self.assertEqual(x1,x2)

    def test_iterator(self):
        x = [1, 2, 3]
        root = from_list(x)
        tmp = []
        try:
            get_next = iterator(root)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_preOrder_list(root), tmp)
        get_next = iterator(None)
        self.assertRaises(StopIteration, lambda: get_next())


if __name__ == '__main__':
 unittest.main()