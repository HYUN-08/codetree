arr = list(map(int, input().split()))

for i in range(3, 11):
    arr.append(arr[-2]*2 + arr[-1])

print(*arr)