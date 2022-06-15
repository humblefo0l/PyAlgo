"""
234. Palindrome Linked List
Easy

9212

567

Add to List

Share
Given the head of a singly linked list, return true if it is a palindrome.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    start = mid = end = head

    while end and end.next:
        mid = mid.next
        end = end.next.next

    center = mid = reverseList(mid)

    while mid:
        if mid.val != start.val:
            return False
        mid = mid.next
        start = start.next

    reverseList(center)
    return True


def reverseList(head):

    prevNode = None
    while head:
        nextNode = head.next
        head.next = prevNode
        prevNode = head
        head = nextNode

    head = prevNode
    return head


def printLinkedList(head):
    while head:
        print(head.val, end=" ")
        head = head.next




# head = [1,2,2,1]
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(2)
h.next.next.next = ListNode(1)

print(isPalindrome(h))
# print()
# h = reverseList(h)
# print()
# printLinkedList(h)

# print(isPalindrome(h))
