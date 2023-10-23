"""
# LINEAR Search Algorithm: 

    Linear search is a simple searching algorithm that checks each element in a list or array 
    one by one until a match is found or the entire list has been searched. 
    
"""

def LinearSearch(key, arr):
    found = False
    for index in range(len(arr)):
        if arr[index] == key:
            found = True
            return found
        
    return found


myList1 = [3,7,0,8,1,-2,9,5]
key1 = 8

value = LinearSearch(key1, myList1)
if value:
    print(f"The key:{key1} is found in Array:{myList1}")
else:
    print(f"The key:{key1} is not found in Array:{myList1}")


