import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from problems.hasDuplicate import hasDuplicate


class TestHasDuplicate(unittest.TestCase):

    def test_has_duplicate_true(self):
        self.assertTrue(hasDuplicate([1, 2, 3, 3]))
        self.assertTrue(hasDuplicate([5, 5, 5, 5]))
        self.assertTrue(hasDuplicate([0, 1, 0]))

    def test_has_duplicate_false(self):
        self.assertFalse(hasDuplicate([1, 2, 3, 4]))
        self.assertFalse(hasDuplicate([]))
        self.assertFalse(hasDuplicate([42]))

    def test_has_duplicate_mixed_values(self):
        self.assertTrue(hasDuplicate([-1, 1, -1]))
        self.assertFalse(hasDuplicate([-1, 0, 1]))


if __name__ == "__main__":
    unittest.main()
