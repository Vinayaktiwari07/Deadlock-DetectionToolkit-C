from graph_manager import ResourceAllocationGraph
from detection import DeadlockDetector
from recovery import DeadlockRecovery

# Create graph
rag = ResourceAllocationGraph()

# Add processes
rag.add_process("P1")
rag.add_process("P2")

# Add resources
rag.add_resource("R1")
rag.add_resource("R2")

# Allocate resources
rag.allocate_resource("R1", "P1")
rag.allocate_resource("R2", "P2")

# Create circular wait (deadlock situation)
rag.request_resource("P1", "R2")
rag.request_resource("P2", "R1")

# Detect deadlock
detector = DeadlockDetector(rag.get_graph())

if detector.detect_cycle():
    print("⚠ Deadlock Detected!")
    cycle_nodes = detector.get_cycle_nodes()
    print("Processes involved:", cycle_nodes)

    # Recovery
    recovery = DeadlockRecovery(rag)
    recovery.terminate_process("P1")

    # Re-check
    detector = DeadlockDetector(rag.get_graph())
    if detector.detect_cycle():
        print("Still Deadlocked!")
    else:
        print("✅ Deadlock Resolved!")
else:
    print("No Deadlock.")


#////additional
# from visualization import GraphVisualizer

# visualizer = GraphVisualizer(rag.get_graph())
# visualizer.draw_graph()
