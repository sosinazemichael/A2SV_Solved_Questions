class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        result = 0
        piles= sorted(piles)
        for i in range(len(piles) //3, len(piles),2):
            result += piles[i]
        return result

        
