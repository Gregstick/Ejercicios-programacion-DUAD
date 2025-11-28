class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def print_structure(self):
        if self.root is None:
            print("Árbol vacío")

        current = self.root

        print(current.data)

        left_child = current.left
        right_child = current.right

        if left_child is not None:
            print(left_child.data)
        if right_child is not None:
            print(right_child.data)

        current = left_child  
        while current is not None:
            if current.left is not None:
                print(current.left.data)
            if current.right is not None:
                print(current.right.data)
            
            break

        current = right_child  
        while current is not None:
            if current.left is not None:
                print(current.left.data)
            if current.right is not None:
                print(current.right.data)
            break


A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")
F = TreeNode("F")

A.left = B
A.right = C
B.left = D
B.right = E
C.right = F

tree = BinaryTree(A)

tree.print_structure()