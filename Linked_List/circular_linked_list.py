class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.tail = None  # head ---> None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.tail is None:
            new_node.next = new_node
            self.tail = new_node 
        else:
            new_node.next = self.tail.next #tail → head
            self.tail.next = new_node #tail → new_node → head
     
    def insert_at_last(self, data):
        new_node = Node(data)
        if self.tail is None:
            new_node.next = self.tail
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def delete_at_last(self):
        if self.tail is None:
            print("empty list")
        if self.tail.next == self.tail:
            self.tail = None
        else:
            temp = self.tail.next
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.tail.next 
            self.tail = temp

    def display(self):
        if self.tail is None:
            print("list is empty")
            return
            
        temp = self.tail.next
        while True:    
            print(temp.data, end = " -> ")
            temp = temp.next
            if temp == self.tail.next:
                break
        print()

cll = CircularLinkedList()
cll.insert_at_beginning(7)
cll.insert_at_beginning(5)
cll.insert_at_beginning(1)
cll.insert_at_last(8)
cll.delete_at_last()
cll.display()

            
     
            

