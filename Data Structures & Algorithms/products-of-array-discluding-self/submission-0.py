class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right=[0]*(len(nums)+1)
        left=[0]*(len(nums)+1)
        left[0]=1
        right[-1]=1
        for i in range(len(nums)):
            left[i+1]=left[i]*nums[i]
        for i in range(len(nums)-1,0,-1):
            right[i]=right[i+1]*nums[i]
        new=[0]*len(nums)
        for i in range(len(nums)):
            new[i]=left[i]*right[i+1]
        return new;
