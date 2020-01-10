"""
Swap nodes in a linked list without swapping data
Given a linked list and two keys in it, swap nodes for two given keys.
Nodes should be swapped by changing links. Swapping data of nodes may be
expensive in many situations when data contains many fields.
It may be assumed that all keys in linked list are distinct.

Examples:

Input:  10->15->12->13->20->14,  x = 12, y = 20
Output: 10->15->20->13->12->14

Input:  10->15->12->13->20->14,  x = 10, y = 20
Output: 20->15->12->13->10->14

Input:  10->15->12->13->20->14,  x = 12, y = 13
Output: 10->15->13->12->20->14
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def swapData(self, d1, d2):
        p1 = p2 = None

        current = self.head

        while current:
            if current.next and current.next.data == d1:
                p1 = current

            if current.next and current.next.data == d2:
                p2 = current

            current = current.next

        t1 = p1.next
        t2 = p2.next

        p1.next, p2.next = p2.next, p1.next
        t1.next, t2.next = t2.next, t1.next


ll = LinkedList()
ll.push(7)
ll.push(6)
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
ll.printList()
ll.swapData(3, 5)
ll.printList()
