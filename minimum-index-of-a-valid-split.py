from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        right_counts = Counter(nums)
        left_counts = Counter()
        total_length = len(nums)

        for split_index, value in enumerate(nums):
            right_counts[value] -= 1
            left_counts[value] += 1

            left_size = split_index + 1
            right_size = total_length - split_index - 1
            
            if (left_counts[value] * 2 > left_size and
                right_counts[value] * 2 > right_size):
                return split_index

        return -1
