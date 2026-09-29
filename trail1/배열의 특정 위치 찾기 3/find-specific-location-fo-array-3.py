arr = list(map(int, input().split()))

ans = 0
for i in range(len(arr)):
    if arr[i] == 0:
        ans = arr[i-3] + arr[i-2] + arr[i-1]
        break
    
print(ans)