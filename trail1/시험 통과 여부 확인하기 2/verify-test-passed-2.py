n = int(input())
scores = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for score in scores:
    if sum(score) / 4 >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")
print(cnt)