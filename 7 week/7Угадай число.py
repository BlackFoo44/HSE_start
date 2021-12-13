max_n = int(input())
result = set()
for i in range(1, max_n + 1):
    result.add(i)
biat = input()
while biat != "HELP":
    av = input()
    if av == "YES":
        result &= set(map(int, biat.split()))
    if av == "NO":
        result -= set(map(int, biat.split()))
    biat = input()
print(*sorted(result))
