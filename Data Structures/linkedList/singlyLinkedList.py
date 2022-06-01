class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class sLinkedList:
    def __init__(self) -> None:
        self.size = 0
        self.head = None

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
        prevNode.next = newNode
        self.size += 1


    # Insert at the beginning
    def insertAtBeginning(self, data): # Time Complexity O(1)
        newNode = Node(data)

        if self.head is None:
            self.head = newNode 
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
    def insertAtEnd(self, data): # Time Complexity O(n)
        newNode = Node(data)

        if self.head is None:
            self.head = newNode 
            return
        
        currNode = self.head
        while currNode:
            if currNode.next is None:
                currNode.next = newNode
                self.size += 1
                return
            currNode = currNode.next 

    # Remove at the End
    def removeAtEnd(self): # Time Complexity O(n)
        if self.head is None: return "List is empty"

        currNode = self.head
        while currNode:
            if currNode.next.next is None:
                currNode.next = None
                return
            currNode = currNode.next 
        self.size -= 1 
    
    # Get Ending Element
    def getTail(self): # Time Complexity O(n)
        if self.head is None: return "List is empty"

        currNode = self.head
        while currNode:
            if currNode.next is None:
                return currNode.data
            currNode = currNode.next 

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
sll = sLinkedList()
sll.insertAtBeginning(1)
sll.insertAtBeginning(2)
sll.insertAtBeginning(2)
sll.insertAtBeginning(5)
sll.removeAtBeginning()


print(str(sll)) #[2 2 1 ]
print(sll.getHead())  #2

sll.insertAtEnd(0)
sll.insertAtEnd(-1)
sll.insertAtEnd(-2)
sll.insertAtEnd(-3)
sll.removeAtEnd()

print(str(sll)) #[2 2 1 0 -1 -2 ]
print(sll.getTail()) #-2
print(len(sll)) #6

sll.delete(5)
print(str(sll)) #[2 2 1 0 -1]
print(len(sll)) #5

sll.insertAfter(sll.head.next, 9)
print(str(sll)) #[2 2 9 1 0 -1]
print(len(sll)) #6

print(sll.contains(50)) # False
print(sll.contains(0)) # True

sll.clear()
print(len(sll)) # 0
print(sll.isEmpty()) # True