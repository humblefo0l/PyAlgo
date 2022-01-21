
def reorderLines(log):
    d = []
    c = []
    dd = {}

    for i in log:
        if isinstance(i[1], int):
            d.append(i)
        else:
            c.append(i)

        dd[i[0]] = i

    c.sort(key=lambda x: x[0])
    c.sort(key=lambda x: x[1:])
    d.sort(key=lambda x: x[0])
    d.sort(key=lambda x: x[1:], reverse=True)

    r = c+d
    for i in r:
        print(i)









log = [
    ['a1', 9,2,3,1],
    ['g1', 'act', 'car'],
    ['zo4', 4, 7],
    ['ab1', 'off', 'key', 'dog'],
    ['a8', 'act', 'zoo']
]

reorderLines(log)