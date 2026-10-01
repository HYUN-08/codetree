n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def find_max(n):
    if n == 1:
        return arr[0]
    
    # 두번 호출하지 않도록 저장
    pre_val = find_max(n-1)

    if arr[n-1] >= pre_val:
        return arr[n-1]
    else:
        return pre_val

    
print(find_max(n))
