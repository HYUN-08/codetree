a = input()
b = input()

def a_b(s):
    c = ''
    for i in s:
        if i != ' ':
            c += i
    return c

print(a_b(a) + a_b(b))


