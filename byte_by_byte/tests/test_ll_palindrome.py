import sys
import unittest
sys.path.append('/Users/guajardo/Documents/Tech Interviews/interview_prep/byte_by_byte')
sys.path.append('/Users/guajardo/Documents/Tech Interviews/interview_prep/linkedlist')

from ll_palindrome import ll_is_palindrome
import linkedlist as ll


class TestLLPalindrome(unittest.TestCase):
    def setUp(self):
        self.ll_1 = ll.LinkedList()
        self.ll_1.append(2)
        self.ll_1.append(1)
        self.ll_1.append(2)
        self.ll_1.append(1)
        self.ll_1.append(2)

        self.ll_2 = ll.LinkedList()
        self.ll_2.append(2)
        self.ll_2.append(1)
        self.ll_2.append(1)
        self.ll_2.append(2)

        self.ll_3 = ll.LinkedList()
        self.ll_3.append(2)
        self.ll_3.append(1)
        self.ll_3.append(1)

    def test_ll_palindrome(self):
        self.assertEqual(ll_is_palindrome(self.ll_1.head), True)
        self.assertEqual(ll_is_palindrome(self.ll_2.head), True)
        self.assertEqual(ll_is_palindrome(self.ll_3.head), False)
        self.assertEqual(ll_is_palindrome(None), None)


if __name__ == '__main__':
    unittest.main()
