global DataQueue

DataQueue = [None] * 10
class Queue:
    def __init__(self, arr):
        self.arr = arr
        self.RarePointer = -1
        self.FrontPointer = -1

    def Enqueue(self, data):
        if self.RarePointer == len(self.arr) - 1:
            print("Queue is full, can't add more data")
        else:
            self.RarePointer = self.RarePointer + 1
            self.arr[self.RarePointer] = data
            print(self.arr)

    def Dequeue(self):
        if self.FrontPointer == self.RarePointer:
            print("Queue is empty, can't delete more data")
        else:
            self.FrontPointer = self.FrontPointer + 1
            self.arr[self.FrontPointer] = None
            print(self.arr)

# Create an instance of the Queue class
myQueue = Queue(DataQueue)


myQueue.Enqueue(2)
myQueue.Enqueue(4)
myQueue.Enqueue(6)
myQueue.Enqueue(8)
myQueue.Enqueue(10)

myQueue.Dequeue()
myQueue.Dequeue()
myQueue.Dequeue()

myQueue.Enqueue(6)
myQueue.Enqueue(8)
myQueue.Enqueue(10)

myQueue.Dequeue()
myQueue.Dequeue()
myQueue.Dequeue()
myQueue.Dequeue()
myQueue.Dequeue()
myQueue.Dequeue()
myQueue.Dequeue()
