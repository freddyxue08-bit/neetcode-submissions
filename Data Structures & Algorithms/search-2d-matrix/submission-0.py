class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix[0]),len(matrix)
        l,r=0,n*m
        while r>l:
            x=(l+r)//2
            if(matrix[x//m][x%m]==target):
                return True
            elif(matrix[x//m][x%m]>target):
                r=x
            else:
                l=x+1
        return False

        