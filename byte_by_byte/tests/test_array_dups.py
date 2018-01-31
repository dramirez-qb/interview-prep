import sys
sys.path.append('/Users/guajardo/Documents/Tech Interviews/interview_prep/byte_by_byte')
from dups_array import find_duplicates
import unittest


class TestArrayDups(unittest.TestCase):
    def test_array_dups(self):
        arr_1 = [1, 2, 2, 4, 3, 1, 5]
        arr_2 = [3, 3, 3]
        arr_3 = []
        arr_4 = [1, 2, 3]

        self.assertEqual(find_duplicates(arr_1), [1, 2])
        self.assertEqual(find_duplicates(arr_2), [3])
        self.assertEqual(find_duplicates(arr_3), [])
        self.assertEqual(find_duplicates(arr_4), [])


if __name__ == '__main__':
    unittest.main()
