class Solution:
    def swap(self,nums: List[int],start:int, end:int):
            while end>start:
                t=nums[start]
                nums[start],nums[end]=nums[end],t
                end-=1
                start+=1
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        """
        Do not return anything, modify nums in-place instead.
        """
        self.swap(nums,0,len(nums)-1)
        self.swap(nums,0,(k-1))
        self.swap(nums,k,len(nums)-1)
        
        