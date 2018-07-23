import unittest

from distributeCandies import Solution

class TestSolution(unittest.TestCase):

    s = Solution()

    def test_cae1(self):
        self.assertEqual(self.s.distributeCandies([3, 4, 7, 7, 6, 6]), 3)
        
    def test_case2(self):
        self.assertEqual(self.s.distributeCandies([80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]), 3)
    
if __name__ == '__main__':
    unittest.main()