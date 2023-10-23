"""

SELECTION SORT :
    -> It is one of the algorithm that works repeatedly finding the minimum element 
       from the unsorted part of array and put in at the beginning of sorted region
       of array.

"""

def selection_sort(arr):
    num_of_elements = len(arr)

    # Traverse through all array elements
    for index in range(0, num_of_elements):
        minElementIndex = index

        # Find the minimum element in the remaining unsorted array
        for unsortedIndex in range(index+1, num_of_elements):
            if(arr[unsortedIndex] < arr[minElementIndex]):
                minElementIndex = unsortedIndex

    # Swap the found minimum element with the first element
        temp = arr[index]
        arr[index] = arr[minElementIndex]
        arr[minElementIndex] = temp


myList = [64,25,12,22,11,13]
print("Before: ", myList)
selection_sort(myList)
print("After: ", myList)