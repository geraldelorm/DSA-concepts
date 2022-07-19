def breathFirstSearch(root): #BFS # O(n)
    visited = []
    queue = [root]

    while len(queue):
        node = queue.pop(0)
        visited.append(node.value)

        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)

    return str(visited)

# Time O(n)
# Space O(n)