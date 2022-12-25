import ryad_macloren as rm


def test_ryad_macloren1():
    m1, m2 = 2, 0
    res = rm.ryad_macloren(m1, m2)
    exp = 1.0
    assert res == exp


def test_ryad_macloren2():
    x, n = 1, 2
    res = rm.ryad_macloren(x, n)
    exp = 2.5
    assert res == exp


def test_ryad_macloren3():
    m1, m2 = 1, 2
    res = rm.ryad_macloren(m1, m2)
    exp = 2.5
    assert res == exp


def test_ryad_macloren_cos():
    m1, m2 = 1.5, 3
    res = rm.ryad_macloren_cos(m1, m2)
    exp = 0.0701171875
    assert res == exp


def test_ryad_macloren_sin1():
    m1, m2 = 1, 3
    res = rm.ryad_macloren_sin(m1, m2)
    exp = 0.841468253968254
    assert res == exp


def test_ryad_macloren_sin2():
    m1, m2 = 1.5, 5
    res = rm.ryad_macloren_sin(m1, m2)
    exp = 0.9974949556821353
    assert res == exp


def test_ryad_macloren_arcsin1():
    m1, m2 = 1, 2
    res = rm.ryad_macloren_arcsin(m1, m2)
    exp = 1.2416666666666667
    assert res == exp


def test_ryad_macloren_arcsin2():
    m1, m2 = 1, 2
    res = rm.ryad_macloren_arcsin(m1, m2)
    exp = 1.2416666666666667
    assert res == exp


def test_ryad_macloren_arccos1():
    m1, m2 = 1, 3
    res = rm.ryad_macloren_arccos(m1, m2)
    exp = 0.28369047619047616
    assert res == exp


def test_ryad_macloren_arccos2():
    m1, m2 = 1, 3
    res = rm.ryad_macloren_arccos(m1, m2)
    exp = 0.28369047619047616
    assert res == exp
