"""
Find distance from root to given node in a binary tree
Given root of a binary tree and a key x in it, find distance of the given key from
root. Dis­tance means num­ber of edges between two nodes.

Examples:

Input : x = 45,
        Root of below tree
        5
      /    \
    10      15
    / \    /  \
  20  25  30   35
       \
       45
Output : Distance = 3
There are three edges on path
from root to 45.

For more understanding of question,
in above tree distance of 35 is two
and distance of 10 is 1.
"""

class newNode:
    def __init__(self, item):
        self.data = item
        self.left = self.right = None

def findDistance(root, n):
    return _findDistance(root, n, 0)

def _findDistance(root, n, c):
    if root:
        if root.data == n:
            return c

        else:
            a = _findDistance(root.left, n, c+1)
            b = _findDistance(root.right, n, c+1)

            if b:
                return b
            else:
                return a


root = newNode(5)
root.left = newNode(10)
root.right = newNode(15)
root.left.left = newNode(20)
root.left.right = newNode(25)
root.left.right.right = newNode(45)
root.right.left = newNode(30)
root.right.right = newNode(35)

print(findDistance(root, 45))