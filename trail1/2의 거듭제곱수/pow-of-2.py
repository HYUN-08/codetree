n = int(input())
cnt = 1

while True:
    if 2**cnt == n:
        print(cnt)
        break
    else:
        cnt += 1
