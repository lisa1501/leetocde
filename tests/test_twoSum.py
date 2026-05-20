import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from problems.twoSum import twoSum


class TestTwoSum(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEqual(twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(twoSum([3, 3], 6), [0, 1])

    def test_negative_numbers(self):
        self.assertEqual(twoSum([-1, -2, -3, -4, -5], -8), [2, 4])
        self.assertEqual(twoSum([-2, 7, 11, -15], -8), [1, 3])

    def test_duplicate_values(self):
        self.assertEqual(twoSum([1, 5, 5, 7], 10), [1, 2])
        self.assertEqual(twoSum([0, 4, 3, 0], 0), [0, 3])

    def test_no_solution(self):
        with self.assertRaises(ValueError):
            twoSum([1, 2, 3], 7)


if __name__ == "__main__":
    unittest.main()
