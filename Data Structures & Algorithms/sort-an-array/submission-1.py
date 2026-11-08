class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)
    def merge(self,left,right):
        result=[]
        p1=0
        p2=0
        while(len(left)>p1 and len(right)>p2):
            if left[p1]>right[p2]:
                result.append(right[p2])
                p2+=1
            else:
                result.append(left[p1])
                p1+=1
        while(len(left)>p1):
            result.append(left[p1])
            p1+=1
        while(len(right)>p2):
            result.append(right[p2])
            p2+=1
        return result
    def merge_sort(self,nums):
        if len(nums)==0 or len(nums)==1:
            return nums
        return self.merge(self.merge_sort(nums[:len(nums)//2]),self.merge_sort(nums[len(nums)//2:len(nums)]))