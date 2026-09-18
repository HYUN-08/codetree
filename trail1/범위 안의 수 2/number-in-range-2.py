total = 0
cnt = 0
for _ in range(10):
    n = int(input())
    if 0<=n<=200:
        total += n
        cnt += 1

print(total, round(total/cnt, 1))