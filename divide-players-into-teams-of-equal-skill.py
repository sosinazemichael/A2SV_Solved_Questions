from math import prod
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        a=n//2
        total=sum(skill)
        target=total//a
        skill.sort()
        left=0
        right=n-1
        result=[]

        while left<right:
            if skill[left]+skill[right]>target:
                right-=1
            elif  skill[left]+skill[right]<target:
                left+=1  
            else:
                result.append([skill[left],skill[right]])
                left +=1 
                right-=1

        if len(result) != a:
            return -1 
        answer=0        
        for i in result:
            answer+=i[0]*i[1]
        return answer
