import math

def ryad_macloren(m1, m2):
    res = 0
    for i in range(0, m2 + 1):
        res += (m1 ** i) / math.factorial(i)
    return res

def ryad_macloren_cos(m1, m2):
    res = 0
    for i in range(0, m2 + 1):
        res += (((-1)**i) / math.factorial(2*i)) * (m1 ** (2 * i))
    return res

def ryad_macloren_sin(m1, m2):
    res = 0
    for i in range(0, m2 + 1):
        res += (((-1) ** i) / math.factorial(2*i + 1)) * (m1 ** (2 * i + 1))
    return res

def ryad_macloren_arcsin(m1, m2):
    res = 0
    for i in range(0, m2 + 1):
        res += ((math.factorial(2*i)) / (4**i * (math.factorial(i)**2) * (2*i + 1))) * (m1 ** (2 * i + 1))
    return res

def ryad_macloren_arccos(m1, m2):
    res = (3.14 / 2) - (ryad_macloren_arcsin(m1, m2))
    return res
