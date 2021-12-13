def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


n = int(input())
j = 0
for i in range(1, n + 1):
    j += + factorial(i)
print(j)
