n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def abs_arr(arr):
    for a in arr:
        print(abs(a), end=' ')

abs_arr(arr)