def import_data1():
    data = []
    with open('advent2022/5/5_edit.txt', 'r') as f:
        data = f.readlines()
    mat, inst = data[:8], data[10:]
    mat = [i.split() for i in mat]
    mat = list(zip(*mat))[::-1]
    mat = list(zip(*mat))[::-1]
    mat = list(zip(*mat))[::-1]
    mat = [list(i) for i in mat]
    mat_nice = []
    for i in mat:
        i = [i[j] for j in range(len(i)) if i[j] != '[0]']
        mat_nice.append(i)
    inst = [i.split() for i in inst]
    inst = [[int(i[1]), int(i[3])-1, int(i[5])-1] for i in inst]
    return mat_nice, inst

stacks, insts = import_data1()

A = stacks[0]

def move1(stacks, inst):
    for _ in range(inst[0]):
        a = stacks[inst[1]].pop()
        stacks[inst[2]].append(a)
    return stacks

def sol1():
    stacks, insts = import_data1()
    for i in insts:
        move1(stacks,i)
    tops = [i[-1] for i in stacks]
    s = ''
    for i in tops:
        s+=i[1]
    return s

print('Sol1:')
print(sol1())

#######

def move2(stacks, inst):
    a = stacks[inst[1]][-inst[0]:]
    del stacks[inst[1]][-inst[0]:]
    stacks[inst[2]]+=a
    return stacks

def sol2():
    stacks, insts = import_data1()
    print(stacks)
    for i in insts:
        move2(stacks,i)
    print(stacks)
    tops = [i[-1] for i in stacks if len(i)!=0 ]
    s = ''
    for i in tops:
        s+=i[1]
    return s

print('Sol2:')
print(sol2())