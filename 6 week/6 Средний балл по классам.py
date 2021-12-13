school = ([], [], [])
fin = open('input.txt', 'r', encoding='utf8')
for line in fin:
    line = line.split()
    c = int(line[2])
    school[c - 9].append(int(line[3]))
for c in school:
    print(sum(c) / len(c), end=' ')
