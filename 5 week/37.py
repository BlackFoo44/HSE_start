x = []
y = []
xy1 = []
xy = []
for i in range(8):
    n = list(map(int, input().split()[:2]))
    x.append(n[0])
    y.append(n[1])
for j in range(len(x)):
    if x[j] + y[j] != (x[j-1]) + (y[j-1]) and x[j] - y[j] != (x[j-1]) - (y[j-1]):
        if x[j] != x[j-1] and y[j] != y[j-1]:
            xy = str('No')
    else:
        xy = str('Yes')
print(xy)


