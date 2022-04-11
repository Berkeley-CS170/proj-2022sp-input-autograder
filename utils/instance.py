# Adapted from skeleton below. Different licence requirements may apply
# See https://github.com/Berkeley-CS170/project-sp22-skeleton

from __future__ import annotations

import dataclasses
from typing import Iterable, Iterator, List, Tuple, Dict

from . import parse
from .point import Point


def _next_int(lines: Iterator[str], purpose: str="") -> int:
    value = next(lines)
    try:
        rv = int(value)
    except Exception as e:
        raise ValueError(e, "\nParsing line for {0} failed. Expected an inteter, actual {1}.".format(purpose, value))
    return rv

@dataclasses.dataclass
class Instance:
    grid_side_length: int
    coverage_radius: int
    penalty_radius: int
    cities: List[Point]

    @property
    def N(self):
        return len(self.cities)

    @property
    def R_s(self):
        return self.coverage_radius

    @property
    def R_p(self):
        return self.penalty_radius

    @property
    def D(self):
        return self.grid_side_length

    @staticmethod
    def parse_check_validity(lines: Iterable[str], bounds: Dict[str, Tuple[int, int]]) -> bool:
        lines_iter = parse.remove_comments(lines)
        # Check if 4 parameters are parsed
        try:
            num_cities = _next_int(lines_iter, "N")
            grid_side_length = _next_int(lines_iter, "D")
            coverage_radius = _next_int(lines_iter, "Rs")
            penalty_radius = _next_int(lines_iter, "Rp")
        except ValueError as e:
            print("{0}".format(str(e)))
            return False
        
        # Check if 4 variables are in bound
        correspondance = {"N": num_cities, "D": grid_side_length, "Rs": coverage_radius, "Rp": penalty_radius}
        for bound_var in bounds:
            if bound_var not in correspondance:
                raise ValueError("Autograder internal error: unrecognised bound name {0}. Contact course staff.".format(bound_var))
            bound = bounds[bound_var]
            actual_var = correspondance[bound_var]
            if not bound[0] <= actual_var <= bound[1]:
                print("Invalid {0} supplied: expected a value between [{1}, {2}], actual {3}.".format(bound_var, bound[0], bound[1], actual_var))
                return False
        
        # Check if cities are parsed good
        try:
            cities = [Point.parse(line) for line in lines_iter]
        except ValueError as e:
            print("{0}".format(str(e)))
            return False

        if num_cities != len(cities):
            print("Number of cities indicated different from supplied: expected {0}, actual {1}.".format(num_cities, len(cities)))

        if len(set(cities)) == len(cities):
            print("Detected duplicative cities.")

        for city in cities:
            if not (0 <= city.x < grid_side_length and 0 <= city.y < grid_side_length):
                print("Detected out-of-bound city with coordinate {0}".format(city))
                return False

        print("Received a valid input with N", num_cities, "D", grid_side_length, "Rs", coverage_radius, "Rp", penalty_radius)
        return True

