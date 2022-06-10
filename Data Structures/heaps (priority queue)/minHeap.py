# Implementing a priority queue where min item is returned first using a min heap
import sys

class minPriorityQueue:
    def __init__(self, maxsize) -> None:
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [sys.maxsize] * maxsize

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        output = ""
        for i in range(0, (self.size - 1 // 2)):
            output += (" PARENT : " + str(self.Heap[i]) + 
                  " LEFT CHILD : " + str(self.Heap[self.left_child(i)]) +
                  " RIGHT CHILD : " + str(self.Heap[self.right_child(i)]) + "\n")
        return output

    def parent(self, index): #O(1)
        return index // 2
    
    def left_child(self, index): #O(1)
        return (2 * index) + 1 

    def right_child(self, index): #O(1)
        return (2 * index) + 2


    def swap(self, firstIndex, secondIndex): #O(1)
        self.Heap[firstIndex], self.Heap[secondIndex] = (self.Heap[secondIndex], self.Heap[firstIndex])

    def insert(self, ele): #O(logN)
        if self.size >= self.maxsize:
            return "Heap is Full"

        self.Heap[self.size] = ele
        curr = self.size

        while (self.Heap[curr] < self.Heap[self.parent(curr)]):
            self.swap(curr, self.parent(curr))
            curr = self.parent(curr)

        self.size += 1

    def extractMin(self): #O(logN)
        if self.size == 0: return "Heap is empty"

        popped = self.Heap[0]
        self.Heap[0] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(0) #Shift Down
          
        return popped

    def minHeapify(self, index): #O(logN)
        if not index * 2 > self.size:
            if self.Heap[index] > self.Heap[self.left_child(index)]:
                self.swap(index, self.left_child(index))
                self.minHeapify(self.left_child(index))

            elif self.Heap[index] > self.Heap[self.right_child(index)]:
                self.swap(index, self.right_child(index))
                self.minHeapify(self.right_child(index))  




# Test
pQueue = minPriorityQueue(10)
assert len(pQueue) == 0

pQueue.insert(10)
pQueue.insert(5)
pQueue.insert(15)
assert len(pQueue) == 3
print(str(pQueue))


assert pQueue.extractMin() == 5
assert pQueue.extractMin() == 10
assert pQueue.extractMin() == 15

assert pQueue.extractMin() == "Heap is empty"

print("ALL PASSED ✔")