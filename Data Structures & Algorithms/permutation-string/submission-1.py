class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        count1 = [0] * 26
        count2= [0]*26
        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')]+=1
        a,b=0,len(s1)-1
        for j in range(len(s1)):
            count2[ord(s2[j]) - ord('a')] += 1
        if count1 == count2:
            return True

        # slide: i is the new character entering on the right
        for i in range(len(s1), len(s2)):
            count2[ord(s2[i]) - ord('a')] += 1               # enters
            count2[ord(s2[i - len(s1)]) - ord('a')] -= 1     # leaves
            if count1 == count2:
                return True
        return False
                