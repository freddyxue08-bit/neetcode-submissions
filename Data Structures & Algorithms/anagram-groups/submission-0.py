class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words={}
        for word in strs:
            letters=[0]*26
            for letter in word:
                letters[ord(letter)-97]+=1
            letters=tuple(letters)
            words[letters]=words.get(letters,[])+[word]
        return list(words.values())