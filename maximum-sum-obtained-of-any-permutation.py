class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * (n + 1)
        
        for start, end in requests:
            freq[start] += 1
            freq[end + 1] -= 1
        
        for i in range(1, n):
            freq[i] += freq[i-1]
            
        freq = freq[:n]
 
        freq.sort()
        nums.sort()
         
        total_sum = 0
        MOD = 10**9 + 7
        
        for f, num in zip(freq, nums):
            total_sum = (total_sum + f * num) % MOD
            
        return total_sum
