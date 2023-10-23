"""
NOTE:
    In Python, the terms "pass by reference" and "pass by value" are not used in the same strict sense as they are 
    in languages like C++ or Java. Instead, Python's parameter passing mechanism is a bit different and 
    often referred to as "passing objects by reference" or "passing objects by sharing."

# Pass by Object Reference (or Pass by Sharing):
    
    * When you pass an object as an argument to a function, what gets passed is a reference to
      the object (memory address), not a copy of the object itself.

    * Changes made to the object within the function can affect the object outside the 
      function because they both refer to the same memory location.

# Immutable vs. Mutable:

    * In Python, objects are either mutable (can be modified after creation) or 
      immutable (cannot be modified after creation).

    * \\Immutable objects\\, like numbers, strings, and tuples, behave like "pass by value" because they 
      cannot be changed directly. A new object is created when you modify an immutable object.

    * \\Mutable objects\\, like lists and dictionaries, behave like "pass by reference" because changes 
      made inside the function are reflected outside as well.



"""

# Passing an integer (immutable)
def modify_integer(num):
    num += 10
    print("Inside function:", num)

# Passing a list (mutable)
def modify_list(my_list):
    my_list.append(10)
    print("Inside function:", my_list)


y = 5
print(y)
modify_integer(y)
print("Outside function:", y)
# Output:
# Inside function: 15
# Outside function: 5 (unchanged)


my_list = [1, 2, 3]
print(my_list)
modify_list(my_list)
print("Outside function:", my_list)
# Output:
# Inside function: [1, 2, 3, 10]
# Outside function: [1, 2, 3, 10] (changed)