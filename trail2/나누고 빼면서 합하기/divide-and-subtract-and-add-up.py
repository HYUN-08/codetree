n, m = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
ans = a[0]

def change_m(m):
    global ans

    while m != 1:
        ans += a[m - 1]
        if m % 2 == 1:
            m -= 1
        else:
            m //= 2

    return ans

if m == 1:
    print(ans)
else:
    print(change_m(m))
