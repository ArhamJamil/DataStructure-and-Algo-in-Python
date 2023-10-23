"""
A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. 
This means that the item that is inserted first will be the first one to be removed. 
Think of it like a real-world queue of people waiting in line – 
the person who arrives first is the first one to leave the line when it's their turn.

Queues are commonly used in computer science and software development for various applications, 
such as task scheduling, managing resources, and more.

"""

global DataQueue
global FrontPointer
global RearPointer

DataQueue = [None] * 10 
FrontPointer = -1
RearPointer = -1

def Enqueue(data):
    global DataQueue
    global FrontPointer
    global RearPointer

    if RearPointer == len(DataQueue) - 1:
        print("Queue is Full , Can't add more Data")
    else:
        RearPointer = RearPointer + 1
        DataQueue[RearPointer] = data
        print(DataQueue)

def Dequeue():
    global DataQueue
    global FrontPointer
    global RearPointer

    if FrontPointer == RearPointer or FrontPointer == len(DataQueue) - 1:
        print("Queue is Empty , Can't delete more data")
    else:
        FrontPointer = FrontPointer + 1
        DataQueue[FrontPointer] = None
        print(DataQueue)


Enqueue(1)
Enqueue(2)
Enqueue(9)

Dequeue()

Enqueue(4)

Dequeue()
Dequeue()

Enqueue(1)
Enqueue(2)
Enqueue(9)
Enqueue(1)
Enqueue(2)
Enqueue(9)
Enqueue(2)

Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Dequeue()
Enqueue(9)
Enqueue(2)