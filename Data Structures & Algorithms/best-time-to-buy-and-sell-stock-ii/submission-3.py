class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # This is the optimized greedy solution, of just capturing the days that there is an increase, because if there is an increase it will always be greater than just buying and hoding till the end of the week. This works because if everyday it consecutively went up it is like we buy the day before sell the day of and buy again at the same price if it keeps going up so essentially we never lose any money. 
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        return profit