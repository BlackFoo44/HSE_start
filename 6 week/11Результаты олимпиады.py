olimp = []
for i in range(int(input())):
    olimp.append((input().split()))
olimp.sort(key=lambda temp: (-int(temp[1]), (temp[0])))

for i in olimp:
    print(i[0])
