class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref=""
        new_pref=""
        if len(strs)==1:
            return strs[0]
        for i in range(min(len(strs[0]),len(strs[1]))):
            if strs[0][i]==strs[1][i]:
                pref+=strs[0][i]
            else:
                break
        for i in range(2,len(strs)):
            for j in range(min(len(pref),len(strs[i]))):
                if pref[j]==strs[i][j]:
                    new_pref+=pref[j]
                else:
                    break
            pref=new_pref
            new_pref=""

        return pref