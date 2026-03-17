from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.at_most(nums, goal) - self.at_most(nums, goal - 1)

    def at_most(self, nums: List[int], goal: int) -> int:
        if goal < 0:
            return 0
            
        tail = 0
        current_sum = 0
        count = 0
        
        for head in range(len(nums)):
            current_sum += nums[head]
            
            while current_sum > goal and tail <= head:
                current_sum -= nums[tail]
                tail += 1
            
            count += (head - tail + 1)
            
        return count
