class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
             return
            
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTree(data)

    def inorder(self):
        elements = []
        if self.left:
            elements.append(self.left.inorder())
            
        elements.append(self.data)
        
        if self.right:
            elements.append(self.right.inorder())
            
        return elements
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    def min(self):
        if self.left is None:
            return self.data
        return self.left.min()
    
    def max(self):
        if self.right is None:
            return self.data
        return self.right.max()
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
                
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
                
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min1 = self.right.min()
            self.data = min1
            self.right.delete(min1)

        return self
        
    
def build(elements):
    root = BinaryTree(elements[0])
    
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root
        

if __name__ == "__main__":
    n = [17, 4, 1, 20, 9, 23, 18, 34]
    tree = build(n)
    tree.delete(20)
    print(tree.inorder())
    ## sum , min, max, pre, post
    
        
