n = int(input())

num = 1

while n > 1:
    n //= num
    if n <= 1:
        print(num)
        break
    else:
        num += 1


