class Solution:
    def minStartValue(self, nums: List[int]) -> int:        
        prefix = 0
        min_prefix = 0

        for n in nums:
            prefix += n
            min_prefix = min(min_prefix,prefix)

        return abs(min_prefix) + 1
