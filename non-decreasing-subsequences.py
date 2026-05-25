class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start, current_path):
            if len(current_path) >= 2:
                result.append(list(current_path))
            
            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                
                if not current_path or nums[i] >= current_path[-1]:
                    used.add(nums[i])
                    current_path.append(nums[i])
                    backtrack(i + 1, current_path)
                    current_path.pop()
                    
        backtrack(0, [])
        return result
