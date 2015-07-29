__author__ = 'sjoseph4'

from random import randint


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, value):

        node = Node(value)
        # if the old list is none, set new node as the first node
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def __str__(self):

        if self.head :
            index = self.head
            nodelist = [str(index.value)]
            while index.next :
                index = index.next
                nodelist.append(str(index.value))
            return  "->".join(nodelist)

    # remove the first node that have the same value as the given node_value

    def removeNode(self, value):
        current = self.head
        if current.value == value:
            self.head = self.head.next
        else:
            while current.next:
                if current.next.value == value:
                    if current.next == self.tail:
                        self.tail = current
                    current.next = current.next.next
                    break
                else:
                    current = current.next


def remove_duplicates(linkedlist):

    buffer=set()
    current = linkedlist.head

    if current:
        buffer.add(current.value)

        while current.next:

            if current.next.value in buffer:
                if current.next == linked_list.tail:
                    linked_list.tail = current
                current.next = current.next.next
            else:
                buffer.add(current.next.value)
                current = current.next


linked_list = LinkedList()

values = [3,5,3,1,4,15,9,3,6,3,15]

for v in values:
    linked_list.addNode(v)
print(linked_list)

remove_duplicates(linked_list)
print(linked_list.tail)
linked_list.addNode(7)
print(linked_list)

