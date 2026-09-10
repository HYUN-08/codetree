n = int(input())

arr = [[1]*i for i in range(1, n+1)]

for i in range(1, n):
    for j in range(1, i):
        # print(i, j)
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]





for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()
