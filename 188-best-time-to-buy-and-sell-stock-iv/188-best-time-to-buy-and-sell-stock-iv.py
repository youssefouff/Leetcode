class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        #create an array that stores values of profit
        profitNums= [0]*len(prices)
        if not prices:
            return 0
        for i in range(k):
            pos = -prices[0]
            profit = 0
            for j in range(1, len(prices)):
                pos = max(pos, profitNums[j]-prices[j])
                profit = max(profit, pos+prices[j])
                profitNums[j] = profit
        return profitNums[-1]
        
        