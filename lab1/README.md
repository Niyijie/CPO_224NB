## CPO_lab1_binary_tree

1. title: Computational Process Organization Lab 1
2. group name : 224_NB
3. group member : Ni Yijie 202320064;Sun Qing 202320057
4. laboratory work number: 3
5. variant description: set based on binary-tree
6. synopsis
   
    a. add a new element (lst.add(3), cons(lst, 3), extend(lst, 3));
   
    b. remove an element (lst.remove(3), remove(lst, 3));
   
    c. size (lst.size(), size(lst));
   
    d. conversion from and to python lists (lst.to_list(), lst.from_list([12, 99, 37]), from_list([12, 99, 37]));
   
    e. find element by specific predicate (lst.find(is_even_), );
   
    f. filter data structure by specific predicate (lst.filter(is_even));
   
    g. map structure by specific function (lst.map(increment));
   
    h. reduce – process structure elements to build a return value by specific functions (lst.reduce(sum));
   
    i. data structure should be a monoid and implement mempty and mconcat functions or methods;
   
    j. iterator: for the mutable version in Python style ; for the immutable version by closure;
7. contribution summary for each member
    Ni Yijie : BinaryTree_Mutable
    Sun Qing : BinaryTree_Immutable
8. work demonstration
    8.1 we use pycharm to write code and test it
    8.2 we use github to control our code version
    8.3 we can run it in terminal like 
        ` python BinaryTree_Mutable_test.py  `
        ` python BinaryTree_Immutable_test.py`
   
9. Conclusion: design binary trees in mutable and immutable ways, 
   we realize the function of add new element,remove element,size 
   of the tree ,list and tree transform,filter,reduce and so on. 
   we get the difference between mutable and immutable variables.