s = [int(i) for i in input().split()]
print(*[s[i] for i in range(len(s)) if s.count(s[i]) == 1])
