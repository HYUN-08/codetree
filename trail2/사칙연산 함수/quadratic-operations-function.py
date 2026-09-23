a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def add(a, c):
    return a + c

def minus(a, c):
    return a - c

def multiply(a, c):
    return a * c

def divide(a, c):
    return a // c

flag = 1
if o == "+":
    result = add(a, c)
elif o == "-":
    result = minus(a, c)
elif o == "*":
    result = multiply(a, c)
elif o == "/":
    result = divide(a, c)
else:
    flag = 0

if flag == 1:
    print(f'{a} {o} {c} = {result}')
else:
    print(False)




