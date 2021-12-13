a = int(input())
b = int(input())
for i in range(a, b+1):
    num = i
    if str(num) == str(num)[::-1]:
        print(num)
