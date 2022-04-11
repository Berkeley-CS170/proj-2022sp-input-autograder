import unittest
import utils.instance as instance
import pathlib
import gradescope_utils.autograder_utils.decorators

SMALL_BOUNDS = {"N": (15, 25), "D": (30, 30), "Rs": (3, 3), "Rp": (8, 8)}
MEDIUM_BOUNDS = {"N": (15, 25), "D": (50, 50), "Rs": (3, 3), "Rp": (10, 10)}
LARGE_BOUNDS = {"N": (195, 205), "D": (100, 100), "Rs": (3, 3), "Rp": (14, 14)}

class TestInput(unittest.TestCase):

    @gradescope_utils.autograder_utils.decorators.weight(1.0)
    @gradescope_utils.autograder_utils.decorators.tags("Small")
    def test_small(self):
        try:
            with open(file=pathlib.Path("/autograder/submission/small.in"), mode="r") as f:
                self.assertTrue(instance.Instance.parse_check_validity(f, SMALL_BOUNDS), "")
        except FileNotFoundError as e:
            self.fail("Could not find small.in.")
    
    @gradescope_utils.autograder_utils.decorators.weight(1.0)
    @gradescope_utils.autograder_utils.decorators.tags("Medium")
    def test_medium(self):
        try:
            with open(file=pathlib.Path("/autograder/submission/medium.in"), mode="r") as f:
                self.assertTrue(instance.Instance.parse_check_validity(f, MEDIUM_BOUNDS), "")
        except FileNotFoundError as e:
            self.fail("Could not find medium.in.")

    @gradescope_utils.autograder_utils.decorators.weight(1.0)
    @gradescope_utils.autograder_utils.decorators.tags("Large")
    def test_large(self):
        try:
            with open(file=pathlib.Path("/autograder/submission/large.in"), mode="r") as f:
                self.assertTrue(instance.Instance.parse_check_validity(f, LARGE_BOUNDS), "")
        except FileNotFoundError as e:
            self.fail("Could not find large.in.")
    