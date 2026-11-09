class Solution:
    def twoSum(self, nums:List[int],num: int,target: int):
        ans=[]
        i,j=0,len(nums)-1
        while (j>i):
            s=nums[i]+nums[j]
            if s==target:
                ans.append([num,nums[i],nums[j]])
                i+=1
                j-=1
                while j>i and nums[i]==nums[i-1]:
                    i+=1
                    continue
                while j>i and nums[j]==nums[j+1]:
                    j-=1
                    continue
            elif s>target:
                j-=1
            else:
                i+=1
        return ans
    def threeSum(self,nums:List[int], num: int, target:int):
        ans=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for t in self.twoSum(nums[i+1:],nums[i],target-nums[i]):
                ans.append([num]+t)
        return ans
            
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            nums.sort()
            ans=[]
            for i in range(len(nums)-3):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                ans+=(self.threeSum(nums[i+1:],nums[i],target-nums[i]))
            return ans
        