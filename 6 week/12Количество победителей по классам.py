in_file = open('input.txt', 'r', encoding='utf8')
s = [[], [], []]
for line in in_file:
    s[int(line.split()[2])-9].append(int(line.split()[3]))
print(s)


