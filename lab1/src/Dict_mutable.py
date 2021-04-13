import math

class DictNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.deleted = 0     # fake delete flag

class HashDict:
    '''
        init the dict (initial size is 10)
    '''
    def __init__(self):
        self.values = []    # store key
        self.size = 10   # init size of dict is 100
        for i in range(10):
            self.values.append(None)
        self.len = 0      # the num of stored values

    '''
        if dict is full
    '''
    def dealFull(self):
        if self.len == self.size:
            # copy all node
            temp_lst = []
            for v in self.values:
                if v.deleted == 0:  # pass the value which is deleted
                    temp_lst.append(v)
            # resize the dict
            self.size = math.floor(self.size * 2)
            self.values = []
            for i in range(self.size):
                self.values.append(None)
            # put the node to dict again
            self.len = 0
            for v in temp_lst:
                self.put(v.key,v.value)

    '''
        calculate the pisition to store
    '''
    def getPosToSet(self,key):
        pos = hash(key) % self.size
        return pos

    '''
        put key-value to the dict
    '''
    def put(self,key,value):
        self.dealFull() # resize the dict when it is full
        node = DictNode(key,value)
        pos = self.getPosToSet(key)
        # if there is no collision
        if self.values[pos] == None:
            self.values[pos] = node
            self.len = self.len + 1
            return
        elif self.values[pos].key == key:
            # update value
            self.values[pos].value = value
            return
        else:
            # if there is collision
            # find pos+1 to size-1
            for i in range(pos+1,self.size):
                if self.values[i] == None:
                    self.values[i] = node
                    self.len = self.len + 1
                    return
                elif self.values[i].key == key:
                    self.values[i].value = value
                    return
            # find 0 to pos-1
            for i in range(pos):
                if self.values[i] == None:
                    self.values[i] = node
                    self.len = self.len + 1
                    return
                elif self.values[i].key == key:
                    self.values[i].value = value
                    return

    '''
        get value by key
    '''
    def get(self,key):
        pos = self.getPosToSet(key)
        # if there is no collision
        if self.values[pos] and self.values[pos].key == key and self.values[pos].deleted == 0:
            return self.values[pos].value
        else:
            # if there is collision
            # find pos+1 to size-1
            for i in range(pos + 1, self.size):
                if self.values[i] is None:
                    return None
                elif self.values[i].key == key and self.values[i].deleted == 0:
                    return self.values[i].value
            # find 0 to pos-1
            for i in range(pos):
                if self.values[i] is None:
                    return None
                elif self.values[i].key == key and self.values[i].deleted == 0:
                    return self.values[i].value
        # if not find return None
        return None

    '''
        remove key
    '''
    def remove(self,key):
        value = self.get(key)
        if value == None:
            return False
        else:
            for n in self.values:
                if n and n.key == key:
                    n.deleted = 1
                    return True
        return False

    '''
        construct dict from dict
    '''
    def from_dict(self, dict):
        for key, value in dict.items():
            self.put(key, value)

    '''
         convert dict to list
    '''
    def to_list(self):
        lst = []
        for v in self.values:
            if v and v.deleted == 0:
                lst.append(v.value)
        return lst

if __name__ == '__main__':
    dict = HashDict()

    # dict.put(1,2)
    # dict.put(1,3)
    # dict.put(2,4)

    d = {"1":1,"2":2,"3":3}
    dict.from_dict(d)

    print(dict.to_list())




