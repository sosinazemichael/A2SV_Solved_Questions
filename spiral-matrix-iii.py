class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        result = [[rStart, cStart]]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        
        steps = 1   
        d = 0      
        r, c = rStart, cStart
        
        while len(result) < rows * cols:
            for _ in range(2):
                for _ in range(steps):
                    r += dr[d]
                    c += dc[d]
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                        if len(result) == rows * cols:
                            return result
            
                d = (d + 1) % 4
             
            steps += 1
            
        return result
