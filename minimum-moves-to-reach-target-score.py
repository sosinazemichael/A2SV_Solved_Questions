class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        steps = 0
        while target > 1:
            if maxDoubles == 0:
                steps += (target - 1)
                return steps
            
            # If target is even and we have doubles, divide it!
            if target % 2 == 0 and maxDoubles > 0:
                target //= 2
                maxDoubles -= 1
                steps += 1
            else:
                target -= 1
                steps += 1
                
        return steps
