def values(mat):
    x = []
    y = []
    for i in range(len(mat)):
        x.append(mat[i][0])
        y.append(mat[i][1])
    return x, y


def koordin(kord):
    koord1 = kord[0]
    koord2 = kord[1]
    return koord1, koord2


def interp(x1, y1, x):
    x1, x2 = koordin(x1)
    y1, y2 = koordin(y1)
    y1 = y1 + ((x - x1) * (y2 - y1) / (x2 - x1))
    return y1

def piece_interp(x1, Y1, x):
    d = -1
    ss = []
    for i in x:
        for j in range(1, len(x1)):
            if i <= x1[j]:
                d = j-1
                break
            else:
                j += 1
        piece = (i - x1[d + 1]) * Y1[d] / ((x1[d] - x1[d + 1])) + (i - x1[d]) * Y1[d + 1] / ((x1[d + 1] - x1[d]))
        ss.append(piece)
    return ss

def polynom(x1, y1, x):
    pp = 0
    for i in range(len(x1)):
        p = 1
        for j in range(len(x1)):
            if j != i:
                p *= (x - x1[j]) / (x1[i] - x1[j])
        pp += y1[i] * p
    return pp
