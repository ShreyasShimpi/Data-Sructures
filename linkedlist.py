class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_b(self, data):
        node = Node(data, self.head)
        self.head = node
        
    def insert_e(self, data):
        if self.head is None:
            self.head= Node(data)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_e(data)
            
    def length(self):
        itr = self.head
        counter = 0
        while itr:
            counter += 1
            itr = itr.next
            
        return counter

    def remove(self, index):
        if index<0 or index >= self.length():
            print("Invalid index")
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        count  =0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count += 1
            
    def insert(self, data, index):
        if index<0 or index >= self.length():
            print("Invalid index")
            return
        
        if index == 0:
            self.insert_b()
            return
        
        count  =0
        itr = self.head
        while itr:
            if count == index - 1:
                temp = Node(data, itr.next)
                itr.next = temp
                break
            
            itr = itr.next
            count += 1
          
    def print(self):
        if self.head is None:
            print("Linked list i empty.")
            return
          
        itr = self.head
        ll = ""
        while itr:
            ll += str(itr.data) + "---"
            itr = itr.next
        print(ll)

if __name__ == "__main__":
    l = Linkedlist()
    l.insert_b(2)
    l.insert_e(5)
    l.insert_values([2, 3, 4])
    l.print()
    ##    l.length()
    ##    l.remove(10)
    l.insert(6, 2)
    l.print()


        
    
