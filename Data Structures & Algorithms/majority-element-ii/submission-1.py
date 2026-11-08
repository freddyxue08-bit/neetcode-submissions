class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1=None
        cand2=None
        count1=0
        count2=0
        for num in nums:
            if num==cand1:
                count1+=1
            elif num==cand2:
                count2+=1
            elif num!=cand1 and num!=cand2 and count1>0 and count2>0:
                count1-=1
                count2-=1
            elif num!=cand1 and num!=cand2 and count1==0:
                cand1=num
                count1=1
            else:
                cand2=num
                count2=1
        count1=0
        count2=0
        for num in nums:
            if num==cand1:
                count1+=1
            if num==cand2:
                count2+=1
        answer=[]
        if count1>len(nums)//3:
            answer.append(cand1)
        if count2>len(nums)//3:
            answer.append(cand2)
        return answer

        