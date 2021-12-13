def is_ascending(b):
    i = 1
    while i < len(b) and b[i - 1] < b[i]:
        i += 1
    if i == len(a):
        return 'YES'
    return 'NO'


a = list(map(int, input().split()))
print(is_ascending(a))
