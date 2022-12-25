EPS = 1.0e-10


def permissive(n1, n2):
    res = n1[n2][n2]
    return res

def transp(ms):
    return [list(i) for i in zip(*ms)]

def multiple_matr(n1, n2):
    res = [[0 for __ in range(len(n2[0]))] for __ in range(len(n1))]
    for i in range(len(n1)):
        for j in range(len(n2[0])):
            res[i][j] = sum(n1[i][x] * n2[x][j] for x in range(len(n2)))
    return res

def emen(lis, ras):
    t_lis = transp(lis)
    l = multiple_matr(t_lis, lis)
    r = multiple_matr(t_lis, ras)
    gr = rigs(r)
    return gaus(l, gr)

def rigs(mult_r):
    return [x for x, in mult_r]

def side(mat):
    lis = left(mat)
    ras = right(mat)
    return lis, ras

def right(mat):
    ras = []
    for i in range(len(mat)):
        ras.append([mat[i][1]])
    return ras

def left(mat):
    lis = []
    for i in range(len(mat)):
        lis.append([mat[i][0], 1])
    return lis

def polinom(ras, x1):
    Ax = []
    for i in range(len(x1)):
        A = []
        for j in range(len(ras)):
            A = [x1[i] ** j] + A
        Ax += [A]
    y = multiple_matr(Ax, ras)
    res = []
    for n in range(len(y)):
        res.append([x1[n], y[n][0]])
    return res


def aproximation(mat, othX):
    lis, ras = side(mat)
    slauV  = emen(lis, ras)
    res = []
    for x_value in othX:
        res.append([x_value, slauV[0] * x_value + slauV[1]])
    return res

def gaus(n1, n2):
    n = len(n2)
    for k in range(n):
        if abs(n1[k][k]) < EPS:
            for i in range(k+1, n):
                if abs(n1[i][k]) > abs(n1[k][k]):
                    for j in range(k,n):
                        n1[k][j], n1[i][j] = n1[i][j], n1[k][j]
                    n2[k], n2[i] = n2[i], n2[k]
                    break
        re = permissive(n1, k)
        if re == 0:
            return False
        else:
            for j in range(k,n):
                n1[k][j] /= re
            n2[k] /= re
            for i in range(n):
                if i == k or n1[i][k] == 0:
                    continue
                fr = n1[i][k]
                for j in range(k,n):
                    n1[i][j] -= fr * n1[k][j]
                n2[i] -= fr * n2[k]
    return n2
