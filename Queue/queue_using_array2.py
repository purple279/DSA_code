class QueueUsingArr:
    size = 3
    def __init__(self):
        self.arr = [None] * self.size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if self.rear == self.size - 1:
            raise IndexError("queue if full")
        if self.rear == -1:
            self.rear += 1
            self.arr[self.rear] = data
            return
        self.rear += 1
        self.arr[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            raise IndexError("queue is empty")
        temp = self.arr[0]
        for i in range(1, self.rear + 1):
            self.arr[i - 1] = self.arr[i]
        self.rear -= 1
        return temp
    
if __name__ == "__main__":
    q = QueueUsingArr()
    q.enqueue(10)
    q.enqueue(0)
    q.enqueue(50)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
