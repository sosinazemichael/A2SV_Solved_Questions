class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3!=0:
            return []
        x = num//3
        return list([x-1, x, x+1])
