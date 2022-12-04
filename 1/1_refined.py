def import_data():
    with open('advent2022/1/1.txt', 'r') as f:
        data = f.readlines()
    cal_list = []
    elf = 0
    c = 0
    while c < len(data):
        if len(data[c])!=1:
            elf += int(data[c])
            c+=1
        else:
            cal_list.append(elf)
            elf=0
            c+=1
    return cal_list


def sol1():
    cal_list = import_data()
    cal_list.sort()
    return cal_list[-1]

def sol2():
    cal_list = import_data()
    cal_list.sort()
    return sum(cal_list[-3:])

if __name__=="__main__":
    print(sol1()) #69206
    print(sol2()) #197400
