class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        buy1 = -prices[0]
        sell1 = 0
        buy2 = -prices[0]
        sell2 = 0

        for price in prices:
            # Update states in correct order
            buy1 = max(buy1, -price)             # first buy
            sell1 = max(sell1, buy1 + price)     # first sell
            buy2 = max(buy2, sell1 - price)      # second buy
            sell2 = max(sell2, buy2 + price)     # second sell

        return sell2
