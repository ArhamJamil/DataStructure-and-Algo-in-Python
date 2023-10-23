'''
What is an ARRAY ?

 An "ARRAY" is a data structure that holds a 'collection of elements', each identified by an index or a key. 
 The elements in an array are usually of the same data type, and they are stored in contiguous memory 
 locations, which allows for efficient access and manipulation of the elements.

ARRAY in Python: 
    * In Python, arrays are implemented using LISTS, which are a versatile and widely used data structure. 
    * NOTE : "Remember that Python lists are dynamic and can hold elements of different types."
    
    # Array Functions and Methods:
        Python lists (arrays) provide various functions and methods for manipulation:

        * [ len(arr) ]: Returns the number of elements in the array.
        * [ arr.append(item) ]: Adds an item to the end of the array.
        * [ arr.insert(index, item) ]: Inserts an item at a specific index.
        * [ arr.remove(item) ]: Removes the first occurrence of a specified item.
        * [ arr.pop(index) ]: Removes and returns the item at the specified index.
        * [ arr.index(item) ]: Returns the index of the first occurrence of the specified item.
        * [ arr.count(item) ]: Returns the number of occurrences of a specified item.
        * [ arr.sort() ]: Sorts the array in ascending order.
        * [ arr.reverse() ]: Reverses the order of elements in the array.
 
 
 '''

# DECLARATION OF ARRAY :
    # DECLARE <NameOfArray> : ARRAY[1:10] OF <DataType> 
    # DECLARE my_array : ARRAY[1:6] OF INTEGER

# INITIALIZATION of ARRAY in python
my_array = []

# CREATING ARRAY in Python:
my_array = [1,2,3,4,5,6,7] # Creating an array (list) of integers
char_array = ['A', 'B', 'C', 'D', 'E', 'F']
# SIZE of ARRAY in python:
print("size of Array is : ",len(my_array))
    #  size of my_array is 6 

# Accessing elements by index
    # Index Start from 0 in python 
    # TotalIndexOFArray = (SIZEofArray - 1) => {I = (n-1)}
'''
    NOTE: 
        Array elements are accessed using their index, which starts from 0 for the first element. 
        Negative indexing can also be used to access elements from the end of the array.
'''
first_element = my_array[0]  # Accessing the first element (index 0)
print("the first element (index 0)", first_element)
second_element = my_array[1]  # Accessing the second element (index 1)
print("the second element (index 1)",second_element)


# Array with Function 

def printArray(arr, size):
    i = 0
    while i < size:
        print(arr[i])
        i = i + 1
        
printArray(my_array, 7)
printArray(char_array, len(char_array))



