n = int(input())
arr = list(map(int, input().split()))
counting = [0] * 9

for elem in arr:
    for i in range(1, 10):
        if elem == i:
            counting[i-1] += 1

for elem in counting:
    print(elem)
