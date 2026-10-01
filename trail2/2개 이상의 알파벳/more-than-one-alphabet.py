a = input()

# Please write your code here.

def chceck(a):
    ch = []
    result = False
    for i in range(len(a)):
        if a[i] not in ch:
            ch.append(a[i])
        
        if len(ch) == 2:
            result = True
            break
    
    return result


if chceck(a):
    print("Yes")
else:
    print("No")

