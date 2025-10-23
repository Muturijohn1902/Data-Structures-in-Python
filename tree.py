
class Node:
    def __init__(self, data):
        self.data = data
        self.Lchild = None
        self.Rchild = None
        self.parent = None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)

    def add_node(self, data):
        parent = self.root
        if data <= parent.data:
            self.left_child(parent, data)
        else:
            self.right_child(parent, data)

    def left_child(self, parent, data):
        if not parent.Lchild :
            new_node = Node(data)
            parent.Lchild = new_node
            new_node.parent = parent
            new_node.Lchild = None
            new_node.Rchild = None
        elif parent.Lchild :
            parent = parent.Lchild
            if data <= parent.data:
                self.left_child(parent, data)
            else:
                self.right_child(parent, data)

    def right_child(self, parent, data):
        if not parent.Rchild:
            new_node = Node(data)
            parent.Rchild = new_node
            new_node.parent = parent
            new_node.Lchild = None
            new_node.Rchild = None
        elif parent.Rchild:
            parent = parent.Rchild
            if data <= parent.data:
                self.left_child(parent, data)
            else:
                self.right_child(parent, data)

    def inorderTraversal(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root == None:
            return
        if root:
            self._inorder(root.Lchild)
            print(root.data)
            self._inorder(root.Rchild)

    def preorderTraversal(self):
        self._preorder(self.root)

    def _preorder(self, root):
        if root == None:
            return
        if root:
            print(root.data)
            self._preorder(root.Lchild)
            self._preorder(root.Rchild)


tree = BinaryTree(10)
tree.add_node(5)
tree.add_node(15)
tree.add_node(2)
tree.add_node(7)

print("Inorder:")
tree.inorderTraversal()

print("Preorder:")
tree.preorderTraversal()
