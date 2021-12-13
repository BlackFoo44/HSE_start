a = tuple(map(int, input().split()))
print(len(set(range(min(a[:2]), max(a[:2])+1)) &
          set(range(min(a[2:]), max(a[2:])+1))))
