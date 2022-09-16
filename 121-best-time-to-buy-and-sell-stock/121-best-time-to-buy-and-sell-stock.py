class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mxProfit = 0
        if not prices:
            return 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                mxProfit = max(mxProfit, profit)
            else:
                l = r
            r+=1
        return mxProfit
            
            
        
        