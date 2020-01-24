"""
Reverse a Singly Linked List
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLinkedList(node):

    previous = None
    current = node

    while current:

        temp = current.next
        current.next = previous
        previous = current
        current = temp

    return previous



def pLinkedList(node):
    c = node

    while c:
        print(c.data, end=" ")
        c=c.next
    print()


if __name__ == '__main__':
    ll = Node(1)
    ll.next = Node(2)
    ll.next.next = Node(3)
    ll.next.next.next = Node(4)
    ll.next.next.next.next = Node(5)

    pLinkedList(ll)
    rl = reverseLinkedList(ll)
    pLinkedList(rl)
