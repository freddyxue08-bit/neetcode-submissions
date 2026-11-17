class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r=0,len(nums)-1
        while r>l:
            m=(l+r)//2
            if nums[m]==target:
                return True
            if nums[m]>nums[l]:
                if nums[l]<=target<nums[m]:
                    r=m
                else:
                    l=m+1
            elif nums[r]>nums[m]:
                if nums[m]<target<=nums[r]:
                    l=m+1
                else:
                    r=m
            else:
                if sum(nums[m:r+1])==(r-m+1)*nums[m]:
                    r=m
                else:
                    l=m+1
        if nums[l]==target:
            return True
        return False