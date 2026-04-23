from agents.ml_agent import MLAgent


def main():
    agent = MLAgent()

    fault = "A-E"
    result = agent.predict_path(fault)

    print("🔍 Fault:", fault)
    print("🤖 Predicted Path:", result)


if __name__ == "__main__":
    main()