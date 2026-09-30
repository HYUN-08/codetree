arr = list(map(int, input().split()))
cnt = [0] * 6

for a in arr:
    for i in range(6):
        if a == i+1:
            cnt[i] += 1

for i in range(6):
    print(f"{i+1} - {cnt[i]}")