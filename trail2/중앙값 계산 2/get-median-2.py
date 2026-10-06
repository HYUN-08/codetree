n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(len(arr)):
    arr2 = arr[:i+1]
    if (i+1) % 2 == 1:
        mid = i // 2
        arr2.sort()
        print(arr2[mid], end=' ')

