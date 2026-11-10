class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        letters={}
        a,b=0,0
        for i in range(len(s)):
            b+=1
            if letters.get(s[i],-1)==-1:
                letters[s[i]]=i
            else:
                if letters[s[i]]+1>a:
                    a=letters[s[i]]+1
                letters[s[i]]=i
            if b-a>length:
                length=b-a
        return length

