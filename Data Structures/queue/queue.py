class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.size = 0
        self.front = None
        self.back = None

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        output = []
        currNode = self.front
        while currNode:
            output.append(currNode.data)
            currNode = currNode.next
        return str(output)

    # add elements to the back of a queue
    def enqueue(self, data): #Time Complexity = O(1)
        newNode = Node(data)
        if self.front is None:
            self.front = newNode
            self.back = newNode
            self.size += 1
            return

        self.back.next = newNode
        self.back = newNode
        self.size += 1

    # remove elements from the front of the queue
    def dequeue(self): #Time Complexity = O(1)
        if self.front is None: return "Queue is empty"

        val = self.front.data
        self.front = self.front.next
        self.size -= 1

        return val

    #  return front value without removing
    def peek(self): #Time Complexity = O(1)
        if self.front is None: return "Queue is empty"
        return self.front.data

    # Searching for data in a queue
    def contains(self, data): #Time Complexity = O(n)
        if self.front is None: return "Queue is empty"

        currNode = self.front
        while currNode:
            if currNode.data == data:
                return True
            currNode = currNode.next
        
        return False
    
    def isEmpty(self): #Time Complexity = O(1)
        return self.size == 0





# Test
myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)

assert str(myQueue) == "[1, 2, 3, 4, 5]"
assert len(myQueue) == 5

assert myQueue.dequeue() == 1
assert str(myQueue) == "[2, 3, 4, 5]"

assert myQueue.peek() == 2
assert str(myQueue) == "[2, 3, 4, 5]"

assert myQueue.contains(50) == False
assert myQueue.contains(4) == True

assert myQueue.isEmpty() == False


print("ALL PASSED ✔")