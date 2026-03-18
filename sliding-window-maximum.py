class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque()

        for index, num in enumerate(nums):
            while q and q[-1] < num:
                q.pop()
            q.append(num)

            if index >= k and nums[index - k] == q[0]:
                q.popleft()
            
            if index >= k - 1:
                result.append(q[0])
        
        return result
