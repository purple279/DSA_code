class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class StackLinkedList:
    def __init__(self):
        self.top = None  # head ---> None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("underflow")
            return None
        data = self.top.data
        self.top = self.top.next
        return data
    
    def peek(self):
        if self.top is None:
            print("stack is empty")
            return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
if __name__ == "__main__":
  stack = StackLinkedList()
  stack.push(5)
  stack.push(6)
  stack.push(1)
  stack.push(2)

  print(stack.pop())
  print(stack.is_empty())
  print(stack.peek())   

                
    
