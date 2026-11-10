class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum=prices[0]
        small=prices[0]
        diff=0
        for i in range(len(prices)):
            if prices[i]<small:
                small=prices[i]
            if prices[i]-small>diff:
                diff=prices[i]-small
        return diff
           
        

        

        