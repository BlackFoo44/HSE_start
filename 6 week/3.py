count_index_n = int(input())
N = list(map(int, input().split()))
if count_index_n == len(N) and len(N) <= 10**9:
    N.sort()
print(' '.join(map(str, N)))
