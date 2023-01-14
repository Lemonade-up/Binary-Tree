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
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data

    def calculate_sum(self):
        if self.left:
            leftsum = self.left.calculate_sum()
        else:
            leftsum = 0
        if self.right:
            rightsum = self.right.calculate_sum()
        else:
            rightsum = 0
        
        return leftsum + rightsum + self.data


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
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        if val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        
        else:    
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            minval = self.right.find_min()
            self.data = minval
            self.right = self.right.delete(minval)

        return self
        
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
    numbers = [19, 13, 19, 38, 1, 27, 8, 15, 16, 50, 12]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.search(1))
    print(numbers_tree.search(50))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.calculate_sum())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())

    numbers_kree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_kree.delete(17)
    print("After deleting 17 ",numbers_kree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]