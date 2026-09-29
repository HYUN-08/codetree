arr = list(map(int, input().split()))

even = 0
sum3 = 0
cnt = 0

for i in range(10):
    if i % 2 == 1:
        even += arr[i]
    if (i+1) % 3 == 0:
        sum3 += arr[i]
        cnt += 1

print(even, round(sum3/cnt, 1))