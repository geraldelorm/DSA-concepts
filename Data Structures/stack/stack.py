# Linked Stack - stack implemented with a linked list
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.size = 0
        self.top = None

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        output = []
        currNode = self.top
        while currNode:
            output.append(currNode.data)
            currNode = currNode.next
        return str(output)

    # add elements into the stack
    def push(self, data): #Time Complexity = O(1)
        newNode = Node(data)
        if self.top is None:
            self.top = newNode
            self.size += 1
            return

        newNode.next = self.top
        self.top = newNode
        self.size += 1

    # remove elements from the stack
    def pop(self): #Time Complexity = O(1)
        if self.top is None: return "Stack is empty"

        val = self.top.data
        self.top = self.top.next
        self.size -= 1

        return val

    #  return top value without removing
    def peek(self): #Time Complexity = O(1)
        if self.top is None: return "Stack is empty"
        return self.top.data

    # Searching for data in a stack
    def contains(self, data): #Time Complexity = O(n)
        if self.top is None: return "Stack is empty"

        currNode = self.top
        while currNode:
            if currNode.data == data:
                return True
            currNode = currNode.next
        
        return False
    
    def isEmpty(self): #Time Complexity = O(1)
        return self.size == 0





# Test
stack = Stack()
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)

assert str(stack) == "[1, 2, 3, 4, 5]"
assert len(stack) == 5

assert stack.pop() == 1
assert str(stack) == "[2, 3, 4, 5]"

assert stack.peek() == 2
assert str(stack) == "[2, 3, 4, 5]"

assert stack.contains(50) == False
assert stack.contains(4) == True

assert stack.isEmpty() == False


print("ALL PASSED ✔")