"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"


Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    start = 0
    end = 0
    length = 0

    def longestPalindrome(self, s: str) -> str:
        i = 0
        j = len(s)

        self._longesgPalindrome(s, i, j-1)

        print(F"Longest palindrome length is: {self.length}")
        print(F"Longest palindrome substring is: {s[self.start:self.end+1]}")

        return s[self.start: self.end+1]

    def _longesgPalindrome(self, s, i, j):
        if self.isPal(s, i, j):
            if j - i +1 > self.length:
                self.start = i
                self.end = j
                self.length = j - i +1
        else:
            self._longesgPalindrome(s, i+1, j)
            self._longesgPalindrome(s, i, j-1)

    def isPal(self, s, i, j):

        if i == j:
            return True

        if i > j:
            return False

        # Only 2 chars
        if i+1 == j:
            if s[i] == s[j]:
                return True
            else:
                return False
        else:
            if s[i] == s[j]:
                return self.isPal(s, i+1, j-1)

        return False


class SolutionDP:
    start = 0
    end = 0
    length = 0
    def __init__(self):
        self.dp = None

    def longestPalindrome(self, s: str) -> str:
        i = 0
        j = len(s)
        self.dp = [[-1 for a in range(j)] for b in range(j)]

        self._longesgPalindrome(s, i, j-1)

        print(F"Longest palindrome length is: {self.length}")
        print(F"Longest palindrome substring is: {s[self.start:self.end+1]}")

        return s[self.start: self.end+1]

    def _longesgPalindrome(self, s, i, j):
        if self.isPal(s, i, j):
            self.dp[i][j] = 1
            if j - i +1 > self.length:
                self.start = i
                self.end = j
                self.length = j - i +1
        else:
            self.dp[i][j] = 0
            self._longesgPalindrome(s, i+1, j)
            self._longesgPalindrome(s, i, j-1)

    def isPal(self, s, i, j):

        if self.dp[i][j] >= 0:
            return self.dp[i][j]

        if i == j:
            self.dp[i][j] = 1
            return True

        if i > j:
            self.dp[i][j] = 0
            return False

        # Only 2 chars
        if i+1 == j:
            if s[i] == s[j]:
                self.dp[i][j] = 1
                return True
            else:
                self.dp[i][j] = 0
                return False

        else:
            if s[i]== s[j]:
                res = self.isPal(s, i+1, j-1)
                self.dp[i][j] = 1 if res else 0
                return res

        self.dp[i][j] = 0
        return False


def printSubStr(str, low, high):
    for i in range(low, high + 1):
        print(str[i], end="")

def longestPalSubstr(str):
    # Get length of input String
    n = len(str)

    # All subStrings of length 1
    # are palindromes
    maxLength = 1
    start = 0

    # Nested loop to mark start
    # and end index
    for i in range(n):
        for j in range(i, n):
            flag = 1

            # Check palindrome
            for k in range(0, ((j - i) // 2) + 1):
                if (str[i + k] != str[j - k]):
                    flag = 0

            # Palindrome
            if (flag != 0 and (j - i + 1) > maxLength):
                start = i
                maxLength = j - i + 1

    print("Longest palindrome subString is: ", end="")
    printSubStr(str, start, start + maxLength - 1)

    # Return length of LPS
    return maxLength


# A O(n ^ 2) time and O(1) space program to find the
# longest palindromic substring

# This function prints the longest palindrome substring (LPS)
# of str[]. It also returns the length of the longest palindrome

#
# def longestPalSubstr(string):
#     maxLength = 1
#
#     start = 0
#     length = len(string)
#
#     low = 0
#     high = 0
#
#     # One by one consider every character as center point of
#     # even and length palindromes
#     for i in range(1, length):
#         # Find the longest even length palindrome with center
#         # points as i-1 and i.
#         low = i - 1
#         high = i
#         while low >= 0 and high < length and string[low] == string[high]:
#             low -= 1
#             high += 1
#
#         # Move back to the last possible valid palindrom substring
#         # as that will anyway be the longest from above loop
#         low += 1
#         high -= 1
#         if string[low] == string[high] and high - low + 1 > maxLength:
#           start = low
#           maxLength = high - low + 1
#
#         # Find the longest odd length palindrome with center
#         # point as i
#         low = i - 1
#         high = i + 1
#         while low >= 0 and high < length and string[low] == string[high]:
#             low -= 1
#             high += 1
#
#         # Move back to the last possible valid palindrom substring
#         # as that will anyway be the longest from above loop
#         low += 1
#         high -= 1
#         if string[low] == string[high] and high - low + 1 > maxLength:
#           start = low
#           maxLength = high - low + 1
#
#     print(F"Longest palindrome substring is: {string[start:start + maxLength]}")
#     return maxLength



if __name__ == '__main__':
    import time
    st = "babadabxxxxxyxxxxx"
    st = "forgeeksskeegforgggghhhhghghghghghgggghhhhghghghghgh"
    #
    # sol = Solution()
    # start_time = time.time()
    # sol.longestPalindrome(st)
    # stop1=time.time() - start_time
    # print(F"\nTime taken by Recursive solution is: {time.time() - start_time}")
    #
    # print()
    # # DP
    # start_time = time.time()
    # solDP = SolutionDP()
    # solDP.longestPalindrome(st)
    # print(F"\nTime taken by DP solution is: {time.time() - start_time}")

    # gfg
    start_time = time.time()
    longestPalSubstr(st)
    stop2 = time.time() - start_time
    print(F"\nTime taken by GFG solution is: {stop2}")

    # fn = stop2 > stop1
    # print(F"stop2 > stop1: {fn}")