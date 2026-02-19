class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            count = 0  # Reset count for every new number
            for j in nums:
                if j < i: # Compare values directly
                    count += 1
            result.append(count) # Add to list after checking all j's
        return result


      
