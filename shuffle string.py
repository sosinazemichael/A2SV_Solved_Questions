class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [""] * len(s)
        for i in range(len(s)):
            char = s[i]
            target_pos = indices[i]
            result[target_pos] = char
            
     
        return "".join(result)
