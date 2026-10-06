a, b, c, d = map(int, input().split())

# Please write your code here.


total = 0

while True:
    if a == c and b == d:
        break

    b += 1
    total += 1
    
    if b == 60:
        a += 1
        b = 0
    

print(total)

    