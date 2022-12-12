import math as v

def plus(v1, v2): #1 сложение векторов
    return [x + y for x, y in zip(v1, v2)]

def min(v1, v2): #2 вычитание векторов. Model
    return [x - y for x, y in zip(v1, v2)]

def umn_scalar(v1,s):  # 3 умножение на скаляр
    return [i*s for i in v1]

def del_scalar(v1,s):  # 4 деление на скаляр
    return [i/s for i in v1]

def multi_scalar(v1,v2): # 5 скалярное произведение
    return sum([x*y for x, y in zip(v1,v2)])

def lengt(v2): # 6 длина вектора
    return v.sqrt(sum([v1**2 for v1 in v2]))

def same(v1,v2): # 7 равенство векторов
    if [x - y for x,y in zip(v1,v2)] == [0,0,0]:
        return True
    else:
        return False

def collin(v1,v2): # 8 коллинеарность векторов
    if v1[0] / v2[0] == v1[1] / v2[1] == v1[2] / v2[2]:
        return True
    else:
        return False

def ortog(v1,v2): # 9 ортогоналость векторов
    if sum([x*y for x,y in zip(v1,v2)]) == 0:
        return True
    else:
        return False

def angle(v1,v2): # 10 угол между векторами
    return v.acos(multi_scalar(v1, v2) / (lengt(v1) * lengt(v2)))





