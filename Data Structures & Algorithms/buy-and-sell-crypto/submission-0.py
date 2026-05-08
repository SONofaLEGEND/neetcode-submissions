class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #brute force
        # iterate the loop through each day and the consecutive days 
        # O(n2) complexity

        #sliding window
        # left i, right j
        # if i > j -- i + 1, j + 1 -- calculate j - i store


        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r+=1
        return max_profit