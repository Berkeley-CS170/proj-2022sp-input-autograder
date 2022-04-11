# Adapted from skeleton below. Different licence requirements may apply
# See https://github.com/Berkeley-CS170/project-sp22-skeleton

from __future__ import annotations

import dataclasses
from typing import Optional, TypeVar

from .distance import Distance
from . import parse

T = TypeVar("T")


def _coalesce(*args: Optional[T], default: T) -> T:
    for arg in args:
        if arg is not None:
            return arg
    return default


@dataclasses.dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int

    @staticmethod
    def distance(first: Point, second: Point):
        """Returns the distance between two points.
        >>> Point.distance(Point(0, 0), Point(3, 4))
        5.0
        """
        dx = first.x - second.x
        dy = first.y - second.y
        return ((dx ** 2) + (dy ** 2)) ** (1/2)

    @staticmethod
    def distance_precise(first: Point, second: Point):
        """Returns a Distance object that represents the distance between the
        two given points. We do this to avoid floating point imprecision.
        Distance objects support comparison with numbers and other distances.
        There may be bugs in the Distance implementation. Use at your own risk.
        >>> Point.distance_precise(Point(0, 0), Point(3, 4)) == 5
        True
        >>> Point.distance_precise(Point(0, 0), Point(2, 3)) < 5
        True
        >>> Point.distance_precise(Point(0, 0), Point(2, 3)) >= 5
        False
        """
        return Distance((first.x - second.x) ** 2 + (first.y - second.y) ** 2)

    def replace(self, *, x: Optional[int] = None, y: Optional[int] = None) -> Point:
        """Constructs a new Point with the parameters passed replaced.
        >>> point = Point(1, 2)
        >>> point.replace(y=3)
        Point(x=1, y=3)
        >>> point = Point(1, 2)
        >>> point.replace(x=5)
        Point(x=5, y=2)
        """
        return Point(
            x=_coalesce(x, default=self.x),
            y=_coalesce(y, default=self.y)
        )
    
    def __str__(self) -> str:
        return "Point (" + str(self.x) + ", " + str(self.y) + ")"

    @staticmethod
    def parse(line: str) -> Point:
        try:
            points = line.split()
            assert len(points) == 2
            x_s, y_s = points
            rv =  Point(x=int(x_s), y=int(y_s))
        except Exception as e:
            raise ValueError(e, "Error parsing points, expected two integers, actual {0}.".format(line))
        return rv

    def serialize(self, out):
        print(self.x, self.y, file=out)

    def serialize_to_string(self) -> str:
        return parse.serialize_to_string_impl(self.serialize, self)