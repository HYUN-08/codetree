n, m = map(int, input().split())

arr_2d = [[0]*m for i in range(n)]

num = 1
for i in range(n):
    for j in range(m):
        arr_2d[i][j] = num
        print(arr_2d[i][j], end=" ")
        num += 1
    print()
