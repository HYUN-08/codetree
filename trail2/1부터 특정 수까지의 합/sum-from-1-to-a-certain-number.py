n = int(input())

# Please write your code here.
def ten_divide(n):
    total = 0
    for i in range(1, n+1):
        total += i
    print(total//10)

ten_divide(n)