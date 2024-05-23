'''
INSERTION SORT :

    -> Insertion sort is a simple and intuitive sorting algorithm used to arrange a list or 
       an array of elements in a specific order, typically ascending or descending. It works by 
       iteratively building a sorted portion of the input list, one element at a time, and 
       inserting each unsorted element into its correct position within the sorted portion.

    -> Insertion sort is an in-place sorting algorithm, which means it doesn't require additional 
       memory to store temporary data structures. However, it is not the most efficient sorting 
       algorithm for large lists, as its average and worst-case time complexities are both O(n^2),
       where n is the number of elements in the list. Consequently, it is often used for 
       small datasets

'''
def insertion_sort(arr):
    for index in range(1, len(arr)):
        currentElement = arr[index]
        j = index - 1

        while j >= 0 and currentElement > arr[j]:
            if arr[j] < currentElement:
                arr[j+1] = arr[j]
                j = j - 1
        
        arr[j+1] = currentElement


mylist = [10,1,7,4,8,2,11]
print("Before:", mylist)
insertion_sort(mylist)
print("After:", mylist)