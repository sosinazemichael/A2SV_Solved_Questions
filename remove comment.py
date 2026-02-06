import re

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        full_text = "\n".join(source)
        pattern = r"//.*|/\*[\s\S]*?\*/"
        cleaned = re.sub(pattern, "", full_text)
        
        return [line for line in cleaned.split("\n") if line]
