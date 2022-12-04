def import_data():
    with open('advent2022/1/1.txt', 'r') as f:
        data = f.readlines()
    blist = []
    slist = []
    c = 0
    while c < len(data):
        if len(data[c])!=1:
            slist.append(int(data[c]))
            c+=1
        else:
            blist.append(slist)
            slist=[]
            c+=1
    return blist

data = import_data()

portata_elfi = [sum(i) for i in data]
portata_elfi.sort(reverse=True)
A,B,C = portata_elfi[:3]
print(A)
print(A+B+C)