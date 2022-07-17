def mergeSort(arr): 
    if len(arr) <= 1:
        return arr
    mid = len(arr)// 2
    sortedLeft = mergeSort(arr[:mid])
    sortedRight = mergeSort(arr[mid:])

    return mergeArr(arr, sortedLeft, sortedRight)

def mergeArr(myList, left, right): #O(n)
    # Two iterators for traversing the two halves
    i = 0
    j = 0
    
    # Iterator for the main list
    k = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # The value from the left half has been used
            myList[k] = left[i]
            # Move the iterator forward
            i += 1
        else:
            myList[k] = right[j]
            j += 1
        # Move to the next slot
        k += 1

    # For all the remaining values
    while i < len(left):
        myList[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        myList[k]=right[j]
        j += 1
        k += 1
    
    return myList


# TEST
assert mergeSort([5, 3, 4, 2, 1]) == [1, 2, 3, 4, 5]
assert mergeSort([98, 56, 87, 45]) == [45, 56, 87, 98]

print("Passed ✔")