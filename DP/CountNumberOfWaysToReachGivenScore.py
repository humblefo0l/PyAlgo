"""
Count number of ways to reach a given score in a game
Consider a game where a player can score 3 or 5 or 10 points in a move. Given a
total score n, find number of ways to reach the given score.
Examples:

Input: n = 20
Output: 4
There are following 4 ways to reach 20
(10, 10)
(5, 5, 10)
(5, 5, 5, 5)
(3, 3, 3, 3, 3, 5)

Input: n = 13
Output: 2
There are following 2 ways to reach 13
(3, 5, 5)
(3, 10)
"""

def count(arr, size, n):

    if n == 0:
        return 1

    if n < 0:
        return 0

    if size < 0 :
        return 0

    return (count(arr, size-1, n) + count(arr, size, n-arr[size]))


def countDP(arr, size, n, memo):
    if (size, n) in memo:
        return memo[(size, n)]

    if n == 0:
        return 1

    if n<0 or size <0:
        return 0

    memo[(size, n)] = countDP(arr, size-1, n, memo) + \
                      countDP(arr, size, n-arr[size], memo)

    return memo[(size, n)]

# Driver Program
arr = [3,5,10]
n = 20
memo = {}
print('Count for', n, 'is', count(arr, len(arr)-1, n))
print('Count for', n, 'is', countDP(arr, len(arr)-1, n, memo))

n = 13
print('Count for', n, 'is', count(arr, len(arr)-1, n))
print('Count for', n, 'is', countDP(arr, len(arr)-1, n, memo))

