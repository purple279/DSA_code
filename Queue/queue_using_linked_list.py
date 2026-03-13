class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueUsingLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = None(data)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = self.rear.next

    def dequeue(self):
        if self.front is None:
            raise IndexError("queue is empty")
        temp = self.front.data
        self.front = self.front.next
        return temp

if __name__ == "__main__":
  q = QueueUsingLL()
  q.enqueue(10)
  q.enqueue(0)
  q.enqueue(50)
  print(q.dequeue())
  print(q.dequeue())
  print(q.dequeue())
  print(q.dequeue())        

