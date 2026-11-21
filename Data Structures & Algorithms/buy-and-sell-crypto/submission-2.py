class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        smallest = prices[0]
        profit =0

        while i < len(prices):
            if prices[i] - smallest > profit:
                profit = prices[i] - smallest
            
            if prices[i] < smallest:
                smallest = prices[i]
            i+=1 
        
        if profit < 0:
            return 0
        else:
            return profit
            



        