scores = list(map(float, input().split()))

avg = sum(scores) / len(scores)

print(round(avg, 1))