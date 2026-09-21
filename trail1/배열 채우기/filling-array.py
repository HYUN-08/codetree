l = list(map(int, input().split()))
result = []
for i in range(10):
    if l[i] == 0:
        break
    result.append(l[i])

result = result[::-1]
print(*result)
