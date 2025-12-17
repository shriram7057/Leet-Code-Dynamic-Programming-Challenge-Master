class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n

        # Start position
        dp[0] = 0 if obstacleGrid[0][0] == 1 else 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    if j > 0:
                        dp[j] += dp[j - 1]

        return dp[-1]
