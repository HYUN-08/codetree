n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def lcm(n):
    if n == 1:
        return arr[0]

    # 이전 숫자들의 최소공배수
    prev_lcm = lcm(n - 1)
    curr = arr[n - 1]

    # prev_lcm 과 curr의 최소공배수 구하기
    if curr >= prev_lcm:
        candidate = curr
    else:
        candidate = prev_lcm

    step = candidate

    while not (candidate % curr == 0 and candidate % prev_lcm == 0):
        candidate += step

    return candidate

print(lcm(n))
