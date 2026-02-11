class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            can_form = True
            for char in word:
                if word.count(char)>chars.count(char):
                    can_form = False
                    break           
            if can_form:
                count += len(word)
        return count
        
