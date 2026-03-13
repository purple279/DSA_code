class QueueUsingArr:
    size = 3
    def __init__(self):
        self.arr = [None] * self.size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if self.rear == self.size - 1:
            raise IndexError("queue if full")
        if self.front == -1 and self.rear == -1:
            self.front += 1
            self.rear += 1
            self.arr[self.rear] = data
            return
        self.rear += 1
        self.arr[self.rear] = data

    def dequeue(self):
        if self.front == -1 or self.rear == -1 or self.front > self.rear:
            raise IndexError("queue is empty")
        data = self.arr[self.front]
        self.front += 1
        return data
    
if __name__ == "__main__":
    q = QueueUsingArr()
    q.enqueue(10)
    q.enqueue(0)
    q.enqueue(50)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
