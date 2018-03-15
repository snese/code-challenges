import unittest

from dict import Solution

class TestSolution(unittest.TestCase):

    s = Solution()

    def test_cae1(self):
        self.assertEqual(self.s.twoSum([1, 2, 3, 4], 4), [0, 2])

    def test_case2(self):
        self.assertEqual(self.s.twoSum([3, 2, 4], 5), [0, 1])
    
    def test_case3(self):
        self.assertEqual(self.s.twoSum([11, 2, 7, 11, 15], 9), [1, 2])

    
if __name__ == '__main__':
    unittest.main()