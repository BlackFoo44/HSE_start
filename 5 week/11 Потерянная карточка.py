n = int(input())
j = 0
for i in range(1, n+1):
    j += i
k = 0
for i in range(1, n):
    m = int(input())
    k += m
print(j - k)
