class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        # States:
        # hold = max profit while holding a stock
        # sold = max profit when we just sold today
        # rest = max profit when we are not holding and not selling today (cooldown or doing nothing)

        hold = -prices[0]
        sold = 0
        rest = 0

        for price in prices[1:]:
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest

            # If we hold today: either we were already holding, or we buy today from rest state
            hold = max(prev_hold, prev_rest - price)

            # If we sold today: we must have held yesterday
            sold = prev_hold + price

            # If we rest today: either we rested yesterday or just sold yesterday
            rest = max(prev_rest, prev_sold)

        # Maximum profit is in not holding a stock (either rest or sold)
        return max(sold, rest)
