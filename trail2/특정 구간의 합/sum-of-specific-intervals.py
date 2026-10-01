n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def sum_interval(a1, a2):
    print(sum(arr[a1-1:a2]))

for a1, a2 in queries:
    sum_interval(a1, a2)