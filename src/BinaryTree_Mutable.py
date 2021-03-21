"""
task -example

1. Add a new element (lst.add(3), cons(lst, 3))
2. Remove an element by value (lst.remove(3), remove(lst, 3))
3. Size (lst.size(), size(lst)), member, reverse (if applicable), intersection
4. Conversion from/to built-in list (you should avoid of usage these function into your library):
    – from (lst.from_list([12, 99, 37]), from_list([12, 99, 37]))
    – to (lst.to_list(), to_list(lst)).
5. Find element by speciﬁc predicate (lst.find(is_even), find(lst, is_even))
6. Filter data structure by speciﬁc predicate (lst.filter(is_even), filter(lst, is_even))
7. Map (link) structure by speciﬁc function (lst.map(increment), map(lst, increment))
8. Reduce (link)– process structure elements to build a return value by speciﬁc functions (lst.reduce(sum), reduce(lst, sum))
9. Data structure should be an iterator
    - for the mutable version in Python style
    - for the immutable version by closure
10. Data structure should be a monoid and implement mempty and mconcat.
    - Suppose that S is a set, and is some binary operation SSßS,
      then S with (mconcat) is a monoid if it satisﬁes the following two axioms:
    - Associativity For all a, b and c in S, the equation (ab)c = a(bc) holds.
    - Identity element There exists an element e (mempty) in S such that for every element a in S,
      the equations ea = ae = a hold.
"""
from queue import Queue

class TreeNode(object):
    def __init__(self, value=-1, lchild=None, rchild=None):
        # constructor
        self.lchild = lchild
        self.rchild = rchild
        self.value = value

    def get_value(self):
        # get value
        return self.value


class BinaryTree(object):
    def __init__(self, root=None):
        # constructor
        self.root = root
        self.level_queue = []
        self.cur_index = 0

    def insert_node_in_order(self, value):
        # add new node
        new_node = TreeNode(value)
        # if tree is empty
        if self.root is None:
            self.root = new_node
        else:
            # use queue to find the next position
            queue = Queue()
            queue.put(self.root)
            while not queue.empty():
                cur_node = queue.get()
                if cur_node.lchild is None:
                    cur_node.lchild = new_node
                    break
                elif cur_node.rchild is None:
                    cur_node.rchild = new_node
                    break
                else:
                    queue.put(cur_node.lchild)
                    queue.put(cur_node.rchild)

    def get_parent(self, value):
        # get node's parent node
        if self.root.value == value:
            return None
        queue = Queue()
        queue.put(self.root)
        # use queue to level traverse the tree and find the node equal the value
        while not queue.empty():
            # get the front node from queue
            cur_node = queue.get()
            # get left child
            lchild = cur_node.lchild
            if lchild:
                if lchild.value == value:
                    return cur_node
                else:
                    queue.put(cur_node.lchild)
            # get right child
            rchild = cur_node.rchild
            if rchild:
                if rchild.value == value:
                    return cur_node
                else:
                    queue.put(cur_node.rchild)
        return None

    def remove_node(self, value):
        # remove node whose .value is value
        # if root is null can not remove
        if not self.root:
            return False
        if self.root.value == value:
            self.root = None
            return True
        # remove the value from list
        list = self.to_list_pre_order()
        list.remove(value)
        # reconstruct a tree
        self.root = None
        for i in list:
            self.insert_node_in_order(i)
        return self.root

    def pre_order(self,node,list):
        if node is None:
            return
        else:
            list.append(node.value)
            self.pre_order(node.lchild,list)
            self.pre_order(node.rchild,list)

    def in_order(self,node,list):
        if node is None:
            return
        else:
            self.in_order(node.lchild,list)
            list.append(node.value)
            self.in_order(node.rchild,list)

    def post_order(self,node,list):
        if node is None:
            return
        else:
            self.post_order(node.lchild,list)
            self.post_order(node.rchild,list)
            list.append(node.value)

    def to_list_pre_order(self):
        list = []
        self.pre_order(self.root,list)
        return list

    def to_list_in_order(self):
        list = []
        self.in_order(self.root,list)
        return list

    def to_list_post_order(self):
        list = []
        self.post_order(self.root,list)
        return list

    def to_list_level_order(self):
        #  get tree's level-order list
        if self.root is None:
            return []
        my_list = list()
        queue = Queue()
        queue.put(self.root)
        while not queue.empty():
            cur_node = queue.get()
            my_list.append(cur_node.value)
            if cur_node.lchild:
                queue.put(cur_node.lchild)
            if cur_node.rchild:
                queue.put(cur_node.rchild)
        return my_list

    def size(self):
        # get the node numbers of binary tree
        return len(self.to_list_in_order())

    def from_list(self, list):
        # use list make a binary tree
        for index in range(len(list)):
            self.insert_node_in_order(list[index])
        return self

    def find_pre_order(self, value):
        # get index of value in the pre-order
        list = self.to_list_pre_order()
        return list.index(value)

    def find_post_order(self, value):
        # get index of value in the post-order
        list = self.to_list_post_order()
        return list.index(value)

    def find_level_order(self, value):
        # get index of value in the level-order
        list = self.to_list_level_order()
        return list.index(value)

    def find_in_order(self, value):
        # get index of value in the in-order
        list = self.to_list_in_order()
        return list.index(value)

    def filter(self):
        # filter even value
        lst = self.to_list_pre_order()
        result = []
        for i in range(len(lst)):
            if lst[i] % 2:
                result.append(lst[i])
        return result

    def empty(self):
        return self.root

    def concat(self,tree1,tree2):
        # concat two trees
        if not tree1:
            return tree2
        if not tree2:
            return tree1

        root = TreeNode(tree1.value + tree2.value)
        root.lchild = self.concat(tree1.lchild, tree2.lchild)
        root.rchild = self.concat(tree1.rchild, tree2.rchild)
        return root

    def map(self, f):
        # change a value to other type
        if self.root is None:
            return None
        queue = Queue()
        queue.put(self.root)
        while not queue.empty():
            cur = queue.get()
            cur.value = f(cur.value)
            if cur.lchild is not None:
                queue.put(cur.lchild)
            if cur.rchild is not None:
                queue.put(cur.rchild)
        return self

    def reduce(self, fun):
        # return sum of the bt
        sum = 0
        lst = self.to_list_pre_order()
        for i in range(len(lst)):
            sum = fun(sum, lst[i])
        return sum

    def __eq__(self,tree):
        # whether two trees are the same
        if self.root is None and tree.root is None:
            return True
        # pre order list
        lpre1 = self.to_list_pre_order()
        lpre2 = tree.to_list_pre_order()
        # in order list
        lin1 = self.to_list_in_order()
        lin2 = tree.to_list_in_order()

        # pre order and in order can determine a tree
        for i in range(len(lpre1)):
            if lpre1[i] == lpre2[i] and lin1[i] == lin2[i]:
                continue
            else:
                return False
        return True

    def __iter__(self):
        # return iterator itself
        if self.root is None:
            self.cur_index = 0
            return self
        self.level_queue.append(self.root)
        self.cur_index += 1
        return self

    def __next__(self):
        # return next element or StopIteration
        if self.cur_index == 0:
            raise StopIteration
        if self.root.lchild is not None:
            self.level_queue.append(self.root.lchild)
        if self.root.rchild is not None:
            self.level_queue.append(self.root.rchild)
        tmp = self.level_queue[self.cur_index-1].value
        if self.cur_index < len(self.level_queue):
            self.root = self.level_queue[self.cur_index]
            self.cur_index += 1
        else:
            self.root = self.level_queue[0]
            self.cur_index = 0
        return tmp

if __name__ == '__main__':
    x = [1, 2, 3]
    bt = BinaryTree()
    bt = bt.from_list(x)
    tree = BinaryTree(TreeNode(2, lchild=TreeNode(3, rchild=TreeNode(5)),
                        rchild=TreeNode(4, lchild=TreeNode(6))))

    print(tree.to_list_in_order())
    print(tree.to_list_in_order2())
    #print(bt.to_list_post_order())




