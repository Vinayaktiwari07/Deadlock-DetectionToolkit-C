import tkinter as tk
from tkinter import messagebox
from graph_manager import ResourceAllocationGraph
from detection import DeadlockDetector
from recovery import DeadlockRecovery
from visualization import GraphVisualizer


class DeadlockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Deadlock Detection & Recovery Toolkit")
        self.root.geometry("500x500")

        self.rag = ResourceAllocationGraph()

        # Title
        tk.Label(root, text="Deadlock Detection Toolkit", font=("Arial", 16, "bold")).pack(pady=10)

        # Process Input
        self.process_entry = tk.Entry(root)
        self.process_entry.pack(pady=5)
        tk.Button(root, text="Add Process", command=self.add_process).pack()

        # Resource Input
        self.resource_entry = tk.Entry(root)
        self.resource_entry.pack(pady=5)
        tk.Button(root, text="Add Resource", command=self.add_resource).pack()

        # Allocate
        tk.Label(root, text="Allocate Resource (R -> P)").pack(pady=5)
        self.alloc_resource = tk.Entry(root)
        self.alloc_resource.pack()
        self.alloc_process = tk.Entry(root)
        self.alloc_process.pack()
        tk.Button(root, text="Allocate", command=self.allocate).pack(pady=5)

        # Request
        tk.Label(root, text="Request Resource (P -> R)").pack(pady=5)
        self.req_process = tk.Entry(root)
        self.req_process.pack()
        self.req_resource = tk.Entry(root)
        self.req_resource.pack()
        tk.Button(root, text="Request", command=self.request).pack(pady=5)

        # Buttons
        tk.Button(root, text="Detect Deadlock", command=self.detect_deadlock, bg="orange").pack(pady=10)
        tk.Button(root, text="Recover Deadlock", command=self.recover_deadlock, bg="red").pack(pady=5)
        tk.Button(root, text="Show Graph", command=self.show_graph, bg="lightblue").pack(pady=5)

        # Status Label
        self.status = tk.Label(root, text="", fg="blue")
        self.status.pack(pady=10)

    def add_process(self):
        p = self.process_entry.get()
        self.rag.add_process(p)
        self.status.config(text=f"Process {p} added")

    def add_resource(self):
        r = self.resource_entry.get()
        self.rag.add_resource(r)
        self.status.config(text=f"Resource {r} added")

    def allocate(self):
        r = self.alloc_resource.get()
        p = self.alloc_process.get()
        self.rag.allocate_resource(r, p)
        self.status.config(text=f"{r} allocated to {p}")

    def request(self):
        p = self.req_process.get()
        r = self.req_resource.get()
        self.rag.request_resource(p, r)
        self.status.config(text=f"{p} requested {r}")

    def detect_deadlock(self):
        detector = DeadlockDetector(self.rag.get_graph())
        if detector.detect_cycle():
            messagebox.showwarning("Deadlock", "Deadlock Detected!")
            self.status.config(text="Deadlock Detected!")
        else:
            messagebox.showinfo("Status", "No Deadlock")
            self.status.config(text="System Stable")

    def recover_deadlock(self):
        detector = DeadlockDetector(self.rag.get_graph())
        if detector.detect_cycle():
            cycle_nodes = detector.get_cycle_nodes()
            for node in cycle_nodes:
                if node.startswith("P"):
                    recovery = DeadlockRecovery(self.rag)
                    recovery.terminate_process(node)
                    break
            self.status.config(text="Recovery Applied")
        else:
            self.status.config(text="No Deadlock to Recover")

    def show_graph(self):
        visualizer = GraphVisualizer(self.rag.get_graph())
        visualizer.draw_graph()


if __name__ == "__main__":
    root = tk.Tk()
    app = DeadlockApp(root)
    root.mainloop()
