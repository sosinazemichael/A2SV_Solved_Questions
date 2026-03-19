import sys

def solve():
     
    for i in range(1, 6):
        row = list(map(int, sys.stdin.readline().split()))
        if 1 in row:
             
            j = row.index(1) + 1
            result = abs(i - 3) + abs(j - 3)
            print(result)
            break

if __name__ == "__main__":
    solve()
