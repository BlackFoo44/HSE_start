a, b, c, d, e = int(input()), int(input()),\
 int(input()), int(input()), int(input())
count_numbers = 0
for x in range(1001):
    if x != e:
        if (a * x ** 3 + b * x ** 2 + c * x + d) / (x - e) == 0:
            count_numbers += 1
print(count_numbers)
