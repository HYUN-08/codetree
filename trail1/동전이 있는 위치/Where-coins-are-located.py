n, m = map(int, input().split())
arr = [[0]*n for _ in range(n)]

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    # print(r, c)
    if 0<=r-1<n+1 and 0<=r-1<n+1:
        arr[r-1][c-1] = 1

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()