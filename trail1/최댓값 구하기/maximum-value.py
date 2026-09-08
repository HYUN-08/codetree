a, b, c = map(int, input().split())

max_abc = a

if b >= max_abc:
    if c >= max_abc:
        max_abc = c
    else:
        max_abc = b


if c >= max_abc:
    if b >= max_abc:
        max_abc = b
    else:
        max_abc = c

print(max_abc)

