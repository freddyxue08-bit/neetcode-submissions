class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=1,x
        while r>l:
            m=(l+r)//2
            if m*m==x:
                return m
            elif m*m>x:
                r=m
            else:
                l=m+1
        return l if l*l == x else l - 1