N = int(input())

# Please write your code here.

cnt = 0

def f(n):
    global cnt

    if n == 1:
        return cnt

    cnt += 1

    # n이 짝수
    if n % 2 == 0:
        return f(n//2)

    # n이 홀수
    else:
        return f(n//3)
    

print(f(N))

