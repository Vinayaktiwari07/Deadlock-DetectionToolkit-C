class DeadlockDetector:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.rec_stack = set()
        self.cycle_nodes = []

    def detect_cycle(self):
        self.visited.clear()
        self.rec_stack.clear()
        self.cycle_nodes.clear()

        for node in self.graph:
            if node not in self.visited:
                if self.dfs(node):
                    return True
        return False

    def dfs(self, node):
        self.visited.add(node)
        self.rec_stack.add(node)

        for neighbor in self.graph.get(node, []):
            if neighbor not in self.visited:
                if self.dfs(neighbor):
                    self.cycle_nodes.append(neighbor)
                    return True
            elif neighbor in self.rec_stack:
                self.cycle_nodes.append(neighbor)
                return True

        self.rec_stack.remove(node)
        return False

    def get_cycle_nodes(self):
        return list(set(self.cycle_nodes))
