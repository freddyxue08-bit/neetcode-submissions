from math import floor,ceil
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        while r>l:
            m=(l+r)//2
            day=1
            running=0
            for weight in weights:
                running+=weight
                if running>m:
                    day+=1
                    running=weight
            
            if day>days:
                l=m+1
            else:
                r=m
        return l

                