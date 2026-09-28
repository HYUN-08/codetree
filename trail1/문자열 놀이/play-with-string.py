s, q = input().split()
s = list(s)
q = int(q)

for _ in range(q):
    ask = list(input().split())
    # print(ask)
    if int(ask[0]) == 1:
        a = int(ask[1])-1
        b = int(ask[2])-1
        s[a], s[b] = s[b], s[a]
    else:
        for i in range(len(s)):
            if s[i] == ask[1]:
                s[i] = ask[2]

    print(''.join(s))
        

