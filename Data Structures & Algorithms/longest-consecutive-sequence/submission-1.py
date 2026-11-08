class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        count=0
        new=0
        for num in num_set:
            if num-1 not in num_set:
                new=1
                while num+1 in num_set:
                    new+=1
                    num+=1
                if new>count:
                    count=new
        return count