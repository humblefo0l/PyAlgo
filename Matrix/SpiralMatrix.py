def spiralMatrix(matrix):
    top = 0
    bottom = len(matrix) -1
    left = 0
    right = len(matrix[0]) -1

    dir = [0,1,2,3]
    dr=0
    while top <= bottom and left <= right:

        if dir[dr] == 0:
            for i in range(left, right+1):
                print(matrix[top][i], end=" ")
            top += 1
        elif dir[dr] == 1:
            for i in range(top, bottom+1):
                print(matrix[i][right], end=" ")
            right -= 1

        elif dir[dr] == 2:
            for i in range(right, left-1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1

        elif dir[dr] == 3:
            for i in range(bottom, top-1, -1):
                print(matrix[i][left], end=" ")
            left += 1
        dr = (dr+1) % 4

m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
# m = [[1, 2, 3, 4, 5],
#      [6, 7, 8, 9, 10],
#      [11,12,13,14,15],
#      [16,17,18,19,20]]

spiralMatrix(m)