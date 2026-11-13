from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        res=[]
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:   # drop smaller ones from the back
                q.pop()
            q.append(i)

        res = [nums[q[0]]] 
        for r in range(k,len(nums)):
            if q[0]==r-k:
                q.popleft()
            while q and nums[r]>nums[q[-1]]:
                q.pop()
            q.append(r)
            res.append(nums[q[0]])
        return res
        

        