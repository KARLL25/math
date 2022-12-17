def sum(mat1,mat2): #1 Сложение матриц
    res = []
    for i range(len(mat1)):
        r = (list(map(lambda x,y:x+y, mat1[i], mat2[i])))
        res.append(r)
        return res

def mine(mat1, mat2):#2 Вычитание матриц
    res = []
    for i in range(len(mat1)):
        l = (list(map(lambda x, y: x - y, mat1[i], mat2[i])))
        res.append(l)
    return res

def transpon(mas):#3 Транспонирование матриц
    return [list(i) for i in zip(*mas)]

def umn_skalar(mat1,s):#4 Умножение матриц на скаляр
    res = []
    for i range(len(mat1)):
        r = [n * s for n in mat1[i]]
        res.append(r)
    return res

def swap(mat1, d1, d2):#5 Перестановка строк матрицы местами
    mat1[d1], mat1[d2] = mat1[d2],mat1[d1]
    return mat1

def index(mass,d):#6 Получение строки по индексу: элементарная функция
    return mass[d]

def stroka_skalar(mat1,sk,d):#7 Умножение одной строки матрицы по заданному индексу на скаляр
    return [n * sk for n in mat1[d]]


