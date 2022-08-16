def quickSort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    leftLess = [i for i in arr[1:] if i <= pivot]
    rightGreater = [i for i in arr[1:] if i > pivot]

    # tail recursion 😜
    return quickSort(leftLess) + [pivot] + quickSort(rightGreater)

# Time = O(nlogn) or O(n^2) in worse case with randomization of pivot
# Space = O(n)

# in place sorting
def quickSort2(arr, low, high):
    if len(arr) == 1:
        return arr
  
    if low < high:
        pivot = partition(arr, low, high)

        quickSort2(arr, low, pivot - 1)
        quickSort2(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot, ptr = arr[high], low

    for i in range(low, high):
        if arr[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    arr[ptr], arr[high] = arr[high], arr[ptr]
    return ptr

# Time = O(nlogn)
# Space = O(1)

# TEST
assert quickSort([5, 3, 4, 2, 1]) == [1, 2, 3, 4, 5]
assert quickSort([98, 56, 87, 45]) == [45, 56, 87, 98]

arr = [5, 3, 4, 2, 1]
quickSort2(arr, 0, len(arr) - 1)
assert arr == [1, 2, 3, 4, 5]

arr2 = [98, 56, 87, 45]
quickSort2(arr2, 0, len(arr2)-1)
assert arr2 == [45, 56, 87, 98]

print("Passed ✔")
