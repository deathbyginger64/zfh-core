from network.graph import NetworkGraph
from faults.injector import FaultInjector
from agents.ml_agent import MLAgent


def main():
    # Create network
    net = NetworkGraph()
    net.create_sample_network()

    print("\n--- INITIAL NETWORK ---")
    net.display()

    # Inject fault
    injector = FaultInjector(net.get_graph())

    # Get edges and break one
    graph = net.get_graph()
    edges = list(graph.edges())

    if not edges:
        print("❌ No edges to break")
        return

    u, v = edges[0]   # you can randomize later
    injector.break_link(u, v)

    fault_edge = f"{u}-{v}"

    print("\n--- AFTER FAULT ---")
    net.display()

    # ML Agent predicts path
    agent = MLAgent()
    predicted_path = agent.predict_path(fault_edge)

    print("\n🤖 ML Predicted Path:", predicted_path)

    # Apply fix manually (simulate rerouting)
    print("\n🛠 Applying ML-based fix...")

    for i in range(len(predicted_path) - 1):
        u = predicted_path[i]
        v = predicted_path[i + 1]

        if graph.has_edge(u, v):
            graph[u][v]["status"] = "up"

    print("\n--- AFTER ML FIX ---")
    net.display()


if __name__ == "__main__":
    main()