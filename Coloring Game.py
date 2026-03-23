import sys

def solve():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    max_val = a[n-1]
    count = 0
    for k in range(2, n):
        i = 0
        j = k - 1
        while i < j:
            if a[i] + a[j] > max_val - a[k] and a[i] + a[j] > a[k]:
                count += (j - i)
                j -= 1
            else:
                i += 1
                
    print(count)
t_str = sys.stdin.readline().strip()
if t_str:
    t = int(t_str)
    for _ in range(t):
        solve()
