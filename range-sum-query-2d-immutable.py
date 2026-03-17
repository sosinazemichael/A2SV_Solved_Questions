from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
            
        rows, cols = len(matrix), len(matrix[0])
        self.dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        
    
        for r in range(rows):
            row_data = matrix[r]
            dp_current = self.dp[r + 1]
            dp_prev = self.dp[r]
            
            for c in range(cols):
                dp_current[c + 1] = (row_data[c] + 
                                     dp_prev[c + 1] + 
                                     dp_current[c] - 
                                     dp_prev[c])

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
         
        return (self.dp[r2 + 1][c2 + 1] - 
                self.dp[r1][c2 + 1] - 
                self.dp[r2 + 1][c1] + 
                self.dp[r1][c1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
