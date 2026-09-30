n = int(input())
arr = [1, n]

i = 1
while arr[i] <= 100:
    i += 1
    arr.append(arr[-2] + arr[-1])

print(*arr)
