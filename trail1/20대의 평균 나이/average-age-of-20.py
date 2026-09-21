
total = 0
cnt = 0

while True:
    n = int(input())
    if n//10 == 2:
        total += n
        cnt += 1

    else:
        print(f'{total/cnt:.2f}')
        break