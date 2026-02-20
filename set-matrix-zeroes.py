class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # 1. Identify where the zeros are
        zero_rows = [False] * rows
        zero_cols = [False] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows[i] = True
                    zero_cols[j] = True

        # 2. Actually set the zeros
        for i in range(rows):
            for j in range(cols):
                if zero_rows[i] or zero_cols[j]:
                    matrix[i][j] = 0

        
