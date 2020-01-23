"""
Merge two sorted arrays with O(1) extra space
We are given two sorted array. We need to merge these two arrays such that the initial numbers
(after complete sorting) are in the first array and the remaining numbers are in the second array.
Extra space allowed in O(1).

Example:

Input: ar1[] = {10};
       ar2[] = {2, 3};
Output: ar1[] = {2}
        ar2[] = {3, 10}

Input: ar1[] = {1, 5, 9, 10, 15, 20};
       ar2[] = {2, 3, 8, 13};
Output: ar1[] = {1, 2, 3, 5, 8, 9}
        ar2[] = {10, 13, 15, 20}

This task is simple and O(m+n) if we are allowed to use extra space. But it becomes really complicated
when extra space is not allowed and doesn’t look possible in less than O(m*n) worst case time.
"""

def mergeArray(arr1, arr2):

    l = len(arr2) -1

    while l > -1:

        for i in range(len(arr1)):
            if arr1[i] > arr2[l]:
                arr1.insert(i, arr2.pop(l))
                arr2.append(arr1.pop(-1))
                arr2 = sorted(arr2)
        l -= 1
    print(arr1)
    print(arr2)


if __name__ == '__main__':
    arr1 = [1, 5,7]
    arr2 = [2, 3, 6,11,31]
    mergeArray(arr1, arr2)

    arr1 = [1, 5,7,6,11,31]
    arr2 = [2, 3 ]
    mergeArray(arr1, arr2)


