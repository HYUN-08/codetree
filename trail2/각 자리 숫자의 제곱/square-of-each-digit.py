N = int(input())

# Please write your code here.

def ss(n):
    if n < 10:
        return n**2
    
    return ss(n//10) + (n%10)**2

print(ss(N))