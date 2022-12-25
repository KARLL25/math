import aproximation as pm

def test_emen():
    lis = [[1, 2], [3, 4], [5, 6]]
    ras = [[7],[8],[9]]
    res = pm.emen(lis, ras)
    exp = [-6.000000000000053, 6.500000000000042]
    assert res == exp

def test_aproximation1():
    mat = [[1, 2], [3, 4.5], [5, 6], [7, 8]]
    othX = [2]
    res = pm.aproximation(mat, othX)
    exp = [[2, 3.1750000000000007]]
    assert res == exp

def test_aproximation2():
    mat = [[1, 2], [3, 4], [4, 5], [6, 7]]
    othX = [1, 2, 3]
    res = pm.aproximation(mat, othX)
    exp =  [[1, 2.000000000000001], [2, 3.000000000000001], [3, 4.0]]
    assert res == exp

def test_polinom_aproximation2():
    ras = [[0.1], [0.2], [1.3]]
    othX =  [1, 2, 3]
    res = pm.polinom(ras, othX)
    exp = [[1, 1.6], [2, 2.1], [3, 2.8]]
    assert res == exp

def test_polinom_aproximation3():
    ras = [[0.2], [-3.1], [12.22], [-5.77]]
    othX =  [1, 2, 3]
    res = pm.polinom(ras, othX)
    exp = [[1, 3.5500000000000007], [2, 7.870000000000001], [3, 8.390000000000004]]
    assert res == exp
