class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem={}
        for num in nums:
            elem[num]=elem.get(num,0)+1
        return max(elem, key=elem.get)