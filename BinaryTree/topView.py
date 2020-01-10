"""
You are given a pointer to the root of a binary tree. Print the top view of the binary tree.
Top view means when you look the tree from the top the nodes, what you will see will be called the top view of the tree. See the example below.
You only have to complete the function.
For example :

   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
Top View : 1 -> 2 -> 5 -> 6

Input Format

You are given a function,

void topView(node * root) {

}
Constraints

1 Nodes in the tree  500

Output Format

Print the values on a single line separated by space.

Sample Input

   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
Sample Output

1 2 5 6

Explanation

   1
    \
     2
      \
       5
      /  \
     3    6
      \
       4
From the top only nodes 1,2,5,6 will be visible.

"""

class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.level = None


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
        print(root.key, end=" ")
        inorder(root.right)


def topView(root):
    root.level = 0
    d = {}
    q = [root]

    while q:

        n = q.pop(0)

        if n.level not in d:
            d[n.level] = str(n.key)

        if n.right:
            n.right.level = n.level - 1
            q.append(n.right)

        if n.left:
            n.left.level = n.level + 1
            q.append(n.left)

    for k in reversed(sorted(d)):
        print(d[k], end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

topView(root)

