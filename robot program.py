import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()

    # prefix movement: L = -1, R = +1
    prefix = 0
    first_hit = -1

    # Step 1: find first time robot reaches 0 from x
    for i in range(n):
        if s[i] == 'L':
            prefix -= 1
        else:
            prefix += 1

        if x + prefix == 0:
            first_hit = i + 1
            break

    # If robot never reaches 0 within k seconds
    if first_hit == -1 or first_hit > k:
        print(0)
        continue

    # We hit zero once
    answer = 1
    remaining_time = k - first_hit

    # Step 2: find cycle length starting from 0
    prefix = 0
    cycle = -1

    for i in range(n):
        if s[i] == 'L':
            prefix -= 1
        else:
            prefix += 1

        if prefix == 0:
            cycle = i + 1
            break

    # If there is a cycle, count extra hits
    if cycle != -1:
        answer += remaining_time // cycle

    print(answer)
