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
        self.cur = 0

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

