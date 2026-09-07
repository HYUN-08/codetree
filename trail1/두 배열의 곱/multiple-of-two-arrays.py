arr1 = [list(map(int, input().split())) for i in range(3)]
input() # 빈 줄 처리
arr2 = [list(map(int, input().split())) for i in range(3)]
# print(arr1)
# print(arr2)

arr_2d = [[0]*3 for i in range(3)]
# print(arr_2d)

for i in range(3):
    for j in range(3):
        arr_2d[i][j] = arr1[i][j] * arr2[i][j]
        print(arr_2d[i][j], end=" ")
    print()