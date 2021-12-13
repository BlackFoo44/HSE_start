result = set()
n = int(input())
end = []
for i in range(1, n + 1):
    result.add(i)
for m in range(len(result)):
    temp = set(input().split())
    if temp != set(("HELP").split()):
        temp = set(map(int, temp))
        if 2 * len(temp) <= len(result):
            result -= temp
            end.append('NO')
        else:
            result -= result - temp
            end.append('YES')
    else:
        for k in end:
            print(k)
        print(*result)
        break
