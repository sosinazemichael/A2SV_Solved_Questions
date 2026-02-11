from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        count = Counter(nums)
        for i in count:
            if count[i] >= 2:
                result.append(i)
        return result
            

        
