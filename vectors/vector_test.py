import vector.vector as vec




def test_plus():
    v1 = [1, 2, 5]
    v2 = [4, 8, 1]
    exp = [5, 10, 6]
    res = vec.plus(v1,v2)
    assert res == exp


def test_min():
    v1 = [1, 2, 5]
    v2 = [4, 8, 1]
    exp = [-3, -6, 4]
    res = vec.min(v1, v2)
    assert res == exp

def test_umn_scalar():
    v1 = [1, 2, 3]
    s = 2
    exp = [2, 4, 6]
    res = vec.umn_scalar(v1,s)
    assert res == exp

def test_del_scalar():
    v1 = [1,2,3]
    s = 2
    exp = [0.5,1,1.5]
    res = vec.del_scalar(v1,s)
    assert res == exp

def test_multi_scalar():
    v1 = [2,3]
    v2 = [5,10]
    exp = 40
    res = vec.multi_scalar(v1,v2)
    assert res == exp

def test_lengt():
    v2 = [-3,5,9]
    res = vec.lengt(v2)
    exp = 10.723805294763608
    assert res == exp

def test_same():
    v1 = [-1,2,4]
    v2 = [-1,2,4]
    res = vec.same(v1,v2)
    assert res == True

def test_collin():
    v1 = [1,2,3]
    v2 = [3,6,9]
    exp = True
    res = vec.collin(v1,v2)
    assert res == exp

def test_ortog():
    v1 = [1,2]
    v2 = [2,-1]
    res = vec.ortog(v1,v2)
    assert res == True

def test_angle():
    v1 = [4,5,6]
    v2 = [1,2,3]
    res = vec.angle(v1,v2)
    exp = 0.2257261285527342
    assert res == exp
