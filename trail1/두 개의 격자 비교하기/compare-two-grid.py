n, m = map(int, input().split())

grid = [[0]*m for i in range(n)]

arr1 = [list(map(int, input().split())) for i in range(n)]
arr2 = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            grid[i][j] = 0
        else:
            grid[i][j] = 1


for row in grid:
    for elem in row:
        print(elem, end=" ")
    print()