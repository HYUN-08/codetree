l = list(map(int, input().split()))
total = 0
cnt = 0
for i in range(10):
    if l[i] == 0:
        break
    total += l[i]
    cnt += 1

print(total, round(total/cnt, 1))