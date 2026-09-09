n = int(input())
arr = [[0]*n for _ in range(n)]

num = 1

for i in range(n):
    c = n - i - 1
    if i % 2 == 0:
        for r in range(n-1, -1, -1):
            arr[r][c] = num
            num += 1
    else:
        for r in range(n):
            arr[r][c] = num
            num += 1
            
for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()