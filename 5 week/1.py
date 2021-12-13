n = int(input())
jn = int(input())
if n < jn:
    for i in range(n, jn+1):
        print(i, end=" ")
elif n > jn:
    for i in range(n, jn - 1, -1):
        print(i, end=' ')
elif n == jn:
    print(n)
