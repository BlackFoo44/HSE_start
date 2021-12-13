with open('input.txt') as inFile:
    numWord = dict()
    for line in inFile:
        for word in line.strip().split():
            numWord[word] = numWord.get(word, - 1) + 1
            print(numWord[word], end=' ')
