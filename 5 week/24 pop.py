a = input().split()
k = int(input())
a = [elem for num, elem in enumerate(a) if num != k]
print(*a)
