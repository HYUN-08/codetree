n = int(input())
l = input().split()

total = ''
for i in l:
    total += i
# print(total)

for i in range(1, len(total)+1):
    print(total[i-1], end='')
    if i % 5 == 0:
        print()
