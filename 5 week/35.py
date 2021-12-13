a = list(map(int, input().split()))
temp = []
for x in a:
    if x not in temp:
        temp.append(x)
print(*temp)
