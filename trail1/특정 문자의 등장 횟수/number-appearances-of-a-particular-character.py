s = input()

def cnt(s, word):
    cnts = 0
    for i in range(len(s)-1):
        if s[i:i+2] == word:
            cnts += 1
    print(cnts, end = ' ')

cnt(s, "ee")
cnt(s, "eb")