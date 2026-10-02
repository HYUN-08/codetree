n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
max_sum = -99999999999


for i in range(n):
    sum_value = nums[i] + nums[2*n - 1 - i]
    if sum_value > max_sum:
        max_sum = sum_value

print(max_sum)
