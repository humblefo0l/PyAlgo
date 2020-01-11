"""
Clone a linked list with next and random pointer | Set 1
You are given a Double Link List with one pointer of each node pointing to the next node just like in a
single link list. The second pointer however CAN point to any node in the list and not just the previous
node. Now write a program in O(n) time to duplicate this list. That is, write a program which will create
a copy of this list.

Let us call the second pointer as arbit pointer as it can point to any arbitrary node in the linked
list.

The idea is to use Hashing. Below is algorithm.
1. Traverse the original linked list and make a copy in terms of data.
2. Make a hash map of key value pair with original linked list node and copied linked list node.
3. Traverse the original linked list again and using the hash map adjust the next and random reference
of cloned linked list nodes.

"""

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.random = None


def pList(c):
    while c:
        print(c.key,'-->' ,end=" ")
        if c.random:
            print(c.random.key)
        else:
            print(None)
        c = c.next

def clone(head):
    """
    This method will clone the given list
    :return:
    """
    # Cloning and storing in dictionary
    c = head
    d = {}

    while c:
        cn = Node(c.key)
        d[c] = cn
        c = c.next

    # Iterating over the list again
    c = head

    while c:
        next = c.next
        random = c.random

        if next:
            d[c].next = d[next]
        else:
            d[c].next = None

        if random:
            d[c].random = d[random]

        c = c.next

    return d[head]

if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    n1.next = n2
    n1.random = n4
    n2.next = n3
    n3.next = n4
    n3.random = n1
    n4.next = n5
    n4.random = n6
    n5.next = n6
    n5.random = n2
    n6.next = None

    head = n1
    pList(head)
    print()
    #########
    ch = clone(head)
    pList(ch)
