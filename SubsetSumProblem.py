"""
Subset Sum Problem | DP-25
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given
set with sum equal to given sum.
Example:

Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.

Let isSubSetSum(int set[], int n, int sum) be the function to find whether there is a subset of
set[] with sum equal to sum. n is the number of elements in set[].

The isSubsetSum problem can be divided into two subproblems
…a) Include the last element, recur for n = n-1, sum = sum – set[n-1]
…b) Exclude the last element, recur for n = n-1.
If any of the above the above subproblems return true, then return true.

Following is the recursive formula for isSubsetSum() problem.

isSubsetSum(set, n, sum) = isSubsetSum(set, n-1, sum) ||
                           isSubsetSum(set, n-1, sum-set[n-1])
Base Cases:
isSubsetSum(set, n, sum) = false, if sum > 0 and n == 0
isSubsetSum(set, n, sum) = true, if sum == 0


"""
def subsetSum(arr, size, weight):
    """
    This solution may try all subsets of given set in worst case. Therefore time complexity of the
    solution is exponential. The problem is in-fact NP-Complete (There is no known polynomial time
    solution for this problem).
    :param arr:
    :param size:
    :param weight:
    :return:
    """


    if weight == 0:
        return True

    if size == 0 and weight != 0:
        return False

    if arr[size-1]> weight:
        return subsetSum(arr, size-1, weight)

    return subsetSum(arr, size-1, weight) or subsetSum(arr, size-1, weight-arr[size-1])


def isSubsetSum(array, size, weight):
    # The value of sub_array[i][jj] will be
    # true if there is a
    # sub_array of array[0..jj-1] with weight equal to i
    sub_array = ([[False for i in range(weight + 1)]
               for i in range(size + 1)])

    # If weight is 0, then answer is true
    for i in range(size + 1):
        sub_array[i][0] = True


        # If weight is not 0 and array is empty,
        # then answer is false
        for i in range(1, weight + 1):
            sub_array[0][i] = False

        # Fill the sub_array table in botton up manner

        for i in range(1, size + 1):
            for jj in range(1, weight + 1):

                if jj < array[i - 1]:
                    sub_array[i][jj] = sub_array[i - 1][jj]
                if jj >= array[i - 1]:
                    sub_array[i][jj] = (sub_array[i - 1][jj] or
                                    sub_array[i - 1][jj - array[i - 1]])

                    # uncomment this code to print table
        # for i in range(size+1):
        #     for jj in range(weight+1):
        #         print(sub_array[i][jj], end=" ")
        #     print()
    return sub_array[size][weight]


if __name__ == '__main__':

    arr = [1,2,3]
    size = len(arr)
    weight = 4

    print(subsetSum(arr, size, weight))
    if (isSubsetSum(arr, size, weight) == True):
        print("Found a subset with given sum")
    else:
        print("No subset with given sum")

