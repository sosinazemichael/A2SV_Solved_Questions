from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        count = Counter(nums)
        for n in count:
            if count[n] >  len(nums)//3 :
                result.append(n)
        return result

        
