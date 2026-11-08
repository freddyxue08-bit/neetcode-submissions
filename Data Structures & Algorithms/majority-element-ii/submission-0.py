class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elems={}
        answer=[]
        for num in nums:
            elems[num]=elems.get(num,0)+1
        for elem in elems:
            if elems[elem]>len(nums)//3:
                answer.append(elem)
        return answer

        