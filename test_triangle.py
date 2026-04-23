from triangle import Triangle, TriangleType


def test_equilateral():
    t = Triangle(7, 7, 7)
    assert t.type == TriangleType.EQUILATERAL


def test_isosceles_B_equals_C():
    t = Triangle(7, 5, 5)
    assert t.type == TriangleType.ISOSCELES


def test_isosceles_A_equals_C():
    t = Triangle(5, 7, 5)
    assert t.type == TriangleType.ISOSCELES


def test_isosceles_A_equals_B():
    t = Triangle(5, 5, 7)
    assert t.type == TriangleType.ISOSCELES


def test_non_isosceles_non_equilateral():
    t = Triangle(9, 7, 3)
    assert t.type != TriangleType.ISOSCELES


def test_scalene_1():
    t = Triangle(5, 7, 4)
    assert t.type == TriangleType.SCALENE


def test_scalene_2():
    t = Triangle(7, 5, 4)
    assert t.type == TriangleType.SCALENE


def test_scalene_3():
    t = Triangle(4, 5, 7)
    assert t.type == TriangleType.SCALENE


def test_invalid_A_greater_than_B_plus_C():
    t = Triangle(5, 2, 2)
    assert t.type == TriangleType.INVALID


def test_invalid_A_equals_B_plus_C():
    t = Triangle(5, 2, 3)
    assert t.type == TriangleType.INVALID


def test_invalid_B_greater_than_A_plus_C():
    t = Triangle(2, 5, 2)
    assert t.type == TriangleType.INVALID


def test_invalid_B_equals_A_plus_C():
    t = Triangle(3, 5, 2)
    assert t.type == TriangleType.INVALID


def test_invalid_C_greater_than_A_plus_B():
    t = Triangle(2, 2, 5)
    assert t.type == TriangleType.INVALID


def test_invalid_C_equals_A_plus_B():
    t = Triangle(2, 3, 5)
    assert t.type == TriangleType.INVALID


def test_retangle_hipotenuse_a():
    t = Triangle(5, 4, 3)
    assert t.type == TriangleType.RETANGLE

def test_retangle_hipotenuse_b():
    t = Triangle(4, 5, 3)
    assert t.type == TriangleType.RETANGLE

def test_retangle_hipotenuse_c():
    t = Triangle(3, 4, 5)
    assert t.type == TriangleType.RETANGLE

def test_retangle_negative():
    t = Triangle(-3, -4, -5)
    assert t.type == TriangleType.INVALID

def test_not_retangle():
    t = Triangle(5, 7, 4)
    assert t.type != TriangleType.RETANGLE

def test_invalid_all_zero():
    t = Triangle(0, 0, 0)
    assert t.type == TriangleType.INVALID

def test_invalid_zero_a():
    t = Triangle(0, 1, 1)
    assert t.type == TriangleType.INVALID

def test_invalid_zero_b():
    t = Triangle(1, 0, 1)
    assert t.type == TriangleType.INVALID

def test_invalid_zero_c():
    t = Triangle(1, 1, 0)
    assert t.type == TriangleType.INVALID

def test_invalid_negative_b():
    t = Triangle(2, -1, 4)
    assert t.type == TriangleType.INVALID

def test_invalid_negative_a():
    t = Triangle(-1, 2, 4)
    assert t.type == TriangleType.INVALID

def test_invalid_negative_c():
    t = Triangle(2, 4, -1)
    assert t.type == TriangleType.INVALID

def test_invalid_all_negative():
    t = Triangle(-1, -1, -1)
    assert t.type == TriangleType.INVALID