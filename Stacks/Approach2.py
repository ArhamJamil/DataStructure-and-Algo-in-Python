class Stack:
    def __init__(self):
        self.arr = [None] * 10  # Initialize the stack with 10 None values
        self.StackPointer = -1  # Initialize the stack pointer

    def PrintStackData(self):
        print(self.arr)

    def Push(self, element):
        if self.StackPointer == 9:
            print("Stack is Full, remove element to add data")
            return False
        else:
            self.StackPointer += 1
            self.arr[self.StackPointer] = element
            return True

    def Pop(self):
        if self.StackPointer < 0:
            print("Stack is Empty, cannot remove element")
            return False
        else:
            removedElement = self.arr[self.StackPointer]
            self.arr[self.StackPointer] = None  # Clear the element at the top
            self.StackPointer -= 1
            return True



        
my_stack = Stack() # Create an instance of the Stack class

my_stack.PrintStackData()  # Print the initial stack

my_stack.Push(10) # Push an element onto the stack
my_stack.PrintStackData()  
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

print("Actual Stack Data => ", Stack().PrintStackData())
