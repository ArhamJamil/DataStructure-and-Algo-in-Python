"""
What is STACK DataStructure :

    -> A stack is a fundamental data structure in computer science and programming that 
       follows the Last-In, First-Out (LIFO) principle. In a stack, the last element added 
       is the first one to be removed. Think of it as a stack of plates where you add new plates 
       on top and remove plates from the top.

    A stack typically supports two primary operations:
        *   Push: This operation adds an element to the top of the stack.
        *   Pop: This operation removes the top element from the stack.

    Stacks can be implemented using arrays, linked lists, or other data structures. 
    They are used in various applications and scenarios for their simplicity and efficiency.

    Here are some common use cases for stacks:

        => Function Calls: Stacks are used to manage function calls in most programming languages. 
           When a function is called, its local variables and execution context are pushed onto 
           the stack. When the function returns, its context is popped from the stack.

        => Memory Management: Stacks are crucial in memory management, including call stacks 
            for managing program execution and managing memory allocation for variables.

        => Undo/Redo Functionality: Stacks can be employed to implement undo and redo functionality
           in applications. Each state change is pushed onto the stack, allowing users to navigate 
           backward and forward through their actions.

"""


global StackPointer 
global StackData

StackPointer = 0
StackData = []

class Stack:
    def __init__(self, arr):
        self.arr = arr

    def PrintStackData(self):
        print(self.arr)

    def Push(self, element):
        global StackPointer  # Use the global keyword to modify the global StackPointer
        global StackData
        if len(self.arr) == 10 :
            print("Stack is Full, remove element to add data")
            return False
        else:
            if StackPointer >= len(self.arr):
                # Manually increase the list's length
                self.arr += [None] * (StackPointer - len(self.arr) + 1)
            self.arr[StackPointer] = element
            StackPointer += 1
            # print(StackPointer)
            StackData = self.arr
            return True
        
    def Pop(self):
        global StackPointer
        global StackData
        if len(self.arr) == 0:
            print("Stack is Empty, cannot remove element")
            return False
        else:
            StackPointer -= 1  # Decrement the global StackPointer to point to the top element
            removedElement = self.arr[StackPointer]
            self.arr = self.arr[0:StackPointer]
            # print(removedElement)
            StackData = self.arr
            return True
            


        
my_stack = Stack(StackData)  # Create an instance of the Stack class

my_stack.PrintStackData()  # Print the initial stack

my_stack.Push(10)
my_stack.PrintStackData()  # Push an element onto the stack
my_stack.Push(20)
my_stack.PrintStackData()  
my_stack.Push(30)
my_stack.PrintStackData()
my_stack.Push(40)
my_stack.PrintStackData()
my_stack.Push(50)
my_stack.PrintStackData()
my_stack.Push(60) 
my_stack.PrintStackData()
my_stack.Push(70) 
my_stack.PrintStackData()
my_stack.Push(80) 
my_stack.PrintStackData()
my_stack.Push(90) 
my_stack.PrintStackData()
my_stack.Push(100) 
my_stack.PrintStackData()

my_stack.Push(200)

my_stack.Pop() # Pop an element from the stack
my_stack.PrintStackData()  

my_stack.Pop()
my_stack.PrintStackData()  

my_stack.Pop()
my_stack.PrintStackData() 

my_stack.Pop()
my_stack.PrintStackData() 

my_stack.Pop()
my_stack.PrintStackData() 

my_stack.Pop()
my_stack.PrintStackData() 

my_stack.Pop()
my_stack.PrintStackData() 

my_stack.Pop()
my_stack.PrintStackData() 

my_stack.Pop()
my_stack.PrintStackData() 

my_stack.Pop()
my_stack.PrintStackData() 

my_stack.Pop()

print("Actual Stack Data => ", StackData)
