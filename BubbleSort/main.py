"""
BUBBLE SORT :
    -> It is a simple comparision based SORTING algorithm that repeatedly steps
       through the array , Compares ADJACENT element (elements in sequence that are located
       next to each other), and SWAPS them if they are in the WRONG order. The pass through 
       the array is repeated until no SWAPS are needed
       
    -> After every round the largest element in array is placed to it it's right place 

"""

def Bubble_Sort(arr):
    num_of_element = len(arr)
    
    for round in range(1, num_of_element-1):
        # Flag to optimize the algorithm by checking if any swaps were made in this pass
        swapped = False
       
        # Last index elements are already in place, so we don't need to check them
        for index in range(0, (num_of_element-round)):

            # Swap if the element found is greater than the next element
            if arr[index] > arr[index+1]:
                
                temp = arr[index]
                arr[index] = arr[index+1]
                arr[index+1]= temp

                swapped = True
        
        # If no two elements were swapped in this pass, the array is sorted
        if not swapped:
            break


myList = [10,1,7,6,14,9]
print("Before: ", myList)
Bubble_Sort(myList)
print("After: ", myList)
