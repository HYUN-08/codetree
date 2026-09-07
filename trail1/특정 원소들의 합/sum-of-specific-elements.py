board = [list(map(int, input().split())) for i in range(4)]
# print(board)

total = 0
for r in range(4):
    for c in range(0, r+1):
        total += board[r][c]
    
print(total)