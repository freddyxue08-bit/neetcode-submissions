class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows    = [[0] * 9 for _ in range(9)]                       # rows[row][digit]
        columns = [[0] * 9 for _ in range(9)]                       # columns[col][digit]
        boxes   = [[[0] * 9 for _ in range(3)] for _ in range(3)]   # boxes[r][c][digit]
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    d = int(board[i][j]) - 1
                    rows[i][d]+=1
                    columns[d][j]+=1
                    boxes[i//3][j//3][d]+=1
        for i in range(9):
            for j in range(9):
                if rows[i][j]>1 or columns[i][j]>1:
                    return False
        for row in boxes:
            for element in row:
                for nb in element:
                    if nb>1:
                        return False
        return True
        
        