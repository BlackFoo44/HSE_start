inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
mass = []
for line in inFile:
    mass.append(line.split())
for i in range(len(mass)):
    mass[i].pop(2)
mass.sort()
for i in range(len(mass)):
    print(*mass[i], file=outFile)
inFile.close()
outFile.close()
