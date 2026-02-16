class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0
        
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == 'x':
                    xy += 1
                else:
                    yx += 1
    
        if (xy + yx) % 2 != 0:
            return -1
        
        
        ans = (xy // 2) + (yx // 2)
        
       
        if xy % 2 != 0:
            ans += 2
            
        return ans
