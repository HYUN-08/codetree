s = list(input().split())

total = 0

for word in s:
    total += len(word)

print(total)