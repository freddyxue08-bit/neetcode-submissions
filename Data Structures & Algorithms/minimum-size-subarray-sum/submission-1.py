class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        a=0
        total=0
        length=len(nums)+1
        for i in range(len(nums)):
            total+=nums[i]
            if total>=target:
                while total-nums[a]>=target:
                    total-=nums[a]
                    a+=1
                if i-a+1<length:
                    length=i-a+1
        if length==len(nums)+1:
            return 0
        return length
