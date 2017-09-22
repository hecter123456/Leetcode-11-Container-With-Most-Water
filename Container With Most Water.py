import unittest

class unitest(unittest.TestCase):
    def testHeightNumberLessThanTwo(self):
        h = [1]
        ans = 0
        self.assertEqual(Solution().maxArea(h),ans);
    def testCase1(self):
        h = [5,8,1,2,3,4,5,6]
        ans = 36
        self.assertEqual(Solution().maxArea(h),ans);
class Solution():
    def maxArea(self, height):
        Ans = 0
        i , j = 0, len(height) - 1
        while i < j:
            Ans = max(Ans,min(height[i],height[j]) * (j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return Ans

if __name__ == '__main__':
    unittest.main()
