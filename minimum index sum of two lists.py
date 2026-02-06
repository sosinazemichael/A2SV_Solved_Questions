class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_sum = float('inf') 
        
        for n in list1:
            if n in list2:  
                i = list1.index(n)
                j = list2.index(n)
                x = i + j
                
                if x < min_sum:
                    min_sum = x
                    result = [n]  
                elif x == min_sum:
                    result.append(n)  
                    
        return result
