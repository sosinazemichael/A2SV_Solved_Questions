import sys

def solve():
     
    n = int(sys.stdin.readline())
    r = list(map(int, sys.stdin.readline().split()))

    m = int(sys.stdin.readline())
    b = list(map(int, sys.stdin.readline().split()))
    
    max_r = 0
    current_r = 0
    for x in r:
        current_r += x
        max_r = max(max_r, current_r)
        
    max_b = 0
    current_b = 0
    for x in b:
        current_b += x
        max_b = max(max_b, current_b)
        
    print(max_r + max_b)

def main():
    line = sys.stdin.readline()
    if line:
        t = int(line)
        for _ in range(t):
            solve()

if __name__ == "__main__":
    main()
