pos = 1.0e-10

def solo_matr(mat):
    mat1 = [[0 for i in range(len(mat))] for j in range(len(mat))]
    c = len(mat)
    for i in range(c):
        for j in range(c):
            mat1[j][j] = 1
    return mat1

def multiple_matr(m1, m2):
    res = [[0 for __ in range(len(m1[0]))] for __ in range(len(m2))]
    for i in range(len(m2)):
        for j in range(len(m1[0])):
            res[i][j] = sum(m2[i][x] * m1[x][j] for x in range(len(m1)))
    return res

def plus_mat(m1, m2):
    for i in range(len(m1)):
        m1[i].extend(m2[i])
    return m1


def reverse_mat(d, reverse, f):
    for i in range(len(d)):
        for j in range(len(d) , len(d[0])):
            reverse.append(d[i][j])
    res = [reverse[i:i + f] for i in range(0, len(reverse), f)]
    return res

def inverse_mat(m1, m2):
    inverse_mat = []
    pm = plus_mat(m1, m2)
    f = len(pm)
    for k in range(f):
        if abs(pm[k][k]) < pos:
            for i in range(k+1, f):
                if abs(pm[i][k]) > abs(pm[k][k]):
                    for j in range(k, 2*f):
                        pm[k][j], pm[i][j] = pm[i][j], pm[k][j]
                    break
        r_part = pm[k][k]
        if r_part == 0:
            return False
        else:
            for j in range(k, 2*f):
                pm[k][j] /= r_part
            for i in range(f):
                if i == k or pm[i][k] == 0:
                    continue
                factor = pm[i][k]
                for j in range(k, 2*f):
                    pm[i][j] -= factor * pm[k][j]
    res = reverse_mat(pm, inverse_mat, f)
    return res
