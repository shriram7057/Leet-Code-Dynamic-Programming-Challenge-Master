class Solution(object):
    def rob(self, nums):
        a = 0  # dp[i-2]
        b = 0  # dp[i-1]

        for money in nums:
            c = max(b, a + money)
            a, b = b, c

        return b
