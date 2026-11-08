class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand=nums[0]
        count=0
        for num in nums:
            if num==cand:
                count+=1
            elif num!=cand and count>1:
                count-=1
            else:
                cand=num
                count=1
        return cand