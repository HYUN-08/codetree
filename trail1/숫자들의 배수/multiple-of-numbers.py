n = int(input())

cnt = 0
a = 1
while cnt < 2:
    print(n*a, end=' ')

    if n*a % 5 == 0:
        cnt += 1
    
    a += 1