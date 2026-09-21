a, b = map(int, input().split())

# Please write your code here.

def check_3(i):
    return i % 3 == 0

def check_369(i):
    while i > 0:
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            return True
            break
        i //= 10

cnt = 0
for i in range(a, b + 1):
    if check_3(i) or check_369(i):
        cnt += 1

print(cnt)
