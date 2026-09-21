a, b = map(int, input().split())

# Please write your code here.
def is_prime(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True

def sum_prime(a, b):
    total = 0
    for i in range(a, b+1):
        if is_prime(i):
            total += i
    
    return total

print(sum_prime(a, b))

    