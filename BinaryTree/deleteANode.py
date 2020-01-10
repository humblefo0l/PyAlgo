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
    return root


def minValueNode(node):
    current = node

    while current.left:
        current = current.left

    return current



def deleteNode(root, key):

    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)

    elif key > root.key:
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minValueNode(root.right)

        root.key = temp.key

        root.right = deleteNode(root.right, temp.key)

    return root





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
print('======')
deleteNode(r, 50)
inorder(r)

