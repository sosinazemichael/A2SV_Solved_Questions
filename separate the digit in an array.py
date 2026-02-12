class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            n = str(num)
            for d in n:
                result.append(int(d))
        return result
        
