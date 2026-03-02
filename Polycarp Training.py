
n = int(input())
a = list(map(int, input().split()))
 
a.sort()
 
k = 1
for contest_problems in a:
    if contest_problems >= k:
        k = k + 1   
print(k - 1)
