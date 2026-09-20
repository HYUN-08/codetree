n = int(input())

r = 1
for i in range(1, 11):
    r *= i
    if r >= n:
        print(i)
        break