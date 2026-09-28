s = input()

def check(word, s):
    if word in s:
        print("Yes", end = ' ')
    else:
        print("No", end = ' ')

check('ee', s)
check('ab', s)