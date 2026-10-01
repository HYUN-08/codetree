a, b, c = map(int, input().split())

# Please write your code here.

n = a*b*c
def sum_ones(n):
    if n < 10:
        return n
    
    return sum_ones(n//10) + n%10

print(sum_ones(n))
