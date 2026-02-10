from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        count = Counter(nums)
        for i in range(len(nums)):
            if count[nums[i]] == 1:
                return nums[i]

        
