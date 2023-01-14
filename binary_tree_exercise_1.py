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
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data


    def search(self, val):
        if self.data == val:
            return True
        if val < self.data: #left tree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data: #right tree
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

        
def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])
    for i in range( 1, len(elements)):
        root.add_child(elements[i])
        
    return root

if __name__ == '__main__':
    numbers = [19, 13, 19, 38, 1, 27, 8, 15, 16, 50, 12]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(1))
    print(numbers_tree.search(50))
    print(numbers_tree.find_min())
