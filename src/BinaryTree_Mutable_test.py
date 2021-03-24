import unittest

from hypothesis import given
import hypothesis.strategies as st

from BinaryTree_Mutable import *


class TestMutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(BinaryTree().size(), 0)
        self.assertEqual(BinaryTree(TreeNode(1,TreeNode(2))).size(), 2)
        self.assertEqual(BinaryTree().from_list([1, 2, 3,4]).size(), 4)

    def test_to_list_pre_order(self):
        self.assertEqual(BinaryTree().to_list_pre_order(), [])
        self.assertEqual(BinaryTree(TreeNode(1)).to_list_pre_order(), [1])
        self.assertEqual(BinaryTree(TreeNode(1, lchild=TreeNode(2, rchild=TreeNode(3)))).to_list_pre_order()
                         , [1, 2, 3])

    def test_to_list_in_order(self):
        self.assertEqual(BinaryTree().to_list_in_order(), [])
        self.assertEqual(BinaryTree(TreeNode(1)).to_list_in_order(), [1])
        self.assertEqual(BinaryTree(TreeNode(1, lchild=TreeNode(2, rchild=TreeNode(3)))).to_list_in_order()
                         , [2, 3, 1])

    def test_to_list_post_order(self):
        self.assertEqual(BinaryTree().to_list_post_order(), [])
        self.assertEqual(BinaryTree(TreeNode(1)).to_list_post_order(), [1])
        self.assertEqual(BinaryTree(TreeNode(1, lchild=TreeNode(2, rchild=TreeNode(3)))).to_list_post_order()
                         , [3, 2, 1])

    def test_to_list_level_order(self):
        self.assertEqual(BinaryTree().to_list_level_order(), [])
        self.assertEqual(BinaryTree(TreeNode(1, TreeNode(2))).to_list_level_order(), [1, 2])
        self.assertEqual(BinaryTree(TreeNode(1, lchild=TreeNode(2, lchild=TreeNode(4),rchild=TreeNode(5))
                                             ,rchild=TreeNode(3))).to_list_level_order()
                         , [1, 2, 3, 4, 5])

    def test_from_list(self):
        test_data = [
            [],
            [1],
            [1,2,3,]
        ]
        for e in test_data:
            tree = BinaryTree()
            tree.from_list(e)
            self.assertEqual(tree.to_list_level_order(), e)

    def test_insert_node_in_order(self):
        tree = BinaryTree()
        tree.insert_node_in_order(1)
        self.assertEqual(tree.to_list_pre_order(), [1])
        tree.insert_node_in_order(2)
        self.assertEqual(tree.to_list_pre_order(), [1, 2])
        tree.insert_node_in_order(3)
        self.assertEqual(tree.to_list_pre_order(), [1, 2, 3])

    def test_remove_node(self):
        bt = BinaryTree()
        for i in range(5):
            bt.insert_node_in_order(i)
        bt.remove_node(2)
        self.assertNotIn(5, bt.to_list_pre_order())

    def test_reduce(self):
        # sum of empty list
        tree = BinaryTree()
        self.assertEqual(tree.reduce(lambda st, e: st + e), 0)

        # sum of list
        tree = BinaryTree()
        tree.from_list([1, 2, 3])
        self.assertEqual(tree.reduce(lambda st, e: st + e), 6)

        # size
        test_data = [
            [],
            [1],
            [1, 2]
        ]
        for e in test_data:
            tree = BinaryTree()
            tree = tree.from_list(e)
            self.assertEqual(tree.reduce(lambda st, _: st + 1), tree.size())

    def test_map(self):
        tree = BinaryTree()
        self.assertIsNone(tree.map(str))

        tree = BinaryTree()
        tree = tree.from_list([1, 2, 3])
        tree.map(str)
        self.assertEqual(tree.to_list_level_order(), ["1", "2", "3"])

        tree = BinaryTree()
        tree.from_list([1, 2, 3])
        tree.map(lambda t: t + 1)
        self.assertEqual(tree.to_list_level_order(), [2, 3, 4])

    def test_filter(self):
        tree = BinaryTree()
        tree.insert_node_in_order(1)
        tree.insert_node_in_order(2)
        tree.insert_node_in_order(3)
        tree.insert_node_in_order(4)
        self.assertEqual(tree.filter(), [1, 3])

    def test_concat(self):
        tree1 = BinaryTree()
        tree1.insert_node_in_order(1)
        tree1.insert_node_in_order(2)
        tree2 = BinaryTree()
        tree2.insert_node_in_order(3)
        tree2.insert_node_in_order(4)
        b = BinaryTree()
        b = b.concat(tree1.root, tree2.root)
        self.assertEqual(BinaryTree(b).to_list_pre_order(), [4, 6])
        tree2.insert_node_in_order(5)
        b = BinaryTree()
        b = b.concat(tree1.root, tree2.root)
        self.assertEqual(BinaryTree(b).to_list_pre_order(), [4, 6, 5])

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, list):
        tree1 = BinaryTree()
        tree1 = tree1.from_list(list)
        tree2 = tree1.to_list_level_order()
        self.assertEqual(list, tree2)

    @given(st.lists(st.integers()))
    def test_python_len_and_tree_size_equality(self,list):
        tree = BinaryTree()
        tree = tree.from_list(list)
        self.assertEqual(tree.size(),len(list))

    @given(st.lists(st.integers()))
    def test_monoid_identity(self, list):
        # tree1 + tree2 == tree2 + tree1
        tree1 = BinaryTree().from_list(list)
        tree2 = BinaryTree()
        tree2.insert_node_in_order(1)
        tree2.insert_node_in_order(2)
        tree3 = BinaryTree()

        list1 = BinaryTree(tree3.concat(tree1.root, tree2.root)).to_list_level_order()
        list2 = BinaryTree(tree3.concat(tree2.root, tree1.root)).to_list_level_order()
        self.assertEqual(list1, list2)

    def test_iter(self):
        x = [1, 2, 3]
        bt = BinaryTree()
        bt = bt.from_list(x)
        tmp = []
        for e in bt:
            tmp.append(e)
        self.assertEqual(x, tmp)
        self.assertEqual(bt.to_list_level_order(), tmp)

        i = iter(BinaryTree())
        self.assertRaises(StopIteration, lambda: next(i))


if __name__ == '__main__':
    unittest.main()
