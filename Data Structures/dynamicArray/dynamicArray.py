class DynamicArray(object):
    # Similar to List
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.static_arr = self._make_array(self.capacity)

    # this is how we will bw able to use -> len(arr)
    def __len__(self) -> int:
        return self.size
    
    # this is how we will bw able to use -> arr[]
    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.static_arr[index]
        else:
            raise IndexError('Given index: {0} is less than Zero or larger than array size {1} '.format(index, self.size))

    def __str__(self) -> str:
        return str(self.static_arr)

    def _resize(self, new_capacity):
        new_arr = self._make_array(new_capacity)

        for i in range(self.size):
            new_arr[i] = self.static_arr[i]

        self.static_arr = new_arr
        self.capacity = new_capacity

    def _make_array(self, capacity):
        return [None] * capacity

    # Adds an element at the end of the list 
    def append(self, item): #Time Complexity = O(1) if resizing is needed Time Complexity becomes O(n)
        if self.size == self.capacity:
            self._resize(2 * self.capacity)

        self.static_arr[self.size] = item
        self.size += 1

    # Removes all the elements from the list
    def clear(self): 
        self.__init__()

    # Returns a copy of the list
    def copy(self):
        return self.static_arr

    # Returns the number of elements with the specified value
    def count(self, value): #Time Complexity = O(n)
        counter = 0
        for ele in self.static_arr:
            if ele == value:
                counter += 1
        return counter
    
    # Add the elements of a list (or any iterable), to the end of the current list
    def extend(self, new_list): #Time Complexity = O(n) where n is the new_list
        for ele in new_list:
            self.append(ele)

    # Returns the index of the first element with the specified value
    def index(self, value): #Time Complexity = O(n)
        counter = 0
        for ele in self.static_arr:
            if ele == value:
                return counter
            counter += 1
        return -1

    # Reverses the order of the list
    def reverse(self): #Time Complexity = O(n)
        temp_arr = self._make_array(self.size)
        for i in range(self.size):
            temp_arr[i] = self.static_arr[self.size - 1 - i]
        return temp_arr

    # Delete Item from end of list
    def pop(self): #Time Complexity = O(1)
        if self.size==0:
            print("Array is empty deletion not Possible")
            return

        self.static_arr[self.size-1]=0
        self.size-=1

    # Sorts the list
    def sort(self): #Time Complexity depends on underlying sorting algo
        return sorted(self.static_arr)

    # Adds an element at the specified position
    def insert(self, index, value): #Time Complexity = O(n)
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        
        # Moving element over for insertion
        for i in range(self.size-1,index-1,-1):
            self.static_arr[i+1]=self.static_arr[i]
          
        self.static_arr[index] = value
        self.size+=1

    # Removes the first item with the specified value
    def remove(self, value): #Time Complexity = O(n)
        # Similar to insertion
        return


# Test
dy_array = DynamicArray()
dy_array.append(5)
assert dy_array[0] == 5
assert str(dy_array) == "[5]"

dy_array.append(6)
dy_array.append(7)
assert str(dy_array) == "[5, 6, 7, None]"
assert dy_array.copy() == [5, 6, 7, None]
assert len(dy_array) == 3

dy_array.append(7)
assert dy_array.count(7) == 2

dy_array.extend([1, 2, 3])
assert dy_array[6] == 3
assert len(dy_array) == 7

dy_array.append(20)
assert dy_array.index(20) == 7

assert dy_array.reverse() == [20, 3, 2, 1, 7, 7, 6, 5]
assert dy_array.sort() == [1, 2, 3 , 5, 6, 7, 7, 20]

dy_array.pop()
assert len(dy_array) == 7

dy_array.insert(2, 50)
assert dy_array[2] == 50

dy_array.clear()
assert len(dy_array) == 0

print("ALL PASSED")