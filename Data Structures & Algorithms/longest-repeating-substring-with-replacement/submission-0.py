class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        digits={}
        a=0
        window=0
        for i in range(len(s)):
            digits[s[i]]=digits.get(s[i],0)+1
            if (i - a + 1) - max(digits.values()) <= k:
                 if i - a + 1 > window:
                    window = i - a + 1
            else:
                while (i - a + 1) - max(digits.values()) > k:
                    digits[s[a]] -= 1
                    a += 1
        return window