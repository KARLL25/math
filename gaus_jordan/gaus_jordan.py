sla = 1.0e-10

def gaus(a, b):
    m = len(b)
    for l in range(m):
        if abs(a[l][l]) < sla:
            for i in range(l+1, m):
                if abs(a[i][l]) > abs(a[l][l]):
                    for j in range(l,m):
                        a[l][j], a[i][j] = a[i][j], a[l][j]
                    b[l], b[i] = b[i], b[l]
                    break
        re = perm(a, l)
        if re == 0:
            return False
        else:
            for j in range(l,m):
                a[l][j] /= re
            b[l] /= re
            for i in range(m):
                if i == l or a[i][l] == 0:
                    continue
                fr = a[i][l]
                for j in range(l,m):
                    a[i][j] -= fr * a[l][j]
                b[i] -= fr * b[l]
    return b

def perm(r1, r2):
    res = r1[r2][r2]
    return res
