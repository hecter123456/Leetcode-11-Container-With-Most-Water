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
        if len(height) < 2:
            return 0
        Ans = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                tmp = min(height[i],height[j]) * (j-i)
                Ans = max(Ans,tmp)
        return Ans

if __name__ == '__main__':
    unittest.main()
