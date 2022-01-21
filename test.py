# #2 folder have same no. files
# a = 10
# b = 10
#
#
# a = [1,2,3,4,5]
# b = [3,2,1,6,7]
#
# a = {i:i for i in a }
# b = {i:i for i in b }
#
# def get_hash(obj):
#     return obj
#
# r = [x for i in a if get_hash(a[i]) != get_hash(b[i]) ]
#
# print(r)


def get_encoded_value(data, v):
    import random
    return data + v[random.randint(0,4)]

def get_result(data):


    a = 1
    b = 2

    v = ['a', 'e', 'i', 'o', 'u']

    fib = [a]

    for i in range(len(data)):

        if i == 0:
            print(data[i])
            continue

        if i in fib and data[i] not in v:
            print(get_encoded_value(data[i], v))

        fib.append(b)
        r = a + b
        a = b
        b = r

print(get_result('this is the simple text'))