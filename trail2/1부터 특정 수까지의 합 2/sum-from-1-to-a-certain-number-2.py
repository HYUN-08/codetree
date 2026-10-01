N = int(input())

# Please write your code here.

def s(n):
    if n == 1:
        return 1
    
    return n + s(n-1)

print(s(N))