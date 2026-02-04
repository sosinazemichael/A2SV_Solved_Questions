class Solution:    
    def findUnion(self, a, b):
        # code here
        result= set(a)|set(b)
        
        return sorted(list(result))
