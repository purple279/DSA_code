class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Doublelinkedlist:
    def __init__(self):
        self.head = None  # head ---> None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node # head ---> new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    
    def insert_at_index(self, index, data):
        if index < 0:
            return
        if index == 0:
            self.insert_at_beginning(data)
            return 
        new_node = Node(data)
        temp = self.head
        for i in range(0, index - 1):
            if temp is None:
                return 
            temp = temp.next
        if temp is None:
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    def delete_by_value(self, key):
        temp = self.head
        while temp and temp.data != key:
            temp = temp.next
        if temp is None:
            return
        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next        
        if temp.next:
            temp.next.prev = temp.prev
            
    def delete_by_index(self, index):
        if index < 0 or self.head is None:
            return
        temp = self.head
        for i in range(index):
            if temp is None:
                return
            temp = temp.next
        if temp is None:
            return
        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next
        if temp.next:
            temp.next.prev = temp.prev            
            
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False
                   
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
        print("None")    

l = Doublelinkedlist()
l.insert_at_end(10)                    
l.insert_at_end(20)
l.insert_at_end(30)
l.insert_at_beginning(5)
l.display()
l.delete_by_value(30)
l.display()
l.delete_by_index(0)
l.display()
print("search 20:", l.search(20))
print("search 5:", l.search(5))                  


