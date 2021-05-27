EPSILON = "Epsilon"
CHAR = "char";
CHARSET = "charSet";

ID = 0

def getId():
    global ID
    id = ID
    ID += 1
    return id

def resetID():
    global ID
    ID = 0