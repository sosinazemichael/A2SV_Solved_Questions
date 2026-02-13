from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        count = Counter(changed)
        changed.sort()    
        result = []
        for num in changed:
            if count[num] == 0:
                continue
            count[num] -= 1
            double = num * 2
            if count[double] > 0:
                count[double] -= 1
                result.append(num)
            else:
                return []
                
        return result if len(result) == len(changed) // 2 else []
