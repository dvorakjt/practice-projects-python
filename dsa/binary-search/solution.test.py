import unittest
from solution import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_item_found(self):
        """Calling binary_search with items in the list should return their indices."""
        nums = [0, 1, 3, 7, 8, 10, 12]
        
        for i, n in enumerate(nums):
            self.assertEqual(binary_search(n, nums), i)

    def test_item_not_found(self):
        """Calling binary_search with items not in the list should return -1."""
        nums = [0, 1, 3, 7, 8, 10, 12]
        self.assertEqual(binary_search(9, nums), -1)
        self.assertEqual(binary_search(-20, nums), -1)
        self.assertEqual(binary_search(45, nums), -1)

    def test_empty_list(self):
        """Calling binary_search on an empty list should return -1."""
        nums = []
        self.assertEqual(binary_search(1, nums), -1)

    def test_tuple(self):
        """Calling binary_search on a tuple should return expected indices."""
        nums = (-3, 4, 67, 99, 108)

        for i, n in enumerate(nums):
            self.assertEqual(binary_search(n, nums), i)

if __name__ == '__main__':
    unittest.main()
