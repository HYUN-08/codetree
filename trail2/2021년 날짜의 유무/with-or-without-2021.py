m, d = map(int, input().split())

# Please write your code here.
day31 = [1, 3, 5, 7, 8, 10, 12]
def check(m, d):
    if m in day31:
        if 1 <= d <= 31:
            return True
    elif m == 2:
        if 1 <= d <= 28:
            return True
    elif m in [4, 6, 9, 11]:
        if 1 <= d <= 30:
            return True
    
    return False

if check(m, d):
    print("Yes")
else:
    print("No")

    