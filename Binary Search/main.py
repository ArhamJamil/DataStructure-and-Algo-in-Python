"""
# BINARY SEARCH :

    -> Binary search is an efficient algorithm used to search for a specific element in a 
       sorted list or array. It works by repeatedly dividing the search interval in half until 
       the target element is found or the search interval becomes empty. Binary search is 
       significantly faster than linear search for large datasets because it reduces the 
       search space exponentially with each iteration.

    STEPS :

        * You need to know the value you are searching for, called the "target."

        * Calculate the midpoint of the current search interval by averaging the lower and upper bounds.
            => [ MIDPOINT = (STARTindex + ENDindex) / 2 ]

        * Compare the element at the midpoint with the target value.
    
        * If the midpoint element is equal to the target, you've found it, and the search is successful.
    
        * If the midpoint element is greater than the target, update the STARTindex of the 
          search interval to mid - 1,  effectively discarding the right half of the current interval.
    
        * If the midpoint element is less than the target, update the ENDindex of the 
          search interval to mid + 1, effectively discarding the left half of the current interval.

"""


def BinarySearch(key, arr):
    startIndex = 0
    endIndex = len(arr) - 1

    while (startIndex <= endIndex):
        # This can result in a floating-point number
        x = (startIndex + endIndex) / 2
        mid = int(x)  # Convert the floating-point number to an integer

        print("startIndex:", startIndex, "endIndex:", endIndex, "mid:", mid)  # Debug line
        if arr[mid] == key:
            return [mid, True]

        if key > arr[mid]:
            startIndex = mid + 1
        else:
            endIndex = mid - 1

    return False


myList1 = [11,22,33,44,55,66,77,88]
key1 =88

value = BinarySearch(key1, myList1)
print(value)
