def quickSort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    leftLess = [i for i in arr[1:] if i <= pivot]
    rightGreater = [i for i in arr[1:] if i > pivot]

    return quickSort(leftLess) + [pivot] + quickSort(rightGreater) #tail recursion 😜



# Time = O(nlogn) or O(n^2) in worse case with randomization of pivot
# Space = O(n)

# TEST
assert quickSort([5, 3, 4, 2, 1]) == [1, 2, 3, 4, 5]
assert quickSort([98, 56, 87, 45]) == [45, 56, 87, 98]

print("Passed ✔")