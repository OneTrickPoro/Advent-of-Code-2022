from string import ascii_letters

def import_data1():
    with open('advent2022/3/3.txt', 'r') as f:
        data = f.readlines()
    data_ez = [i.strip() for i in data]
    res = [[b[:len(b)//2],b[len(b)//2:]] for b in data_ez]
    return res

data = import_data1()

def list_obj(data):
    items = [list(set(i[0]) & set(i[1]))[0] for i in data]
    return items

def val_obj(char):
    return ascii_letters.index(char)+1

def sol1():
    data = import_data1()
    items = list_obj(data)
    out = sum([val_obj(a) for a in items])
    return out

def import_data2():
    with open('advent2022/3/3.txt', 'r') as f:
        data = f.readlines()
    groups = [[data[i].strip(), data[i+1].strip(),data[i+2].strip()] for i in range(0,len(data),3)]
    return groups

def find_badge(groups):
    badges = [set(i[0]) & set(i[1]) & set(i[2]) for i in groups]
    badges = [list(i)[0] for i in badges]
    return badges

def sol2():
    groups = import_data2()
    badges = find_badge(groups)
    out = sum([val_obj(a) for a in badges])
    return out
        
print(sol1()) #7845
print(sol2()) #2790