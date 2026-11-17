class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l,r=max(nums),sum(nums)
        while r>=l:
            m=(l+r)//2
            running=1
            total=0
            for num in nums:
                if total+num>m:
                    running+=1
                    total=num
                else:
                    total+=num
            if running>k:
                l=m+1
            else:
                r=m-1
        return l
            