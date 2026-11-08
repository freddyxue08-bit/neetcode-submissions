class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nbs={}
        for num in nums:
            nbs[num]=nbs.get(num,0)+1
        breakpoint=int(sorted(nbs.values(),reverse=True)[k-1])
        answer=[]
        for item in nbs.items():
            if item[1]>=breakpoint:
                answer.append(item[0])
        return answer
        
        