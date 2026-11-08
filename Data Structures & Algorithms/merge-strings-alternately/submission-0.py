class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new=""
        for i in range(min(len(word1),len(word2))):
            new=new+word1[i]+word2[i]
        if len(word1)>len(word2):
            for i in range(len(word2),len(word1)):
                new=new+word1[i]
        elif word2:
            for i in range(len(word1),len(word2)):
                new=new+word2[i]
        return new