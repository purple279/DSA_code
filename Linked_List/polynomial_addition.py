class Node:
    def __init__(self, expo, coeff):
        self.coeff = coeff
        self.expo = expo
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None  # head ---> None
    
    def insert_at_end(self, expo, coeff):
        new_node = Node(expo, coeff)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def display(self):
        temp = self.head
        while temp:
            print(f"{temp.coeff}x^{temp.expo}", end = "")
            if temp.next: # only print + if another term exists
                print(" + ", end="")
            temp = temp.next
        print()

def add_poly(p1, p2):
    result = LinkedList()
    while p1 and p2:
        if p1.expo == p2.expo:
            result.insert_at_end(p1.coeff + p2.coeff, p1.expo) 
            p1 = p1.next
            p2 = p2.next

        elif p1.expo > p2.expo:
            result.insert_at_end(p1.coeff, p1.expo) 
            p1 = p1.next

        else:
            result.insert_at_end(p1.coeff, p1.expo) 
            p2 = p2.next
                              
    while p1:
        result.insert_at_end(p1.coeff, p1.expo) 
        p1 = p1.next

    while p2:
        result.insert_at_end(p2.coeff, p2.expo) 
        p2 = p2.next

    return result            
if __name__ == "__main__":
  p1 = LinkedList()
  p1.insert_at_end(3, 2)
  p1.insert_at_end(4, 1)
  p1.insert_at_end(1, 0)

  p2 = LinkedList()
  p2.insert_at_end(4, 2)
  p2.insert_at_end(2, 0)

  p1.display()
  p2.display()

  result = add_poly(p1.head, p2.head)
  result.display()


