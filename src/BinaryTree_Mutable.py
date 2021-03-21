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

class TreeNode(object):
    def __init__(self, value=-1, lchild=None, rchild=None):
        # constructor
        self.lchild = lchild
        self.rchild = rchild
        self.value = value

    def get_value(self):
        # get value
        return self.value
