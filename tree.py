# A Nodes structure
class Node:
    def __init__(self, data):
        self.data = data
        self.Lchild = None
        self.Rchild = None
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, data):
    # if the child is less than or equal to parent we add it to the left
        def left_child(parent, data):
            if not parent.Lchild :
                new_node = Node(data)
                parent.Lchild = new_node
                new_node.parent = parent
                new_node.Lchild = None
                new_node.Rchild = None
            elif parent.Lchild :
                parent = parent.Lchild
                if data <= parent.data:
                    left_child(parent, data)
                else:
                    right_child(parent, data)
        # else we add to the right
        def right_child(parent, data):
            if not parent.Rchild:
                new_node = Node(data)
                parent.Rchild = new_node
                new_node.parent = parent
                new_node.Lchild = None
                new_node.Rchild = None
            elif parent.Rchild:
                parent = parent.Rchild
                if data <= parent.data:
                    left_child(parent, data)
                else:
                    right_child(parent, data)
        if self.root == None:
            self.root = Node(data)
        else:
            parent = self.root
            if data <= parent.data:
                left_child(parent, data)
            else:
                right_child(parent, data)

    # print data in order (ascending order)
    def inorderTraversal(self):
        def _inorder(root):
            if root == None:
                return
            if root:
                _inorder(root.Lchild)
                print(root.data)
                _inorder(root.Rchild)
        print("Empty tree\n") if self.root == None else _inorder(self.root)

    # print data in preorder (parent->leftchild->rightchild)
    def preorderTraversal(self):
        def _preorder(root):
            if root == None:
                return
            if root:
                print(root.data)
                _preorder(root.Lchild)
                _preorder(root.Rchild)
        print("Empty tree \n") if self.root == None else _preorder(self.root)

    # Delete a node
    def delete_node(self, target):
        deleted = True
        children_nodes = []
    
        def travers(root):
            _add_to_list(root)

        def _add_to_list(root):
            if root:
                _add_to_list(root.Lchild)
                children_nodes.append(root.data)# Travers through the sub-tree adding the nodes in a list
                _add_to_list(root.Rchild)

        def search_target(node, target):
            if node:# use inorder traversal to find the target
                search_target(node.Lchild, target)
                if node.data == target: #when the target is found we remove the link from its parent pointing to it.
                    parent = node.parent
                    if parent.data <= node.data:
                        parent.Rchild = None
                    elif parent.data > node.data:
                        parent.Lchild = None
     
                    travers(node)
                search_target(node.Rchild, target)
        #Deleting the root element
        if target == self.root.data:
            travers(self.root) # add all the nodes in a list
            children_nodes.pop(children_nodes.index(self.root.data))#remove the root from the list
            self.root = None #set the root to none
            for data in children_nodes:
                self.add_node(data)# re add all the nodes to create a new tree without the root data(target)
            deleted = True
            return
        #search for the target
        search_target(self.root, target)
        try:
            children_nodes.pop(children_nodes.index(target))#remove the target from the list
        except ValueError:
            deleted = False
        for data in children_nodes: #Re-add the sub-tree back to the tree without the target
            self.add_node(data)

        print(f"{target} deleted successfully!")if deleted else print(f"Error: {target} not found!")
        

#Create a Binarytree object
tree = BinaryTree()
def add_data():
    data = input("add data: ")
    try:
        data = int(data)
    except ValueError:
        print("Use integer values")
    tree.add_node(data)

# print the list
def display_list():
    print("use :1 for inorder or :2 for preorder")
    order = input("--: ")
    try:
        order = int(order)
    except ValueError:
        print("Use no 1 or 2")
    if order == 1:
        tree.inorderTraversal()
    elif order == 2:
        tree.preorderTraversal()
    
# remove the data from list
def delete_data():
    target = input("Enter target : ")
    try:
        target = int(target)
    except ValueError:
        print("Use integer values")
    tree.delete_node(target)

isRunning = True
while isRunning:
    print("\nMenu")
    print("0. exit")
    print("1. add data")
    print("2. print list")
    print("3. delete node")
    choice = input("--: ")
    try:
        choice = int(choice)
    except ValueError:
        print("enter either:0 ,1, 2, 3")
    match(choice):
        case 0:
            isRunning = False
        case 1:
            add_data()
        case 2:
            display_list()
        case 3:
            delete_data()
