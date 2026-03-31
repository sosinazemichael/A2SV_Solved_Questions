class Solution:
    def splitString(self, s: str) -> bool:
        
        def backtrack(index, prev_val):
            if index == len(s):
                return True
            for j in range(index, len(s)):
                val = int(s[index : j + 1])
                if val == prev_val - 1:
                    if backtrack(j + 1, val):
                        return True
            
            return False
        for i in range(len(s) - 1):
            initial_val = int(s[: i + 1])
            if backtrack(i + 1, initial_val):
                return True
        
        return False
