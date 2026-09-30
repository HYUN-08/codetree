arr = list(map(int, input().split()))

for i in range(3, 11):
    nxt = (arr[-2] + arr[-1]) % 10
    arr.append(nxt)

print(*arr)


