a = list(input().split())
b = list(input().split())
c = list(input().split())

A = 0
B = 0
C = 0
D = 0

total = [a, b, c]

for row in total:
    if row[0] == "Y":
        if int(row[1]) >= 37:
            A += 1
        else:
            C += 1
    else:
        if int(row[1]) >= 37:
            B += 1
        else:
            D += 1

if A >= 2:
    print("E")
else:
    print("N")

