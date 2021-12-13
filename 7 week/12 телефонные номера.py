def dig(string):
    res = ''.join(list(filter(str.isdigit, str(string.replace('+7', '8')))))
    if len(res) < 11:
        res = '8495' + res
    return res


with open('input.txt') as inFile:
    new_numb = dig(inFile.readline())
    numb = list(map(dig, inFile.readlines()))
for _ in numb:
    print('YES' if new_numb == _ else 'NO')
