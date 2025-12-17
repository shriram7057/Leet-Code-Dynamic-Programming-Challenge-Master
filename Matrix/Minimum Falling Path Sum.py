class Solution:
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        dp = matrix[0][:]  # copy first row

        for i in range(1, n):
            new_dp = [0] * n
            for j in range(n):
                best = dp[j]
                if j > 0:
                    best = min(best, dp[j - 1])
                if j < n - 1:
                    best = min(best, dp[j + 1])
                new_dp[j] = matrix[i][j] + best
            dp = new_dp

        return min(dp)
