class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                v = nums[i]
                nums[i], nums[v-1] = nums[v-1], v
        for i in range(len(nums)):
            if i+1!=nums[i]:
                return i+1
        return len(nums)+1