from queue import Queue

class binary_tree_node(object):
    def __init__(self,value=None,lchild=None,rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild

    def get_value(self):
        # return node.element
        return self.value

    def __eq__(self, tree):
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


def create_new_root(node):
    if node is None:
        return None
    new_root = binary_tree_node(node.value)
    new_root.lchild = create_new_root(node.lchild)
    new_root.rchild = create_new_root(node.rchild)
    return new_root

def im_size(node):
    if node is None:
        return 0
    return len(preOrderTraverse(node))

def add(root,value):
    # add new node
    new_node = binary_tree_node(value)
    # if tree is empty
    if root is None:
        root = new_node
    else:
        # use queue to find the next position
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            # if cur_node exists
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


def mempty():
    return None

def pre_order(node, list):
    if node is None:
        return []
    else:
        list.append(node.value)
        pre_order(node.lchild, list)
        pre_order(node.rchild, list)
        return list

def preOrderTraverse(root):
    if root is None:
        return []

    result = []
    result = pre_order(root,result)

    return result


def in_order(node, list):
    if node is None:
        return []
    else:
        in_order(node.lchild, list)
        list.append(node.value)
        in_order(node.rchild, list)
        return list

def inOrderTraverse(root):
    if root is None:
        return []
    result = []
    result = in_order(root,result)
    return result

def to_preOrder_list(root):
    return preOrderTraverse(root)

def from_list(root, lst):
    for index in range(len(lst)):
        add(root,lst[index])
    return root

def find_maxval(root):
    list = to_preOrder_list(root)
    maxV = -9999
    for v in list:
        if v > maxV:
            maxV = v
    return maxV


def reduce_fuc(s, a):
    if type(a) == int and type(s) == int:
        return s + a
    else:
        return s

# filter even value
def filter_func(lst):
    new_list = []
    for i in lst:
        if i % 2 == 1:
            new_list.append(i)
    return new_list


def map(node,f):
    listmap=preOrderTraverse(node)
    for i in range(len(listmap)):
        listmap[i] = f(listmap[i])
    return listmap

def fliter(node,func):
    listfl = preOrderTraverse(node)
    return func(listfl)

def reduce(node,reduce_fuc):
    listre=preOrderTraverse(node)
    sum=0

    for i in range(len(listre)):
        sum=reduce_fuc(sum,listre[i])
    return sum

def mconcat(node1,node2):
    if node1 is None:
        return node2
    if node2 is None:
        return node1
    if node1 is None and node2 is None:
        return None
    node1.value = node1.value + node2.value  # get current node
    node1.lchild = mconcat(node1.lchild, node2.lchild)
    node1.rchild = mconcat(node1.rchild, node2.rchild)
    return node1

def get_parent(root, value):
    # get node's parent node
    if root.value == value:
        return None
    queue = Queue()
    queue.put(root)
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

def delete(root, value):
    # if root is null can not remove
    if not root:
        return False
    if root.value == value:
        root = None
        return True
    # remove the value from list
    list = to_preOrder_list()
    list.remove(value)
    # reconstruct a tree
    root = None
    for i in list:
        add(root,i)
    return root


def iterator(root):
    cur = root
    node_queue = list()
    node_queue.append(cur)

    def foo():
        nonlocal cur
        if len(node_queue) == 0 or cur is None:
            raise StopIteration
            #return
        cur = node_queue.pop(0)
        if cur.lchild is not None:
            node_queue.append(cur.lchild)
        if cur.rchild is not None:
            node_queue.append(cur.rchild)
        tmp = cur.value
        return tmp
    return foo

