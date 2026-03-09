class StackArray:
    def __init__(self):
        self.size = 100
        self.stack = [0] * self.size
        self.top = -1

    def push(self, data):
        if self.top == self.size - 1:
            print("overflow")
            return 
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.top == -1:
            print("underflow")
            return
        data = self.stack[self.top]
        self.top -= 1
        return data
    
    def peek(self):
        if self.top == -1:
            print("stack is empty")
            return None
        return self.stack[self.top]
    
    def is_empty(self):
        return self.top == -1
    
if __name__ == "__main__":
  stack = StackArray()
  stack.push(5)
  stack.push(6)
  stack.push(1)
  stack.push(2)
  print(stack.pop())
  print(stack.is_empty())
  print(stack.peek())    
    
