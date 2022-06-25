from collections import deque

class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.value = value
        self.right = None

class BST:
    def __init__(self) -> None:
        self.size = 0
        self.root = None

    def __len__(self) -> int:
        return self.size

    def insert(self, value): # O(log^n)
        if self.root == None:
            self.root = Node(value)
            self.size += 1
            return
        else:
            self.__insert(self.root, value)

    def __insert(self, root, value):
        new_node = Node(value)
        if root.value == value:
            return False
        elif root.value > value:
            if root.left is None:
                root.left = new_node
                self.size += 1
                return
            self.__insert(root.left, value)                
        else:
            if root.right is None: 
                root.right = new_node
                self.size += 1
                return  
            self.__insert(self.right, value)

    def findMin(self): # O(log^n)
        curr_node = self.root
        while curr_node.left:
            curr_node = curr_node.left

        return curr_node.value

    def findMax(self): # O(log^n)
        curr_node = self.root
        while curr_node.right:
            curr_node = curr_node.right

        return curr_node.value

    def isEmpty(self): # O(1)
        return self.size == 0

    def contains(self, value): # O(log^n)
        curr_node = self.root
        while curr_node:
            if value == curr_node.value:
                return True
            elif value > curr_node.value:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left
        return False  

    def traverse(self, order):
        if self.root is None:
            return "Tree is Empty"
        if order == "pre":
            return self.__preOrder(self.root)
        if order == "in":
            return self.__inOrder(self.root)
        if order == "post":
            return self.__postOrder(self.root)

    def __preOrder(self, root, output = []): #DFS # O(n)
        if root.value:
            output.append(root.value)
        if root.left:
            self.__preOrder(root.left, output)
        if root.right:
            self.__preOrder(root.right, output)
        return str(output)


    def __inOrder(self, root, output = []): #DFS # O(n)
        if root.left:
            self.__inOrder(root.left, output)
        if root.value:
            output.append(root.value)
        if root.right:
            self.__inOrder(root.right, output)
        return str(output)

    def __postOrder(self, root, output = []): #DFS # O(n)
        if root.left:
            self.__postOrder(root.left, output)
        if root.right:
            self.__postOrder(root.right, output)
        if root.value:
            output.append(root.value)
        return str(output)

# External Operations 

def breathFirstSearch(root): #BFS # O(n)
    visited = []
    queue = [root]

    while len(queue):
        node = queue.pop(0)
        visited.append(node.value)

        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

    return str(visited)
        

def height(root): # O(n)
    if root is None: return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    return max(leftHeight, rightHeight) + 1

def findMin(node): # O(log^n)
    curr_node = node
    while curr_node.left:
        curr_node = curr_node.left

    return curr_node

def remove(root, value): # O(log^n)
    if root is None: return "Tree is Empty"

    if root.value < value:
        root.right = remove(root.right, value)
    if root.value > value:
        root.left = remove(root.left, value)

    if root.value == value:
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp = findMin(root.right)
        root.key = temp.key
        root.right = remove(root.right, temp.key)
 
    return root



# test
tree = BST()
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(3)

assert tree.isEmpty() == False
assert len(tree) == 4
assert height(tree.root) == 3
assert tree.findMax() == 6
assert tree.findMin() == 3
assert tree.contains(1) == False
assert tree.contains(4) == True

assert tree.traverse("pre") == "[5, 4, 3, 6]"
assert tree.traverse("in") == "[3, 4, 5, 6]"
assert tree.traverse("post") == "[3, 4, 6, 5]"

assert breathFirstSearch(tree.root) == "[5, 4, 6, 3]"

remove(tree.root, 3)
assert breathFirstSearch(tree.root) == "[5, 4, 6]"
