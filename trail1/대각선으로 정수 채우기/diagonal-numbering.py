n, m = map(int, input().split())

# Please write your code here.
arr = [[0] * m for _ in range(n)]

num = 1

for s in range(n + m - 1):
    for r in range(n):
        c = s - r
        if 0 <= c < m:
            arr[r][c] = num
            num += 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()
