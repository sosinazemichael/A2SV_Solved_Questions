class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = [str(n) for n in nums]
        n = len(strs)
        for i in range(1, n):
            current = strs[i]
            j = i - 1 # means we looks the left
            while j >= 0 and (current + strs[j] > strs[j] + current):
                strs[j + 1] = strs[j]
                j -= 1
            
            strs[j + 1] = current
            
        result = "".join(strs)
        
        return "0" if result[0] == '0' else result
