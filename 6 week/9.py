n, lim = int(input()), list(map(int, input().split()))
k, p = int(input()), list(map(int, input().split()))
pi = [0] * n
for press in p:
    pi[press - 1] += 1
for i in range(n):
    print('YES' if lim[i] - pi[i] < 0 else 'NO')
