import sys
sys.path.append('/Users/guajardo/Documents/Tech Interviews/interview_prep/byte_by_byte')
import fibonacci as fib
import unittest

class TestFib(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib.fib(0), 0)
        self.assertEqual(fib.fib(6), 8)
        with self.assertRaises(ValueError):
            fib.fib(-1)


if __name__ == '__main__':
    unittest.main()
