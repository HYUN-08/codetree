scores = list(map(int, input().split()))
cnt = [0] * 11

for score in scores:
    if score == 0:
        break
    
    for i in range(1, 11):
        if i == score // 10:
            cnt[i] += 1

for i in range(10, 0, -1):
    print(f"{i*10} - {cnt[i]}")
    