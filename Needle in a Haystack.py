from collections import Counter

def solve():
    try:
        s = input().strip()
        t = input().strip()
    except EOFError:
        return

    count_t = Counter(t)
    count_s = Counter(s)
    
    for char in count_s:
        if count_t[char] < count_s[char]:
            return  
        
    remaining = []
    for char in count_t:
        for _ in range(count_t[char] - count_s[char]):
            remaining.append(char)
    remaining.sort()
    
    res = []
    s_idx = 0
    rem_idx = 0
    
    while s_idx < len(s) or rem_idx < len(remaining):
        if s_idx < len(s) and rem_idx < len(remaining):
            if s[s_idx] < remaining[rem_idx]:
                res.append(s[s_idx])
                s_idx += 1
            elif remaining[rem_idx] < s[s_idx]:
                res.append(remaining[rem_idx])
                rem_idx += 1
            else:
                if s[s_idx:] < (remaining[rem_idx] + "".join(remaining[rem_idx+1:])):
                     res.append(s[s_idx])
                     s_idx += 1
                else:
                    res.append(remaining[rem_idx])
                    rem_idx += 1
        elif s_idx < len(s):
            res.append(s[s_idx])
            s_idx += 1
        else:
            res.append(remaining[rem_idx])
            rem_idx += 1
            
    print("".join(res))

solve()
