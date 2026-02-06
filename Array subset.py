from collections import Counter

class Solution:
    # Function to check if b is a subset of a.
    def isSubset(self, a, b):
        count_a = Counter(a)
        for x in b:
            if count_a[x] > 0:
                count_a[x] -= 1
            else:
                return False
        
        return True
