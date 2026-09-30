arr = list(map(int, input().split()))

for a in arr:
    if a == 0:
        break
    
    else:
        if a % 2 == 1:
            print(a+3, end=' ')
        else:
            print(a//2, end=' ')
