class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        hold = -prices[0]
        sell = 0
        cooldown = 0

        for price in prices[1:]:
            prev_hold = hold
            prev_sell = sell
            prev_cooldown = cooldown

            hold = max(prev_hold, prev_cooldown - price)
            sell = prev_hold + price
            cooldown = max(prev_cooldown, prev_sell)

        return max(sell, cooldown)