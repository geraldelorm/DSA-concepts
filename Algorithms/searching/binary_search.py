def binary_search(list, target ):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] > target:
            high = mid - 1
        if list[mid] < target:
            low = mid + 1
        else:
            return mid
    return None

# Time = O(logN)
# Space = O(1)


# Test
my_list = [1, 2 , 3]
assert binary_search(my_list, 3) == 2
assert binary_search(my_list, 5) == None

print("Passed ✔")