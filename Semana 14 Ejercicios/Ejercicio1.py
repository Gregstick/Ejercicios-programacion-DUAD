class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    top: Node

    def __init__(self, top=None):
        self.top = top

    def print_structure(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

class Stack(LinkedList):
    def push(self, data):
        new_node = Node(data, next=self.top)
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack vacio")
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node


stack = Stack()
stack.push("A")
stack.push("B")
stack.push("C")

stack.print_structure()

removed = stack.pop()
print(f"Elemento eliminado: {removed.data}")

stack.print_structure()

