class ResourceAllocationGraph:
    def __init__(self):
        self.graph = {}
        self.processes = set()
        self.resources = set()

    def add_process(self, process):
        if process not in self.processes:
            self.processes.add(process)
            self.graph[process] = []

    def add_resource(self, resource):
        if resource not in self.resources:
            self.resources.add(resource)
            self.graph[resource] = []

    def request_resource(self, process, resource):
        # Edge: Process -> Resource
        if process in self.graph and resource in self.graph:
            self.graph[process].append(resource)

    def allocate_resource(self, resource, process):
        # Edge: Resource -> Process
        if resource in self.graph and process in self.graph:
            self.graph[resource].append(process)

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)

    def get_graph(self):
        return self.graph
