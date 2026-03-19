import sys

def solve():
    # Use fast I/O for 10^5 elements
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    k = int(input[1])
    a = list(map(int, input[2:]))
    
    counts = {}
    left = 0
    total_good_segments = 0
    unique_count = 0
    
    for right in range(n):
        val = a[right]
        if val not in counts or counts[val] == 0:
            unique_count += 1
            counts[val] = 1
        else:
            counts[val] += 1
        while unique_count > k:
            left_val = a[left]
            counts[left_val] -= 1
            if counts[left_val] == 0:
                unique_count -= 1
            left += 1
        
        total_good_segments += (right - left + 1)
        
    print(total_good_segments)

if __name__ == "__main__":
    solve()
