import math

class KeyNotExistException(Exception):
    '''
        this is a exception for key not exist
    '''
    def __init__(self,key):
        self.key = key

    def __str__(self):
        print("key:" + str(self.key) + ",does not exist in the dict")

class DictNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.deleted = 0     # fake delete flag

class HashDict:
    '''
        init the dict (initial size is 100)
    '''
    def __init__(self):
        self.values = []    # store key
        self.size = 100   # init size of dict is 100
        for i in range(100):
            self.values.append(None)
        self.len = 0      # the num of stored values

def size(my_dict: HashDict):
    return my_dict.size

def length(my_dict: HashDict):
    return my_dict.len

def equare(dict1: HashDict, dict2: HashDict):
    d1 = to_dict(dict1)
    d2 = to_dict(dict2)
    if d1.__len__() != d2.__len__():
        return False
    else:
        for k,v in d1.items():
            if d2[k] != v:
                return False
        return True

def mempty(my_dict: HashDict):
    return None

'''
    if dict is full
'''
def dealFull(my_dict: HashDict):
    if my_dict.len == my_dict.size:
        # copy all node
        temp_lst = []
        for v in my_dict.values:
            if v.deleted == 0:  # pass the value which is deleted
                temp_lst.append(v)
        # resize the dict
        my_dict.size = math.floor(my_dict.size * 2)
        my_dict.values = []
        for i in range(my_dict.size):
            my_dict.values.append(None)
        # put the node to dict again
        my_dict.len = 0
        for v in temp_lst:
            put(my_dict,v.key,v.value)

'''
    calculate the pisition to store
'''
def getPosToSet(my_dict: HashDict,key):
    pos = hash(key) % my_dict.size
    return pos

'''
    put key-value to the dict
'''
def put(my_dict: HashDict,key,value):
    dealFull(my_dict) # resize the dict when it is full
    node = DictNode(key,value)
    pos = getPosToSet(my_dict,key)
    # if there is no collision
    if my_dict.values[pos] == None:
        my_dict.values[pos] = node
        my_dict.len = my_dict.len + 1
        return
    elif my_dict.values[pos].key == key:
        # update value
        my_dict.values[pos].value = value
        return
    else:
        # if there is collision
        # find pos+1 to size-1
        for i in range(pos+1,my_dict.size):
            if my_dict.values[i] == None:
                my_dict.values[i] = node
                my_dict.len = my_dict.len + 1
                return
            elif my_dict.values[i].key == key:
                my_dict.values[i].value = value
                return
        # find 0 to pos-1
        for i in range(pos):
            if my_dict.values[i] == None:
                my_dict.values[i] = node
                my_dict.len = my_dict.len + 1
                return
            elif my_dict.values[i].key == key:
                my_dict.values[i].value = value
                return

'''
    get value by key
'''
def get(my_dict: HashDict,key):
    pos = getPosToSet(my_dict,key)
    # if there is no collision
    if my_dict.values[pos] and my_dict.values[pos].key == key and my_dict.values[pos].deleted == 0:
        return my_dict.values[pos].value
    else:
        # if there is collision
        # find pos+1 to size-1
        for i in range(pos + 1, my_dict.size):
            if my_dict.values[i] is None:
                return None
            elif my_dict.values[i].key == key and my_dict.values[i].deleted == 0:
                return my_dict.values[i].value
        # find 0 to pos-1
        for i in range(pos):
            if my_dict.values[i] is None:
                return None
            elif my_dict.values[i].key == key and my_dict.values[i].deleted == 0:
                return my_dict.values[i].value
    # if not find return None
    return None

'''
     get key set
'''
def getKeySet(my_dict: HashDict):
    keySet = []
    for v in my_dict.values:
        if v and v.deleted == 0:
            keySet.append(v.key)


    return keySet

'''
    remove key
'''
def remove(my_dict: HashDict,key):
    value = get(my_dict,key)
    if value == None:
        raise KeyNotExistException(key)
    else:
        for n in my_dict.values:
            if n and n.key == key:
                n.deleted = 1
                my_dict.len = my_dict.len - 1
                return True
        raise KeyNotExistException(key)

'''
    construct dict from dict
'''
def from_dict(my_dict: HashDict, dict):
    for key, value in dict.items():
        put(my_dict,key, value)

def to_dict(my_dict: HashDict):
    dict = {}
    for v in my_dict.values:
        if v and v.deleted == 0:
            dict[v.key] = v.value

    return dict


'''
    construct dict from dict
'''
def from_list(my_dict: HashDict, lst):
    for k,v in enumerate(lst):
        put(my_dict,k, v)

'''
     convert dict to list
'''
def to_list(my_dict: HashDict):
    lst = []
    for v in my_dict.values:
        if v and v.deleted == 0:
            lst.append(v.value)
    return lst

'''
     is is_even=0 find not even else find even
'''
def find(my_dict: HashDict,is_even):
    is_even = is_even % 2
    eve_lst = []
    lst = to_list(my_dict)
    for i in lst:
        if type(i) == int and i % 2 == is_even:
            eve_lst.append(i)
    return eve_lst

'''
    filter element
'''
def filter(my_dict: HashDict,is_even):
    is_even = is_even % 2
    dict = {}
    for v in my_dict.values:
        if v and v.deleted == 0 and v.value % 2 == is_even:
            dict[v.key] = v.value

    return dict

'''
    map dict with f
'''
def map(my_dict: HashDict, f):
    dict = {}
    for v in my_dict.values:
        if v and v.deleted == 0:
            if v.value:
                dict[v.key] = f(get(my_dict,v.key))
            else:
                dict[v.key] = get(my_dict, v.key)
    return dict

'''
    Reduce the mapSet to one value.
'''
def reduce(my_dict: HashDict, f, initial):
    result = initial
    for v in my_dict.values:
        if v and v.deleted == 0:
            result = f(result, get(my_dict,v.key))
    return result

'''
    concat 2 dict,dict2 to dict1
'''
def mconcat(dict1: HashDict, dict2: HashDict):
    if dict1 is None:
        return dict2
    if dict2 is None:
        return dict1
    for v in dict2.values:
        if v and v.deleted == 0:
            value = get(dict2,v.key)
            put(dict1,v.key, value)
    return dict1

def iterator(dict: HashDict):
    if dict is not None:
        res = []
        list = to_list(dict)
        for i in list:
            res.append(i)
        a = iter(res)
    else:
        a = None

    def get_next():
        if a is None:
            raise StopIteration
        else:
            return next(a)
    return get_next

