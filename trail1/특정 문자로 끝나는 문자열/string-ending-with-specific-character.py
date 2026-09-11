words = [input() for _ in range(10)]
e = input()

flag = None

for word in words:
    if word[-1] == e:
        print(word)
        flag = 1

if not flag:
    print(flag)