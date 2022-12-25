import gaus_jordan as g

def test_gaus_jordan():
    mat = [[1, 2, 3], [4, 6, 0], [1, 0, 6]]
    ras = [10, 5, 0]
    res = g.gaus(mat, ras)
    exp = [-10.0, 7.5, 1.6666666666666667]
    assert res == exp
    
def test_gaus_jordan2():
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [6, 4, 11, 11], [-3, -2, -2, -10]]
    ras = [-6, -10, -27, 1]
    res = g.gaus(mat, ras)
    exp = [0.5949367088607593, 1.8607594936708864, -3.5063291139240507, 0.05063291139240508]
    assert res == exp

def test_gaus_jordan3():
    mat = [[1, 2],[3, 4]]
    ras = [1, 2]
    res = g.gaus(mat, ras)
    exp = [0.0, 0.5]
    assert res == exp
