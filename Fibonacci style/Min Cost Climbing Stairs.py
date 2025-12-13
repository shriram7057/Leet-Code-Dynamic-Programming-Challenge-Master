class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])

        a, b = cost[0], cost[1]  # a = cost to reach step 0, b = cost to reach step 1

        for i in range(2, n):
            c = min(a, b) + cost[i]
            a, b = b, c

        return min(a, b)
