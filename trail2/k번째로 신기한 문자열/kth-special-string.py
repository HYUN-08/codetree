n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
words = []
for s in str:
    if s[0:len(t)] == t:
        words.append(s)

words.sort()

print(words[k-1])