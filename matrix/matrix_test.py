import matrix as m

def test_sum(): #1
    mat1 = [[10, 11, 4], [8, 2, 1], [5, 6, 3]]
    mat2 = [[6, 4, 1], [5, 2, 3], [6, 4, 1]]
    res = m.sum(mat1, mat2)
    exp = [[16, 15, 5], [13, 4, 4], [11, 10, 4]]
    assert res == exp

def test_mine():#2
    mat1 = [[4, 3, 1], [8, 3, 4], [2, 3, 7]]
    mat2 = [[2, 3, 5], [1, 2, 5], [6, 1, 4]]
    res = m.mine(mat1, mat2)
    exp = [[2, 0, -4], [7, 1, -1], [-4, 2, 3]]
    assert res == exp

def test_transpon():#3
    mat1 = [[3,1,2],[5,3,2]]
    res = m.transpon(mat1)
    exp = [[3,5],[1,3],[2,2]]
    assert res == exp

def test_umn_skalar():
    mat1 = [[5, 3, 2], [5, 6, 6], [7, 5, 3]]
    s = 2
    res = m.umn_skalar(mat1, s)
    exp = [[10, 6, 4], [10, 12, 12], [14, 10, 6]]
    assert res == exp

def test_swap():
    mat1 = [[2, 1, 5], [1, 7, 2]]
    d1 = 0
    d2 = 1
    res = m.swap(mat1, d1, d2)
    exp = [[1, 7, 2], [2, 1, 5]]
    assert res == exp

def test_index():
    d = 1
    mat1 = [[2, 1, 5], [11, 12, 13], [4, 5, 1]]
    res = m.index(mat1, d)
    exp = [11, 12, 13]
    assert res == exp

def test_stroka_skalar():
    sk = 2
    d = 1
    mat1 = [[4, 3, 1], [10, 13, 12], [5, 2, 4]]
    res = m.stroka_skalar(mat1, sk, d)
    exp = [20, 26, 24]
    assert res == exp
