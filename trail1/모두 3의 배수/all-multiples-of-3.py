flag = True
for i in range(5):
    n = int(input())
    if n % 3 != 0:
        flag = False
        break

if flag:
    print(1)
else:
    print(0)