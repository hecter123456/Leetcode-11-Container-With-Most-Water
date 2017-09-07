import unittest

class unitest(unittest.TestCase):
    def testHeightNumberLessThanTwo(self):
        h = [1]
        ans = 0
        self.assertEqual(Solution().maxArea(h),ans);

class Solution():
    def maxArea(self, height):
        if len(height) < 2:
            return 0
        return None

if __name__ == '__main__':
    unittest.main()
