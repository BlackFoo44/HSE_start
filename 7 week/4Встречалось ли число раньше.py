mylist = list(map(int, input().split()))
b = set()
for i in mylist:
    print('NO' if i not in b else 'YES')
    b.add(i)
