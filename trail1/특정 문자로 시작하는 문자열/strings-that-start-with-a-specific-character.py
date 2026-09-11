n = int(input())
words = [input() for _ in range(n)]
e = input()

total = 0
cnt = 0

for word in words:
    if word[0] == e:
        total += len(word)
        cnt += 1

print(f'{cnt} {(total / cnt):.2f}')