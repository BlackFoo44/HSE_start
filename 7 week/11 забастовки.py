n, k = map(int, input().split())
mySet = set()
weekends = set(range(7, n + 1, 7)) | set(range(6, n + 1, 7))
for i in range(k):
    a, b = map(int, input().split())
    mySet |= set(range(a, n + 1, b))
print(len(mySet - weekends))
