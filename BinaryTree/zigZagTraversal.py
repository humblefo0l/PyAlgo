"""
ZigZag Tree Traversal
Write a function to print ZigZag order traversal of a binary tree. For the below binary tree the

             1
           /   \
        2       3
      /  \     / \
    4     5  6    7
zigzag order traversal will be 1 3 2 7 6 5 4

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def zizagtraversal(root):

    s1 = []
    s2 = []
    s1.append(root)
    while s1 or s2:

        while s1:
            #if S1, insert L , then R into S2
            c = s1.pop(-1)
            s2 = ins(s2, c.left)
            s2 = ins(s2, c.right)
            print(c.data, end=" ")
        while s2:
            # if S2, insert R then L into S1
            c = s2.pop(-1)
            s1 = ins(s1, c.right)
            s1 = ins(s1, c.left)
            print(c.data, end=" ")


def ins(s, side):
    if side:
        s.append(side)
    return s




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
print("Zigzag Order traversal of binary tree is")
zizagtraversal(root)