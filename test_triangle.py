from triangle import Triangle, TriangleType


def test_equilateral():
    t = Triangle(7, 7, 7)
    assert t.type == TriangleType.EQUILATERAL

def test_isosceles():
    ti = Triangle(7, 5, 5) 
    t2 = Triangle(9, 7, 3)

    assert ti.type == TriangleType.ISOSCELES
    assert t2.type != TriangleType.ISOSCELES

def test_scalene():
    ti = Triangle(5, 7, 4) 

    assert ti.type == TriangleType.SCALENE

def test_invalid():
    t0 = Triangle(0,2,1)
    t1 = Triangle(1,2,4)

    assert t0.type == TriangleType.INVALID
    assert t1.type == TriangleType.INVALID