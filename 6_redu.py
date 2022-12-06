def import_data1():
    with open('advent2022/6/6.txt') as f:
        data = f.readlines()
    return data[0]

def redu_str(stringa):
    stringa = stringa[::-1]
    cont = set(stringa)
    s = "".join(cont)
    for i in s:
        stringa = stringa[:stringa.index(i)]+ i + stringa[i.index(i)+1:].replace(i, "")
    return stringa[::-1]

print(redu_str('matematica'))