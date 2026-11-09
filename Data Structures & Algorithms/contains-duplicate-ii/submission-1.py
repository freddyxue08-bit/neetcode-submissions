class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k>=len(nums)-1:
            return len(nums)!=len(set(nums))
        for i in range(len(nums)-k):
            if len(nums[i:i+k+1])!=len(set(nums[i:i+k+1])):
                return True
        return False