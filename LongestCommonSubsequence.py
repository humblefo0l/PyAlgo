"""
Longest Common Subsequence | DP-4
LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them. A
subsequence is a sequence that appears in the same relative order, but not necessarily contiguous. For example,
“abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. So a string of length n has 2^n
different possible subsequences.

It is a classic computer science problem, the basis of diff (a file comparison program that outputs the
differences between two files), and has applications in bioinformatics.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.


"""


def longestCommonSubSeq(string1, string2):
    """
    Deatil Soruce: https://www.youtube.com/watch?v=NnD96abizww

    :param string1:
    :param string2:
    :return:
    """

    string1 = [i for i in string1]
    string2 = [i for i in string2]
    string1_length = len(string1)
    string2_length = len(string2)

    dp = [[0 for i in range(string1_length+1)] for j in range(string2_length+1)]
    ms = ''
    for i in range(string1_length):
        for j in range( string2_length):
            # print("i-{}, j-{}, s1[i]-{}, s2[j]-{}".format(i,j,string1[i], string2[j]))
            if string1[i] == string2[j]:
                if (i-1) >= 0 and (j-1) >=0:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + dp[0][0]
                ms += string1[i]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            # print('dp[i][j]-{}'.format(dp[i][j]))
            # print()

    # print(dp)
    # print(set(ms))
    return dp[string1_length-1][string2_length-1]


def longestCommonSubSeqDP(string1, string2, m, n):
    if m == 0 or n == 0:
        return 0

    if string1[m-1] == string2[n-1]:
        return 1 + longestCommonSubSeqDP(string1, string2, m-1, n-1)

    return max(longestCommonSubSeqDP(string1, string2, m-1, n),
               longestCommonSubSeqDP(string1, string2, m, n-1))


if __name__ == '__main__':

    string1 = "ABCDGH"
    string2 = "AEDFHR"
    print(longestCommonSubSeq(string1, string2))

    s1 = [ x for x in string1]
    s2 = [ x for x in string2]
    m = len(s1)
    n = len(s2)
    print(longestCommonSubSeqDP(s1, s2, m, n))

    print('============')
    string1 = "AGGTAB"
    string2 = "GXTXAYB"
    print(longestCommonSubSeq(string1, string2))
    s1 = [x for x in string1]
    s2 = [x for x in string2]
    m = len(s1)
    n = len(s2)
    print(longestCommonSubSeqDP(s1, s2, m, n))

    print('============')
    string1 = "sdjnksjdnvsdkjnv"
    string2 = "ksdjbvksldbvklsf"
    print(longestCommonSubSeq(string1, string2))
    s1 = [x for x in string1]
    s2 = [x for x in string2]
    m = len(s1)
    n = len(s2)
    print(longestCommonSubSeqDP(s1, s2, m, n))

