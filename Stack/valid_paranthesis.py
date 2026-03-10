class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            print("underflow")
            return None
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return None
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
def is_valid(exp):
    stack = Stack()
    for c in exp:
        if c in '[{(':
            stack.push(c)
        elif c in ']})':
            if stack.is_empty():
                return False
            current = stack.pop()
            if ((current == '{' and c != '}') or 
                (current == '[' and c != ']') or 
                (current == '(' and c != ')')):
                return False
    return stack.is_empty()

if __name__ == "__main__":
  expression = input("enter a expression : ")
  if is_valid(expression):
      print("Balanced")
  else:
      print("Not Balanced")                

