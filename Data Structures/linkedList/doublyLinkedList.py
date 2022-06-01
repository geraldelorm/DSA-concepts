class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class dLinkedList:
    def __init__(self) -> None:
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        currNode = self.head
        output = "["
        while currNode:
            output += str(currNode.data) + " "
            currNode = currNode.next
        output += "]"
        return output

    # Insert after a specified Node
    def insertAfter(self, prevNode, data):  # Time Complexity O(1)
        if self.head is None: return "List is empty"
        if prevNode is None: return "The node provided is the last node, use insertAtEnd() instead"
        newNode = Node(data)

        newNode.next = prevNode.next
        newNode.prev = prevNode
        prevNode.next = newNode
        self.size += 1

        # Insert Before a specified Node
    def insertBefore(self, nextNode, data):  # Time Complexity O(1)
        if self.head is None: return "List is empty"

        newNode = Node(data)

        newNode.next = nextNode
        newNode.prev = nextNode.prev
        nextNode.prev.next = newNode
        nextNode.prev = nextNode
        self.size += 1

    # Insert at the beginning
    def insertAtBeginning(self, data): # Time Complexity O(1)
        newNode = Node(data)

        if self.head is None:
            self.tail = newNode
            self.head = newNode
            self.size += 1
            return
        
        newNode.next = self.head
        self.head = newNode

        self.size += 1

    # Remove at the beginning
    def removeAtBeginning(self): # Time Complexity O(1)
        if self.head is None: return "List is empty"

        tempNode = self.head.next
        self.head = tempNode

        self.size -= 1
    
    # Get Beginning Element
    def getHead(self): # Time Complexity O(1)
        if self.head is None: return "List is empty"

        return self.head.data

    # Insert at the End
    def insertAtEnd(self, data): # Time Complexity O(1)
        newNode = Node(data)

        if self.head is None:
            self.head = newNode 
            self.tail = newNode
            self.size += 1
            return
        
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        
        self.size += 1

    # Remove at the End
    def removeAtEnd(self): # Time Complexity O(1)
        if self.head is None: return "List is empty"

        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1 
    
    # Get Ending Element
    def getTail(self): # Time Complexity O(1)
        if self.head is None: return "List is empty"

        return self.tail.data

    # Search for data in a linked list
    def contains(self, data): # Time Complexity O(n)
        if self.head is None: return "List is empty"

        currNode = self.head
        while currNode:
            if currNode.data == data:
                return True
            currNode = currNode.next
        return False

    # Delete Node in position
    def delete(self, position): # Time Complexity O(position)
        if self.head is None: return "List is Empty"
        if position > self.size: return "Position is larger than List size: " + str(self.size)

        currNode = self.head
        for i in range(1, position + 1):
            if i == position:
                nextNode = currNode.next.next
                currNode.next = nextNode
                self.size -= 1
                return
            currNode = currNode.next

    def isEmpty(self): # Time Complexity O(1)
        return not self.head
    
    def clear(self): # Time Complexity O(1)
        self.head = None
        self.size = 0




# Test
dll = dLinkedList()
dll.insertAtBeginning(1)
dll.insertAtBeginning(2)
dll.insertAtBeginning(2)
dll.insertAtBeginning(5)
dll.removeAtBeginning()


print(str(dll)) #[2 2 1 ]
print(dll.getHead())  #2

dll.insertAtEnd(0)
dll.insertAtEnd(-1)
dll.insertAtEnd(-2)
dll.insertAtEnd(-3)
dll.removeAtEnd()

print(str(dll)) #[2 2 1 0 -1 -2 ]
print(dll.getTail()) #-2
print(len(dll)) #6

dll.delete(5)
print(str(dll)) #[2 2 1 0 -1]
print(len(dll)) #5

dll.insertAfter(dll.head.next, 9)
dll.insertBefore(dll.head.next.next, 8)
print(str(dll)) #[2 2 8 9 1 0 -1]
print(len(dll)) #7

print(dll.contains(50)) # False
print(dll.contains(0)) # True

dll.clear()
print(len(dll)) # 0
print(dll.isEmpty()) # True