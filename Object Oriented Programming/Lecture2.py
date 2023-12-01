'''
 ==> THE PYTHON SELF:

        Self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in Python. It binds the attributes with the given arguments. 

        When working with classes in Python, the term “self” refers to the instance of the class that is currently being used. It is customary to use “self” as the first parameter in instance methods of a class. Whenever you call a method of an object created from a class, the object is automatically passed as the first argument using the “self” parameter. This enables you to modify the object’s properties and execute tasks unique to that particular instance.


==> __init__ Method:

        The __init__ method is a special method in Python classes, and it serves as the constructor. This method is automatically called when an object of the class is created using the ClassName() syntax. The __init__ method is responsible for initializing the attributes of the object.

==> self Argument:
        
        The self parameter is the first parameter in the __init__ method and represents the instance of the class. When you create an object, Python automatically passes the instance as the first argument to the __init__ method. By convention, this parameter is named self, but you can name it differently if you want, although it is highly recommended to stick to the convention.

'''

class mynumber:
    greet = "hello" # Static variable that will be always same for all instances created from this clss
    def __init__(self, value):
        # Inside the __init__ method, you can initialize the attributes of the object using the passed arguments.
        self.value = value 
     
    def print_value(self):
        print(self.value)
 
obj1 = mynumber(17)
obj1.print_value()
print(obj1.greet)

obj2 = mynumber(89)
obj2.print_value()
print(obj2.greet)


'''
    "Self: Pointer to Current Object"
    # Self is always required as the first argument in every method
'''

class check:
    def __init__(self):
        print("Address of self = ",id(self))
 
obj = check()
print("Address of class object = ",id(obj))

obj2 = check()
print("Address of class object = ",id(obj2))