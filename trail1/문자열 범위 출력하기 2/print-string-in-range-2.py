s = input()
n = int(input())

if n > len(s):
    print(s[::-1])

else:
    for i in range(len(s)-1, len(s)-n-1, -1):
        # print(i)
        print(s[i], end='')