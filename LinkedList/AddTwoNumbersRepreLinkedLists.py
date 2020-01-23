"""
Add two numbers represented by linked lists | Set 1
Given two numbers represented by two lists, write a function that returns the sum list. The sum list is
list representation of the addition of two input numbers.
Example:

Input: List1: 5->6->3  // represents number 365
       List2: 8->4->2 //  represents number 248
Output: Resultant list: 3->1->6  // represents number 613


Input: List1: 7->5->9->4->6  // represents number 64957
       List2: 8->4 //  represents number 48
Output: Resultant list: 5->0->0->5->6  // represents number 65005
"""

class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def getHead(self):
        return self.head

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=""),
            temp = temp.next


def addTwoLists(first, second):
    # import pdb; pdb.set_trace()
    fir = first
    sec = second
    cc = None
    ts = ''


    while fir and sec:
        a = fir.data
        b = sec.data
        ss = a + b

        if cc:
            import pdb;pdb.set_trace()
            ss += cc
            cc = None

        if ss >= 10:
            ld = ss % 10
            cc = ss // 10
            import pdb;pdb.set_trace()

            ts += str(ld)
            fir = fir.next
            sec = sec.next
            continue

        ts += str(ss)
        fir = fir.next
        sec = sec.next

    print(ts)



first = LinkedList()
second = LinkedList()
first.push(5)
first.push(2)
first.push(6)

second.push(5)
second.push(4)
second.push(2)

first.printList()
print()
second.printList()
print()

addTwoLists(first.getHead(), second.getHead())
