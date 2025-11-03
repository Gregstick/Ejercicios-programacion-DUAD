class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_node = Node(data, prev=None, next=self.head)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node

    def push_right(self, data):
        new_node = Node(data, prev=self.tail, next=None)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            print("Deque vacío")
            return None
        removed_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return removed_node.data

    def pop_right(self):
        if self.tail is None:
            print("Deque vacío")
            return None
        removed_node = self.tail
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return removed_node.data

    def print_structure(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

dq = Deque()
dq.push_left("B")
dq.push_left("A")
dq.push_right("C")
dq.push_right("D")
dq.print_structure()
print("Se eliminó:", dq.pop_left())
dq.print_structure()
print("Se eliminó:", dq.pop_right())
dq.print_structure()




