from collections import deque


class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

# Driver program to the above graph class
# if __name__ == "__main__":
#     V = 5
#     graph = Graph(5)
#     graph.add_edge(0, 1)
#     graph.add_edge(0, 4)
#     graph.add_edge(1, 2)
#     graph.add_edge(1, 3)
#     graph.add_edge(1, 4)
#     graph.add_edge(2, 3)
#     graph.add_edge(3, 4)

#     graph.print_graph()


# Simple Representation with a HashMap
graph_elements = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}

graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


# breath First Search 
def search(graph, start, ele):
    queue = deque()
    queue.append(start)
    visited = []

    while queue:
        curr = queue.popleft()
        if curr not in visited:
            if curr == ele:
                return True
            else:
                queue += graph[curr]
                visited.append(curr)

    return False


# TEST Shortest Path Finder
assert search(graph,"you", "bob") == True
assert search(graph, "you", "you") == True
assert search(graph, "you", "nobody") == False

print("ALL PASSED ✔")
