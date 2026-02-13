from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        counts = Counter(s)
        for i in range(len(s) - 1):
            digit1 = s[i]
            digit2 = s[i+1]
            
            if digit1 != digit2:
                if counts[digit1] == int(digit1) and counts[digit2] == int(digit2):
                    return digit1 + digit2
 
        return ""
