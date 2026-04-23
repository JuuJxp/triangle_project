from dataclasses import dataclass
from enum import Enum, auto


class TriangleType(Enum):
    EQUILATERAL = auto()
    ISOSCELES = auto()
    SCALENE = auto()
    RETANGLE = auto()
    INVALID = auto()


@dataclass(frozen=True, slots=True)
class Triangle:
    side1: int
    side2: int
    side3: int

    @property
    def type(self) -> TriangleType:
        a, b, c = self.side1, self.side2, self.side3

        if a <= 0 or b <= 0 or c <= 0:
            print(f"Invalid triangle: sides must be positive, but a={a}, b={b}, c={c}")
            return TriangleType.INVALID
        if a == b == c:
            print(f"Equilateral triangle:({a} == {b} == {c})")
            return TriangleType.EQUILATERAL
        if a >= b + c or b >= a + c or c >= a + b:
            print(f"Invalid triangle: violates triangle inequality, one side is greater than or equal to the sum of the other two, a={a}, b={b}, c={c}")
            return TriangleType.INVALID

        x, y, z = sorted((a, b, c))
        if x * x + y * y == z * z:
            print(f"Right-angled triangle: {x}^2 + {y}^2 == {z}^2 ({x*x} + {y*y} == {z*z})")
            return TriangleType.RETANGLE
        if a == b or a == c or b == c:
            print(f"Isosceles triangle: at least two sides are equal, a={a}, b={b}, c={c}")
            return TriangleType.ISOSCELES
        print(f"Scalene triangle: all sides are different and valid, a={a}, b={b}, c={c}")
        return TriangleType.SCALENE
