arr = [i for i in input().split()]
result = []
for i in range(len(arr)-1):
    if i % 2 == 0:
        result.append(arr[i+1])
        result.append(arr[i])
if len(arr) % 2 != 0:
    result.append(arr[-1])
print(' '.join(result))
