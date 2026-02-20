class Solution:
    def hIndex(self, citations: List[int]) -> int:
        result = 0
        citations = sorted(citations, reverse=True)
        for j in range(1, len(citations) + 1):
            i = citations[j-1]
            if i >= j:
                result = j  
            else:
                break 
                
        return result
