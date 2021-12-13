a = list(map(int, input().split()))
b = [a.pop()]
a = b + a
print(*a)
