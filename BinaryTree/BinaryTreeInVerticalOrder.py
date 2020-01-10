"""
Print a Binary Tree in Vertical Order | Set 1
Given a binary tree, print it vertically. The following example illustrates vertical order traversal.
           1
        /    \
       2      3
      / \    / \
     4   5  6   7
             \   \
              8   9


The output of print this tree vertically will be:
4
2
1 5 6
3 8
7
9
"""
class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.level = None

def verticalOrder(root):
    root.level = 0
    q = [root]
    d = {}
    while q:
        node = q.pop(0)

        if node.level in d:
            d[node.level].append(str(node.key))
        else:
            d[node.level] = [str(node.key)]

        if node.left:
            node.left.level = node.level - 1
            q.append(node.left)

        if node.right:
            node.right.level = node.level + 1
            q.append(node.right)


    for key in sorted(d):
        print(" ".join(d[key]))
        # for i in d[key]:
        #     print(i, end=" ")
        # print()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

verticalOrder(root)