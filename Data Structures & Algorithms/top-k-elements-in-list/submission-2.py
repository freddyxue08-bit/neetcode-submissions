class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nbs={}
        count=0
        answer=[]
        for num in nums:
            nbs[num]=nbs.get(num,0)+1
        buckets = [[] for _ in range(len(nums) + 1)]
        for item in nbs.items():
            buckets[item[1]].append(item[0])
        for bucket in range(len(buckets)-1,0,-1):
            if count>=k:
                break
            for element in buckets[bucket]:
                count+=1
                answer.append(element)
        return answer