class Graph_BFS:
    def __init__(self):
        """Initializing a Dictionary to store KeyValue Pair"""
        self.graph = dict()

    def addEdge(self, u, v):
        """If the key is already not present in Map, you create one, if already present, you append the value"""
        if self.graph.get(u) is None:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)

    def BFS(self, start_node):
        visited = [False] * len(self.graph)
        queue = [start_node]
        visited[start_node] = True

        while queue:
            curr_node = queue.pop(0)
            print(str(curr_node))
            """Similarly, if the node is present in Map and if it has adjacent nodes and if it has nodes which are not visited yet,
            we append it to the queue"""
            if not self.graph.get(curr_node) is None:
                for i in self.graph[curr_node]:
                    if not visited[i]:
                        queue.append(i)
                        visited[i] = True


if __name__ == '__main__':
    g = Graph_BFS()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("BFS of the graph is ")
    g.BFS(0)
