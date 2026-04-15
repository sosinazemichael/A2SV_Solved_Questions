class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        
        while low < high:
            mid = low + (high - low) // 2
            current_load = 0
            required_days = 1
            for w in weights:
                if current_load + w > mid:
                    required_days += 1
                    current_load = w
                else:
                    current_load += w

            if required_days > days:
                low = mid + 1
            else:
                 
                high = mid
                
        return low
