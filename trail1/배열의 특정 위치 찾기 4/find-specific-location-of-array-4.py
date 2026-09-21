l = list(map(int, input().split()))

cnt = 0
total = 0
for i in range(10):
    if l[i] == 0:
        break
    if l[i] % 2 == 0:
        cnt += 1
        total += l[i]

print(cnt, total)