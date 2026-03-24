class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        m = len(grid[0])
        MOD = 12345
        
        p = [[1] * m for _ in range(n)]
        current_product = 1
        for r in range(n):
            for c in range(m):
                p[r][c] = current_product
                current_product = (current_product * grid[r][c]) % MOD
        current_product = 1
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                p[r][c] = (p[r][c] * current_product) % MOD
                current_product = (current_product * grid[r][c]) % MOD
                
        return p
