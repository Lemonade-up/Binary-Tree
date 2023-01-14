class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)    

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range( 1, len(elements)):
        root.add_child(elements[i])
        
    return root

if __name__ == '__main__':
    fullname = input("Fullname: ")
    namecon = []
    for i in range(0 , len(fullname)):
        namecon.append(fullname[i])
    name_tree = build_tree(namecon)
    print(name_tree.in_order_traversal())
    print(name_tree.pre_order_traversal())
    print(name_tree.post_order_traversal())

