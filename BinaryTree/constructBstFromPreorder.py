"""
Construct BST from given preorder traversal | Set 1
Given preorder traversal of a binary search tree, construct the BST.

For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be root of following tree.
     10
   /   \
  5     40
 /  \      \
1    7      50
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def getBiggerNumber(arr, key):

    for i in range(len(arr)):
        if key < arr[i]:
            return i

def constructBST(arr):
    root = None
    if arr:
        root = arr[0]
        arr.pop(0)
        i = getBiggerNumber(arr, root)
        root = Node(root)
        if i:
            root.left = constructBST(arr[:i])
            root.right = constructBST(arr[i:])
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

a = [15, 10, 8, 12, 20, 16, 25]
bst = constructBST(a)
inorder(bst)