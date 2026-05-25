class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        
        occupied_cols = set()
        occupied_pos_diagonals = set()
        occupied_neg_diagonals = set()

        def place_queen(row):
            if row == n:
                self.count += 1
                return

            for col in range(n):
                pos_diagonal = row + col
                neg_diagonal = row - col
                
                if (col in occupied_cols or 
                    pos_diagonal in occupied_pos_diagonals or 
                    neg_diagonal in occupied_neg_diagonals):
                    continue

                occupied_cols.add(col)
                occupied_pos_diagonals.add(pos_diagonal)
                occupied_neg_diagonals.add(neg_diagonal)

                place_queen(row + 1)

                occupied_cols.remove(col)
                occupied_pos_diagonals.remove(pos_diagonal)
                occupied_neg_diagonals.remove(neg_diagonal)

        place_queen(0)
        return self.count
