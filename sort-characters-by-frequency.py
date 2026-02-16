from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
         
        count = Counter(s)
        sorted_chars = count.most_common()
        result = ""
        for char, freq in sorted_chars:
            result += char * freq
            
        return result
