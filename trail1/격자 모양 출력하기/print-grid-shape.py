n, m = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    r, c = tuple(map(int, input().split()))
    if 0<=r<n+1 and 0<=c<n+1:
        arr[r][c] = r*c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(arr[i][j], end=' ')
    print()
