def import_data1():
    with open('advent2022/6/6.txt') as f:
        data = f.readlines()
    return data

def check1(stringa):
    ignore = stringa[:4]
    c = 4
    while True:
        while len(ignore) != len(set(ignore)):
            if len(set(ignore))<4:
                ignore = ignore[1:]
                ignore += stringa[c]
                c += 1
        if stringa[c] not in ignore:
            return c

def check2(stringa):
    ignore = stringa[:14]
    c = 14
    while True:
        while len(ignore) != len(set(ignore)):
            if len(set(ignore))<14:
                ignore = ignore[1:]
                ignore += stringa[c]
                c += 1
        if stringa[c] not in ignore:
            return c
            

def redu_str(stringa):
    stringa = stringa[::-1]
    slave = stringa
    for i in set(slave):
        stringa = stringa[:stringa.index(i)] + stringa[stringa.index(i):].replace(i, '')
    return stringa[::-1]
    

def sol1():
   data =import_data1()[0]
   sol = check1(data)
   return sol

def sol2():
   data =import_data1()[0]
   sol = check2(data)
   return sol

print('Sol 1: ', sol1())
