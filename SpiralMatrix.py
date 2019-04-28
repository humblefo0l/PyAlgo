"""
Print the given matrix sparingly
"""


def spiralMatrix(m):

    while m :
        if len(m[0]):
            for i in range(len(m[0])):
                print(m[0][i], end=" ")
            m.pop(0)

        if len(m):
            for i in range(len(m)):
                print(m[i][-1], end=" ")
                m[i].pop(-1)
        if len(m):
            for i in range(len(m[-1])-1, -1, -1):
                print(m[-1][i], end=" ")

            m.pop(-1)

        if len(m):
            for i in range(len(m)-1, -1, -1):
                print(m[i][0], end=" ")
                m[i].pop(0)


if __name__ == '__main__':

    m = [
            [1,2,3, 4, 5, 6],
            [7,8,9,10,11,12],
            [13,14,15,16,17, 18]
        ]
    spiralMatrix(m)


