from collections import deque, defaultdict

class Graph:
    def __init__(self):
        # Initialize the graph as a defaultdict of lists
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        # Add an edge from u to v and from v to u (since the graph is undirected)
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        # Perform Breadth-First Search (BFS) starting from the 'start' node
        visited = set()  # Set to keep track of visited nodes
        queue = deque([start])  # Queue for BFS
        traversal = []  # List to store the order of traversal

        while queue:
            node = queue.popleft()  # Dequeue a node
            if node not in visited:
                visited.add(node)  # Mark the node as visited
                traversal.append(node)  # Add the node to the traversal list
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)  # Enqueue unvisited neighbors
        
        return traversal

    def dfs(self, start):
        # Perform Depth-First Search (DFS) starting from the 'start' node
        visited = set()  # Set to keep track of visited nodes
        traversal = []  # List to store the order of traversal

        def dfs_recursive(node):
            if node not in visited:
                visited.add(node)  # Mark the node as visited
                traversal.append(node)  # Add the node to the traversal list
                for neighbor in self.graph[node]:
                    dfs_recursive(neighbor)  # Recursively visit all neighbors

        dfs_recursive(start)
        return traversal

    def is_connected(self, start, end):
        # Check if there is a path from 'start' to 'end' using BFS
        visited = set()  # Set to keep track of visited nodes
        queue = deque([start])  # Queue for BFS

        while queue:
            node = queue.popleft()  # Dequeue a node
            if node == end:
                return True  # If the end node is found, return True
            if node not in visited:
                visited.add(node)  # Mark the node as visited
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)  # Enqueue unvisited neighbors
        
        return False  # If the end node is not found, return False

    def shortest_path(self, start, end):
        # Find the shortest path from 'start' to 'end' using BFS
        visited = set()  # Set to keep track of visited nodes
        queue = deque([(start, [start])])  # Queue for BFS, storing (node, path) tuples

        while queue:
            node, path = queue.popleft()  # Dequeue a node and its path
            if node == end:
                return path  # If the end node is found, return the path
            if node not in visited:
                visited.add(node)  # Mark the node as visited
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))  # Enqueue unvisited neighbors with updated path
        
        return None  # If the end node is not found, return None

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    print("BFS Traversal:", g.bfs(0))  # Output the BFS traversal starting from node 0
    print("DFS Traversal:", g.dfs(0))  # Output the DFS traversal starting from node 0
    print("Is Connected (0 to 4):", g.is_connected(0, 4))  # Check if there is a path from node 0 to node 4
    print("Shortest Path (0 to 4):", g.shortest_path(0, 4))  # Find the shortest path from node 0 to node 4