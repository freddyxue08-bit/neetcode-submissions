class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need={}
        has= {}
        formed=0
        short=""
        for letter in t:
            need[letter]=need.get(letter,0)+1

        a,b=0,0
        for letter in s:
            if letter in need:
                has[letter]=has.get(letter,0)+1
                if has[letter]==need[letter]:
                    formed+=1
            if letter in need:
                while formed==len(need):
                    if b-a<len(short) or not short:
                        short=s[a:b+1]
                    if s[a] in need.keys():
                        has[s[a]]-=1
                        if has[s[a]]<need[s[a]]:
                            formed-=1
                            
                    a+=1
                

            b+=1
        return short
