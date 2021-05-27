'''
This file holds global variables and can generate globally unique IDs
'''

EPSILON = "Epsilon"
CHAR = "char";

ID = 0

def getId():
    global ID
    id = ID
    ID += 1
    return id

def resetID():
    global ID
    ID = 0