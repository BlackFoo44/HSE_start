N = int(input())
Int_List = list(map(int, input().split()))[:N]
x = int(input())
difference = []
for i in Int_List:
    difference.append(abs(x - i))
print(Int_List[difference.index(min(difference))])
