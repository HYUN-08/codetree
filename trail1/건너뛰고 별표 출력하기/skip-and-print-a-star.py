n = int(input())

for i in range(n):
    for j in range(1+i):
        print("*", end='')
    print()
    print()

for i in range(n-1):
    for j in range(n-1-i, 0, -1):
        print("*", end='')
    print()
    print()