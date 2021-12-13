a = list(map(int, input().split()))
min_value = a[0]
max_index = 0
for i in range(1, len(a)):
    if a[i] > max_value:
        max_value = a[i]
        max_index = i
print(max_value, max_index)
