class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        state=0
        for i in range(len(prices)-1):
            if state==0:
                if prices[i+1]>prices[i]:
                    profit=profit-prices[i]
                    state=1
            if state==1:
                if prices[i+1]<prices[i]:
                    profit=profit+prices[i]
                    state=0
        if state == 1:
            profit += prices[-1]
        return profit
        