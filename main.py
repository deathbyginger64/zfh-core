from network.graph import NetworkGraph
from faults.injector import FaultInjector
from agents.ml_agent import MLAgent


def main():
    net = NetworkGraph()
    net.create_sample_network()

    print("\n--- INITIAL NETWORK ---")
    net.display()

    graph = net.get_graph()
    injector = FaultInjector(graph)

    edges = list(graph.edges())
    u, v = edges[0]
    injector.break_link(u, v)

    fault_edge = f"{u}-{v}"

    print("\n--- AFTER FAULT ---")
    net.display()

    # Active links
    active_links = sum(
        1 for (x, y) in graph.edges()
        if graph[x][y]["status"] == "up"
    )

    agent = MLAgent()
    predicted_path = agent.predict_path(fault_edge, active_links, graph)

    print("\n🤖 ML Predicted Path:", predicted_path)

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