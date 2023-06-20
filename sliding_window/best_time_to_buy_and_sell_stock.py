# Runtime: O(n)
# Memory: O(1)
#
# 1. the brute-force method is to select each day and find the 
# profit that could be taken by selling on every other day
# 2. Because you must buy before you can sell, you only have to
# compare to every subsequent day
# 3. If there exists a price following today's price that's lower than today's price,
# we want to start from there instead
# 4. Store the biggest difference in the sliding window in memory, then we can slide
# the left side of the window to the lowest price and be certain we didn't miss it

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Given a list containing daily prices of a stock,
        returns the highest possible profit that can be made
        by buying on a single day and selling on a single day.

        If no profit can be made, the function returns 0.

        Args:
            prices (list of int): a list of integers representing 
                prices of a stock on each day. Prices must be >0
        
        Returns:
            maxProfit (int): the highest possible profit that can be
                made by buying on a single day and selling on a single
                day.
        """
        profit = 0
        left_index = 0
        right_index = 1

        while right_index < len(prices):
            next_profit = prices[right_index] - prices[left_index]
            if next_profit > profit:
                profit = next_profit

            # if negative profit, then select this as our new lowest
            elif next_profit < 0:
                left_index = right_index

            # check the next value in the list
            right_index += 1

        return profit