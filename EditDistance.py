"""
Edit Distance | DP-5
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of
edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
All of the above operations are of equal cost.

Examples:

Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations.
Replace 'n' with 'r', insert t, insert a

"""

def editDistance(string1, string2):
    """
    Video: https://www.youtube.com/watch?v=We3YDTzNXEk

    :param string1:
    :param string2:
    :return:
    """
    string1 = [i for i in string1]
    string2 = [i for i in string2]

    dp = [[0 for i in range(len(string1)+1)] for j in range(len(string2)+1)]

    # print("-->> {}, {}".format(len(dp), len(dp[0])))
    for i in range(len(dp)):
        dp[i][0] = i

    for i in range(len(dp[0])):
        dp[0][i] = i

    # print(dp)
    for i in range(1,len(string2)+1):

        # dp[0][i-1] = i-1

        for j in range(1, len(string1)+1):
            # dp[j-1][0] = j-1

            if string2[i-1] == string1[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])

    # print(dp)
    return dp[len(string2)][len(string1)]


def editDistanceRecur(str1, str2, index):
    if index == 0:
        return 1

    if index < 0:
        return 0

    if str1[index] == str2[index]:
        return  editDistance( str1, str2, index-1)

    return min(
        editDistance(str1, str2, index)
    )


if __name__ == '__main__':

    string1 = "cat"
    string2 = "cut"
    print("Min edit to convert {} into {} is {}".format(string1, string2,editDistance(string1, string2)))
    print()
    string1 = "azced"
    string2 = "abcdef"
    print("Min edit to convert {} into {} is {}".format(string1, string2,editDistance(string1, string2)))
    print()
    string2 = "sunday"
    string1 = "saturday"
    print("Min edit to convert {} into {} is {}".format(string1, string2,editDistance(string1, string2)))

