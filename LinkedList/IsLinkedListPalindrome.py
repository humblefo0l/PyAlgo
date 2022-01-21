"""
Function to check if a singly linked list is palindrome

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def isPalindrome(node):

    l = 0
    temp = node
    while temp:
        l+=1
        temp = temp.next
    print()
    c =0
    temp = node
    while c <= l//2:
            temp = temp.next
        c +=1

    print(temp.data)

def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next


ll = Node(1)
ll.next = Node(2)
ll.next.next = Node(3)
ll.next.next.next = Node(4)
ll.next.next.next.next = Node(5)

printList(ll)
# printList(ll)
isPalindrome(ll)
