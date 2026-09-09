arr = [[0]*5 for _ in range(5)]

for i in range(5):
    arr[0][i] = 1
    arr[i][0] = 1

for r in range(1, 5):
    for c in range(1, 5):
        arr[r][c] = arr[r-1][c] + arr[r][c-1]

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()
