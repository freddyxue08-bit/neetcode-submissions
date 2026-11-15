from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        while r>l:
            k=(l+r)//2
            hour=0
            for pile in piles:
                hour+=ceil(pile/k)
            if hour>h:
                l=k+1
            else:
                r=k
        return l
