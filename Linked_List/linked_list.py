class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None  # head ---> None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
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
        new_node = temp.next
        temp.next = new_node
    def delete_by_value(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next and temp.next.data != key:
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    def delete_by_index(self, index):
        if index < 0 or self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        temp = self.head
        for i in range(index - 1):
            if temp is None:
                return
            temp = temp.next
        if temp is None or temp.next is None:
            return
        temp.next = temp.next.next

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
l = linkedlist()
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


