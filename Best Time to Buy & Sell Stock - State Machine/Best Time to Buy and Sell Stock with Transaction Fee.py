class Solution(object):
    def maxProfit(self, prices, fee):
        hold = -prices[0]   # Max profit when holding a stock
        cash = 0            # Max profit when not holding a stock

        for price in prices[1:]:
            prev_hold = hold
            prev_cash = cash

            # If we hold today: keep holding OR buy today (pay price)
            hold = max(prev_hold, prev_cash - price)

            # If we are in cash today: keep cash OR sell today (gain price - fee)
            cash = max(prev_cash, prev_hold + price - fee)

        return cash
