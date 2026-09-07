a = list(input().split())
b = list(input().split())

a_age = int(a[0])
a_gender = a[1]

b_age = int(b[0])
b_gender = b[1]

if (a_age >= 19 and a_gender == "M") or (b_age >= 19 and b_gender == "M"):
    print(1)
else:
    print(0)