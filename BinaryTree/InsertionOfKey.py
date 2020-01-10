"""
Insertion of a key
A new key is always inserted at leaf. We start searching a key from root till we hit a leaf node.
Once a leaf node is found, the new node is added as a child of the leaf node.

         100                               100
        /   \        Insert 40            /    \
      20     500    --------->          20     500
     /  \                              /  \
    10   30                           10   30
                                              \
                                              40


Illustration to insert 2 in below tree:
1. Start from root.
2. Compare the inserting element with root, if less than root, then recurse for left, else recurse for
    right.
3. After reaching end,just insert that node at left(if less than current) else right.

Time Complexity: The worst case time complexity of search and insert operations is O(h) where h is
height of Binary Search Tree. In worst case, we may have to travel from root to the deepest leaf node.
The height of a skewed tree may become n and the time complexity of search and insert operation may become
O(n).

"""


class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


def insert(root, node):
    if root is None:
        root = node
    else:
        if node.key > root.key:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)


r = Node(50)
insert(r,Node(30))
insert(r,Node(20))
insert(r,Node(40))
insert(r,Node(70))
insert(r,Node(60))

inorder(r)

















