N = int(input())

# Please write your code here.
def f(n):
    # 짝수일 경우
    if n % 2 == 0:
        if n == 2:
            return 2
    
    # 홀수일 경우
    else:
        if n == 1:
            return 1
    
    return n + f(n-2)

print(f(N))