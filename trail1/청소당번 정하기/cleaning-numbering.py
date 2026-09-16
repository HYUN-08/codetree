n = int(input())

cnt_c = 0
cnt_h = 0
cnt_r = 0

for i in range(1, n+1):
    if i % 12 == 0:
        cnt_r += 1
    elif i % 3 == 0:
        cnt_h += 1
    elif i % 2 == 0:
        cnt_c += 1

print(cnt_c, cnt_h, cnt_r)


