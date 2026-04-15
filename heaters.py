class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_radius = 0
        m = len(heaters)
        
        for house in houses:
            low = 0
            high = m - 1
            dist_to_closest = float('inf')
            
            while low <= high:
                mid = low + (high - low) // 2
                
                if heaters[mid] =a= house:
                    dist_to_closest = 0
                    break
                elif heaters[mid] < house:
                    dist_to_closest = min(dist_to_closest, house - heaters[mid])
                    low = mid + 1
                else:
                    dist_to_closest = min(dist_to_closest, heaters[mid] - house)
                    high = mid - 1
           
            if dist_to_closest > max_radius:
                max_radius = dist_to_closest
                
        return max_radius
