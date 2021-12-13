all = set()
onlyone = set()
for i in range(int(input())):
    temp = set()
    for j in range(int(input())):
        temp.add(input())
    onlyone |= temp
    if i == 0:
        all = temp
    else:
        all &= temp
for s in [all, onlyone]:
    print(len(s), *s, sep='\n')
