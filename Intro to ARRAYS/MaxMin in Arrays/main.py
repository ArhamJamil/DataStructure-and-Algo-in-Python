'''
In C++, the INT_MAX constant represents the maximum value that can be stored in an int data type. 
In Python, there is no direct equivalent built-in constant like INT_MAX from C++, 
but you can achieve similar functionality using the "sys.maxsize" constant for integers.

\\sys.maxsize\\ provides the largest positive integer that can be used as an index in Python lists, 
which is typically equivalent to the maximum value representable by an int on the platform.

'''
import sys

def MinNumber(arr):
    minValue = sys.maxsize

    for index in range(len(arr)):
        # print(element)
        if (arr[index] < minValue):
            minValue = arr[index]
    
    return minValue


def MaxNumber(arr):
    maxValue = 0 
    
    for index in range(len(arr)):
        if (arr[index] > maxValue):
            maxValue = arr[index]

    return maxValue



my_array = [10,14,15,9,8,4,100,200,134,34]

# Minimum Number of Array 
answer = MinNumber(my_array)
print("The Minimum Number in array is : ", answer)

#Maximum Number of Array
answer = MaxNumber(my_array)
print("The Maximum Number of array is : ", answer)