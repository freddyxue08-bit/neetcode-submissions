class Solution:
    def isValid(self, s: str) -> bool:
        opened=[]
        for p in s:
            if p=="(" or p=="[" or p=="{":
                opened.append(p)
            elif p==")":
                if opened==[]:
                    return False
                elif opened[-1]!="(":
                    return False
                else:
                    opened.pop()
            elif p=="]":
                if opened==[]:
                    return False
                elif opened[-1]!="[":
                    return False
                else:
                    opened.pop()
            elif p=="}":
                if opened==[]:
                    return False
                elif opened[-1]!="{":
                    return False
                else:
                    opened.pop()
        if opened!=[]:
            return False
        return True