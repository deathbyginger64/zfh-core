# Zero Fault Horizon (ZFH) — AI-Driven Self-Healing Network System

> A modular AI-powered network resilience platform that simulates network failures, performs intelligent rerouting, and learns recovery strategies using Machine Learning.

---

## 🚧 Project Status

This project is under active development and evolving in phases.

| Phase | Description | Status |
|---|---|---|
| V1 | Rule-based topology restoration | ✅ Complete |
| V2 | Dynamic ML-based rerouting engine | ✅ Complete |
| V3 | Root Cause Analysis (RCA) Agent | 🔄 Starting |
| V4 | Optimization & Multi-Agent Intelligence | ⏳ Planned |

---

## 🧠 Project Vision

Zero Fault Horizon (ZFH) aims to simulate a future-ready autonomous network resilience platform capable of:

- Detecting failures
- Diagnosing root causes
- Predicting recovery actions
- Self-healing network paths
- Optimizing traffic dynamically

The long-term goal is to evolve toward an intelligent multi-agent telecom/network management system.

---

## 🔥 Current Capabilities

### ✅ Network Simulation
- Dynamic graph-based network modeling
- Randomized edge weights
- Real-time topology visualization in terminal

### ✅ Fault Injection Engine
- Simulates realistic link failures
- Random fault generation
- Edge status management (`up/down`)

### ✅ Rule-Based Recovery (V1)
- Deterministic topology restoration
- Shortest-path rerouting using graph algorithms

### ✅ ML-Based Recovery System (V2)
- Supervised learning pipeline
- Dynamic dataset generation
- Feature engineering
- RandomForest-based decision system
- Weight-aware path prediction
- Intelligent rerouting decisions

---

## 🔄 Current System Pipeline

```
Dynamic Network
      ↓
Random Fault Injection
      ↓
Feature Extraction
      ↓
ML-Based Path Prediction
      ↓
Rerouting Decision
      ↓
Network Recovery
```

---

## 🧠 ML Pipeline

### Dataset Generation

The system automatically creates training datasets by:

- Generating dynamic network topologies
- Injecting random faults
- Using a rule-based topology agent as the "teacher"
- Saving optimal recovery paths as labeled data

### Features Used

Current ML features include:

- Fault edge information
- Active link count
- Edge weights
- Dynamic network state

### Model

- **Algorithm:** RandomForestClassifier (scikit-learn)
- **Performance:** ~93% prediction accuracy on dynamic datasets

---

## 📁 Project Structure

```
zfh_core/
├── agents/
│   ├── topology_agent.py
│   └── ml_agent.py
│
├── network/
│   └── graph.py
│
├── faults/
│   └── injector.py
│
├── data/
│   ├── dataset_generator.py
│   └── dataset.csv
│
├── models/
│   ├── train_model.py
│   ├── model.pkl
│   └── path_mapping.pkl
│
├── main.py
├── train.py
├── predict.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

| Area | Technology |
|---|---|
| Language | Python |
| Graph Modeling | NetworkX |
| Machine Learning | scikit-learn |
| Data Handling | Pandas / NumPy |
| Model | RandomForestClassifier |
| Version Control | Git + GitHub |

---

## ⚙️ Setup

**1. Clone Repository:**
```bash
git clone <repo-url>
cd zfh_core
```

**2. Create Virtual Environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies:**
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

**1️⃣ Generate Dataset:**
```bash
python train.py
```
Generates dynamic network scenarios, random failures, and ML training data.

**2️⃣ Train ML Model:**
```bash
python models/train_model.py
```
Preprocesses features, trains the ML model, evaluates accuracy, and saves trained artifacts.

**3️⃣ Run Full System:**
```bash
python main.py
```
Creates the network, injects faults, performs ML-based rerouting, and applies recovery logic.

---

## 🧠 Concepts Implemented

**Networking** — Topology modeling, routing, rerouting, fault tolerance, network resilience

**Machine Learning** — Supervised learning, feature engineering, label encoding, model evaluation, generalization vs memorization

**Software Engineering** — Modular architecture, pipeline design, version control workflows, reproducible environments

---

## 🔭 Future Roadmap

### V3 — Root Cause Analysis Agent
- [ ] Latency simulation
- [ ] Packet loss simulation
- [ ] Traffic load analysis
- [ ] Failure diagnosis engine

### V4 — Multi-Agent Intelligence
- [ ] Optimization agents
- [ ] Predictive maintenance
- [ ] Multi-fault recovery
- [ ] Autonomous orchestration

### V5 — Advanced AI
- [ ] Graph Neural Networks (GNNs)
- [ ] Reinforcement Learning
- [ ] Real-time telemetry ingestion

---

## 👨‍💻 Author

**Aditya Khandelwal**
B.Tech CSE (Cyber Security) · AI + Networking + Autonomous Systems Enthusiast