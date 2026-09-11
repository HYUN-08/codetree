l = ["apple", "banana", "grape", "blueberry", "orange"]

e = input()
cnt = 0

for s in l:
    if s[2] == e or s[3] == e:
        print(s)
        cnt += 1

print(cnt)