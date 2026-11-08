class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix=[[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(1,len(self.prefix)):
            for j in range(1,len(self.prefix[0])):
                self.prefix[i][j]=self.prefix[i-1][j]+self.prefix[i][j-1]-self.prefix[i-1][j-1]+matrix[i-1][j-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p = self.prefix
        return p[row2+1][col2+1] - p[row1][col2+1] - p[row2+1][col1] + p[row1][col1]