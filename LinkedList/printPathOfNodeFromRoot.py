"""
Print path from root to a given node in a binary tree
Given a binary tree with distinct nodes(no two nodes have the same have data values).
The problem is to print the path from root to a given node x. If node x is not present then print “No Path”.

Examples:

Input :          1
               /   \
              2     3
             / \   /  \
            4   5  6   7

               x = 5

Output : 1->2->5
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

root = Node(1)
root.right = Node(3)
root.left = Node(2)
root.left.right = Node(5)
root.left.left = Node(4)
root.right.right = Node(7)
root.right.left = Node(6)

def printPath(root, key):
    n = []
    if _allNode(root, key, n):
        for i in n:
            print(i, end=" ")
    else:
        print("No Path")

def _allNode(root, key, n):
    if root:
        n.append(root.key)
        if root.key == key:
            return True

        if _allNode(root.left, key, n) or _allNode(root.right, key, n):
            return True

        n.pop(-1)

# printPath(root, 5)

"""
Input :         100
               /    \
              60     130
             / \     /  \
            30  70  120  170
                /    /
              11  110
               x = 110           
"""
root = Node(100)
root.left = Node(60)
root.right = Node(130)
root.left.left = Node(30)
root.left.right = Node(70)
root.right.left = Node(120)
root.right.right = Node(170)
root.right.left.left = Node(110)
root.left.right.left = Node(11)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# inorder(root)
# print()
printPath(root, 11)
