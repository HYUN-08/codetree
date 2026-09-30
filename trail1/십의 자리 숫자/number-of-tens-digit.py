arr = list(input().split())
cnt = [0] * 10

for i in range(len(arr)):
    if int(arr[i]) == 0:
        break
    else:
        for j in range(1, 10):
            if len(arr[i]) >= 2 and arr[i][-2] == str(j):
                # print(arr[i][-2])
                cnt[j] += 1

for i in range(1, 10):
    print(f"{i} - {cnt[i]}")
