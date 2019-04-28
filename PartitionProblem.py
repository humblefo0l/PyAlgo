"""
Partition problem | DP-18
Partition problem is to determine whether a given set can be partitioned into two
subsets such that the sum of elements in both subsets is same.
Examples:

arr[] = {1, 5, 11, 5}
Output: true
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false
The array cannot be partitioned into equal sum sets.

Following are the two main steps to solve this problem:
1) Calculate sum of the array. If sum is odd, there can not be two subsets with equal sum,
so return false.
2) If sum of array elements is even, calculate sum/2 and find a subset of array with sum equal
to sum/2.

The first step is simple. The second step is crucial, it can be solved either using recursion
or Dynamic Programming.

"""

def _findPartition(arr, index, s):

    if s == 0:
        return True

    if index <0 and s > 0:
        return False

    if arr[index] > s:
        return _findPartition(arr, index-1, s)

    return _findPartition(arr, index -1, s-arr[index]) or \
           _findPartition(arr, index-1, s)

def _findPartitionDP(arr, index, s, memo):

    if (index, s) in memo:
        return memo[(index, s)]

    if s == 0:
        return True

    if index <0 and s > 0:
        return False

    if arr[index] > s:
        return _findPartitionDP(arr, index-1, s, memo)


    memo[(index, s)] =_findPartitionDP(arr, index -1, s-arr[index], memo) or \
           _findPartitionDP(arr, index-1, s, memo)

    return memo[(index, s)]


def findPartion(arr, index, s):
    if s%2 != 0:
        return False

    return _findPartition(arr, index, s//2)

def findPartionDP(arr, index, s, memo):
    if s%2 != 0:
        return False

    return _findPartitionDP(arr, index, s//2, memo)


if __name__ == '__main__':

    arr = [5,5,1,11,11,1,1,2,3,31,3,3,112,12,1,21,21,2,12,1,2,12,1,2]
    n = len(arr)
    s = sum(arr)

    print(findPartion(arr, n-1, s))
    memo = {}
    print(findPartionDP(arr, n-1, s, memo))
