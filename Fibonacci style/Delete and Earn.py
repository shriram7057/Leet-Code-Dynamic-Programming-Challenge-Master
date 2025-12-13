class Solution(object):
    def deleteAndEarn(self, nums):
        if not nums:
            return 0

        # Step 1: Count total points for each number
        from collections import Counter
        count = Counter(nums)

        # Step 2: Convert into a sorted list of unique numbers
        unique_nums = sorted(count.keys())

        # Step 3: Dynamic Programming like House Robber
        prev = None
        a = 0  # dp[i-2]
        b = 0  # dp[i-1]

        for num in unique_nums:
            points = num * count[num]  # total points from choosing 'num'
            
            if prev == num - 1:
                # Adjacent → cannot take both
                c = max(b, a + points)
            else:
                # Not adjacent → free to take
                c = b + points

            a, b = b, c
            prev = num

        return b
