text = input()
pattern = input()

# Please write your code here.

def check(start):
    if text[start:start + len(pattern)] == pattern:
        return True
    else:
        return False

starts = []
flag = 0
for i in range(len(text)):
    if text[i] == pattern[0]:
        starts.append(i)

for start in starts:
    if check(start):
        flag = 1
        print(start)
        break

if flag == 0:
    print("-1")


