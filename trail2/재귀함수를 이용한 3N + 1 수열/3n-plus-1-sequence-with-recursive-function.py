n = int(input())

# Please write your code here.
cnt = 0 
def f(n):
    global cnt
    
    # 종료
    if n == 1:
        return 1
    
    cnt += 1

    # 짝수면
    if n % 2 == 0:
        return f(n//2)
    
    else:
        return f(n*3+1)
    

f(n)
print(cnt)

