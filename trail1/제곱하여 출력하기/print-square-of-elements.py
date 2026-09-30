n = int(input())
arr = list(map(int, input().split()))

arr2 = [elem**2 for elem in arr]

print(*arr2)