"""
20. Valid Parentheses
Easy

13530

611

Add to List

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

"""

def isValid( s: str) :
    d = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    stk = []

    for i in s:
        if i in d:
            if not stk:
                return False
            l = stk.pop()
            if d[i] != l:
                return False
        else:
            stk.append(i)

    # print('====')
    # print(stk)

    return stk == []


s = "()[]{}"
print(isValid(s))

s = "(]"
print(isValid(s))