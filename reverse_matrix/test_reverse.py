import reverse as r

def test_reverse_matrix():
    matr = [[3,2],[1,4]]
    matr1 = r.solo_matr(matr)
    res = r.inverse_mat(matr, matr1)
    exp = [[0.39999999999999997, -0.19999999999999998],  [-0.09999999999999999, 0.3] ]
    assert res == exp

def test_reverse():
    matr = [[3,2],[1,4]]
    prt = [[6],[6]]
    unt = r.solo_matr(matr)
    inverse_matrix = r.inverse_mat(matr, unt)
    res = r.multiple_matr(prt, inverse_matrix)
    exp = [[1.2], [1.1999999999999997]]
    assert res == exp
