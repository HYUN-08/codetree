arr = list(map(int, input().split()))

total = 0
avg = 0
flag = True
for i in range(len(arr)):
    if arr[i] < 250:
        total += arr[i]
        avg = total / (i+1)
    else:
        flag = False
        break

if flag:
    print(f'{sum(arr)} {sum(arr)/10:.1f}')
else:
    print(f'{total} {avg:.1f}')



