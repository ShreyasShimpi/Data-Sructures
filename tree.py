class Treenode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def level(self):
        level = 0
        itr = self.parent
        while itr:
            level += 1
            itr = itr.parent

        return level
    
    def print(self):
        x = "   "*self.level() + "-"
        print(x + self.data)
        for child in self.children:
            child.print()
            
def b_p_t():
    root = Treenode("Electronics")
    
    laptop = Treenode("Laptop")
    laptop.add_child(Treenode("HP"))
    laptop.add_child(Treenode("Mac"))
    laptop.add_child(Treenode("Dell"))

    TV = Treenode("TV")
    TV.add_child(Treenode("LG"))
    TV.add_child(Treenode("Sony"))
    TV.add_child(Treenode("MI"))

    Phone = Treenode("Phone")
    Phone.add_child(Treenode("Iphone"))
    Phone.add_child(Treenode("Samsung"))
    
    root.add_child(laptop)
    root.add_child(TV)
    root.add_child(Phone)
    
    return root

if __name__ == "__main__":
    root = b_p_t()
    root.print()
