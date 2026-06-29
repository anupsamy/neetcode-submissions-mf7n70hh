class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxRev = 0
        l, r= 0, 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            maxRev = max(profit, maxRev)

            if prices[l] > prices[r]:
                l+= 1
            else:
                r+= 1
        
        return maxRev

