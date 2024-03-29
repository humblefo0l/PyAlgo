"""
21. Merge Two Sorted Lists
Easy

12677

1154

Add to List

Share
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        p1 = p2 = ListNode()

        while list1 and list2:

            if list1.val < list2.val:
                p1.next = list1
                p1 = list1
                list1 = list1.next
            else:
                p1.next = list2
                p1 = list2
                list2 = list2.next

        if list1 or list2:
            p1.next = list1 if list1 else list2

        return p2.next

# list1 = [1,2,4]
# list2 = [1,3,4]

def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
printList(list1)
print("\n====")

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
printList(list2)
print("\n====")

s = Solution()
printList(s.mergeTwoLists(list1, list2))
