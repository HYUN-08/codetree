a, b = map(int, input().split())

# Please write your code here.

def check_decimal(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def check_even(n):
    total = 0
    while n > 0:
        total = total + n % 10 
        n = n // 10
    # print(total)
    if total % 2 == 0:
        return True
    else:
        return False

cnt = 0
for i in range(a, b+1):
    # print(check_decimal(i), check_even(i))
    if check_decimal(i) and check_even(i):
        cnt += 1

print(cnt)

