a, x = list(map(int, input().split())), int(input())
k = 1
a.append('a')
while a[k - 1] != 'a' and x <= a[k - 1]:
    k += 1
print(k)
