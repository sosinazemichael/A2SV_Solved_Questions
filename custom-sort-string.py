from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        result = []
        for char in order:
            if char in counts:
                result.append(char * counts[char])
                del counts[char]
        for char, count in counts.items():
            result.append(char * count)
            
        return "".join(result)
