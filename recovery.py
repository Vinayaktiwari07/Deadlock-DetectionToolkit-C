class DeadlockRecovery:
    def __init__(self, rag):
        self.rag = rag

    def terminate_process(self, process):
        graph = self.rag.get_graph()

        # Remove all outgoing edges from process
        graph[process] = []

        # Remove all incoming edges to process
        for node in graph:
            if process in graph[node]:
                graph[node].remove(process)

        print(f"Process {process} terminated to recover from deadlock.")
