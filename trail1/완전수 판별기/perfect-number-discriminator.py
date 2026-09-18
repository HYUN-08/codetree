n = int(input())

total = 0
for i in range(1, n):
    if n / i == n // i:
        total += i

if total == n:
    print("P")
else:
    print("N")