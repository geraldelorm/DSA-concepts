# Recursive version - return index if found or appropriate index to place target 
def binary_search(list, target ):
    def helper(list, target, low, high):
        mid = int (low + ((high - low) / 2))
        if high < low:
            return low
        if list[mid] == target:
            return mid
        if list[mid] > target:
            return helper(list, target, low, mid - 1)
        else:
            return helper(list, target, mid + 1, high)
    return helper(list, target, 0, len(list) - 1)


# Iterative version
def binary_search2(list, target ):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] > target:
            high = mid - 1
        elif list[mid] < target:
            low = mid + 1
        else:
            return mid
    return None

# Time = O(logN)
# Space = O(1)


# Test
my_list = [1, 2 , 3]
assert binary_search(my_list, 3) == 2
assert binary_search(my_list, 5) == 3
assert binary_search(my_list, 0) == 0

assert binary_search2(my_list, 3) == 2
assert binary_search2(my_list, 5) == None
assert binary_search2(my_list, 0) == None

print("Passed ✔")