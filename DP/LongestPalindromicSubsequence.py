"""
Longest Palindromic Subsequence | DP-12
Given a sequence, find the length of the longest palindromic subsequence in it.

longest-palindromic-subsequence

As another example, if the given sequence is “BBABCBCAB”, then the output should be 7 as
“BABCBAB” is the longest palindromic subseuqnce in it. “BBBBB” and “BBCBB” are also palindromic
subsequences of the given sequence, but not the longest ones.

The naive solution for this problem is to generate all subsequences of the given sequence and find the
longest palindromic subsequence. This solution is exponential in term of time complexity. Let us see how
this problem possesses both important properties of a Dynamic Programming (DP) Problem and can
efficiently solved using Dynamic Programming.

1) Optimal Substructure:
Let X[0..n-1] be the input sequence of length n and L(0, n-1) be the length of the longest
palindromic subsequence of X[0..n-1].

If last and first characters of X are same, then L(0, n-1) = L(1, n-2) + 2.
Else L(0, n-1) = MAX (L(1, n-1), L(0, n-2)).
"""


def lps(seq, start, end):
    if start == end:
        return 1

    if start >= len(seq) or end < 0:
        return 0

    if seq[start] == seq[end] and (start +1 == end):
        return 2

    if seq[start] == seq[end]:
        return 2 +lps(seq, start+1, end-1)

    else:
        return max(lps(seq, start+1, end), lps(seq, start, end-1))


def lpsDP(seq, start, end, memo):

    if (start, end) in memo:
        return memo[(start, end)]

    if start == end:
        return 1

    elif seq[start] == seq[end] and start+1 == end:
        return 2

    elif seq[start] == seq[end] :
        memo[(start, end)] = 2 + lpsDP(seq, start+1, end-1, memo)
        return memo[(start, end)]

    else:

        memo[(start, end)] = max(lpsDP(seq, start+1, end, memo), lpsDP(seq, start, end-1, memo))
        return memo[(start, end)]



if __name__ == '__main__':

    seq = "ABA"
    seq = [i for i in seq]
    n = len(seq)
    memo={}
    print("The length of the LPS is", lps(seq, 0, n - 1))
    print("The length of the LPS is", lpsDP(seq, 0, n - 1, memo))

    seq = "GEEKSFORGEEKS"
    seq = [i for i in seq]
    n = len(seq)
    memo={}
    print("The length of the LPS is", lps(seq, 0, n - 1))
    print("The length of the LPS is", lpsDP(seq, 0, n - 1, memo))

    seq = "GEEKS FOR GEEKS"
    seq = [i for i in seq]
    n = len(seq)
    memo={}
    print("The length of the LPS is", lps(seq, 0, n - 1))
    print("The length of the LPS is", lpsDP(seq, 0, n - 1, memo))
