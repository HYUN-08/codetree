n = int(input())

# Please write your code here.
def hi(n):
    if n == 0:
        return
    hi(n-1)
    print("HelloWorld")

hi(n)