def deco(fun):
    c = 0
    def wrap(*args, **kwargs):
        nonlocal c
        f = fun(*args, **kwargs)
        c += 1
        print('c called  {} time'.format(c))

    return wrap




def coinChange(coin, index, value):
    """
    Recursive approch to solve this problem

    :param coin:
    :param index:
    :param value:
    :return:
    """
    if value == 0 :
        return 1
    elif value >0 and index>=0 and index < len(coin):
        a = coinChange(coin, index, value - coin[index])
        b = coinChange(coin, index + 1, value)
        v = (a + b)
        return v
    else:
        return 0


def coinChangeDP(coin, index, value, memo):
    """
    Dynamic way of solving this problem in similar way as done in previous problem
    :param coin:
    :param index:
    :param value:
    :param memo:
    :return:
    """

    if (index, value) in memo:
        return memo[(index, value)]

    if value == 0:
        return 1

    elif value > 0 and index >= 0 and index < len(coin):
        memo[(index, value)] =  coinChangeDP(coin, index, value - coin[index], memo) + coinChangeDP(coin, index + 1, value, memo)

        return memo[(index, value)]
    else:
        return 0

coin = [1, 2, 3]
index = 0
value = 4
memo = {}

print(coinChange(coin, index, value))
print(coinChangeDP(coin, index, value, memo))
# print(coinChangeDP2(coin, len(coin), value))