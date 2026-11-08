class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        for num in nums:
            if num==val:
                count+=1
        k=len(nums)-count
        while val in nums:
            nums.remove(val)
        return k