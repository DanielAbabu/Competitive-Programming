class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head

        while index:
            current = current.next
            index-=1

        return current.val

    def addAtHead(self, val: int) -> None:

        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:

        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        current = self.head
        new_node = ListNode(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            while index-1:
                current = current.next
                index-=1
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            while index-1:
                current = current.next
                index -=1
            current.next = current.next.next

        self.size -= 1