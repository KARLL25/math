import interp as np

def test_interp():
    mat =  [[1, 2], [3, 4]]
    x1, y1 = np.values(mat)
    x = 2
    res = np.interp(x1, y1, x)
    exp = 3.0
    assert res == exp

def test_piece_interp():
    mat = [[1, 2], [3, 4], [5, 6], [7, 8]]
    x1, y1 = np.values(mat)
    x = [1, 2, 3, 4, 5, 6]
    res = np.piece_interp(x1, y1, x)
    exp = [2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    assert res == exp

def test_polynom():
    mat = [[1, 2], [3, 4], [5, 6], [7, 8]]
    x1, y1 = np.values(mat)
    x = 3
    res = np.polynom(x1, y1, x)
    exp = 4
    assert res == exp
