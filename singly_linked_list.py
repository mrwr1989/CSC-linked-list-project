
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def append(self, value):
        new_node = Node(value)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._count += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node

        if self._tail is None:
            self._tail = new_node

        self._count += 1

    def is_empty(self):
        return self._count == 0

    def __len__(self):
        return self._count

    def __iter__(self):
        current = self._head

        while current is not None:
            yield current.data
            current = current.next

    def __str__(self):
        values = " -> ".join(str(value) for value in self)
        if values:
            return "Head -> " + values + " -> None"
        return "Head -> None"
