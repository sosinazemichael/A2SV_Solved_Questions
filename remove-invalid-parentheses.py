from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]

        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = {s}
        
        while queue:
            valid_strings = [string for string in queue if isValid(string)]
            
            if valid_strings:
                return valid_strings
            
            next_level = set()
            for string in queue:
                for i in range(len(string)):
                    if string[i] in '()':
                        next_level.add(string[:i] + string[i+1:])
            
            queue = next_level
            
        return [""]
