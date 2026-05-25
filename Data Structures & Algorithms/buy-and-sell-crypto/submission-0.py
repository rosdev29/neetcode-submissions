class Solution:
    def maxProfit(self, prices):

        min_price = prices[0]
        max_profit = 0

        for price in prices:

            # cập nhật giá thấp nhất
            if price < min_price:
                min_price = price

            # tính lợi nhuận hiện tại
            profit = price - min_price

            # cập nhật lợi nhuận lớn nhất
            if profit > max_profit:
                max_profit = profit

        return max_profit