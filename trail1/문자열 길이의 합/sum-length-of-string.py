n = int(input())

s = [input() for _ in range(n)]

total = 0
cnt_a = 0

for word in s:
    total += len(word)
    if word[0] == 'a':
        cnt_a += 1

print(total, cnt_a)