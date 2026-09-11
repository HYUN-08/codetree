A = input()
result = ''

while len(A) > 0:
    cnt = 0
    check = A[0]
    for i in range(0, len(A)):
        if A[i] == check:
            cnt += 1
        else:
            break

    # print(A[i-1], cnt)
    result = result + A[i - 1] + str(cnt)

    A = A[cnt::]
    # print(A)

print(len(result))
print(result)
