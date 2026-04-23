# Zero Fault Horizon (ZFH) — Core System

> An AI-driven self-healing network system that simulates network failures and uses Machine Learning to predict optimal rerouting paths.

---

## 🧠 Features

- **Network Simulation** — Graph-based network modeling using NetworkX
- **Fault Injection** — Realistic link failure simulation
- **Rule-Based Agent (V1)** — Deterministic fault response logic
- **ML-Based Agent (V2)** — Intelligent, model-driven path decisions
- **Dataset Generation Pipeline** — Automated training data creation
- **Model Training** — Random Forest classifier for path prediction

---

## 🔄 System Flow

```
Network → Fault Injection → ML Model → Path Prediction → Fix Applied
```

---

## 📁 Project Structure

```
zfh_core/
├── agents/             # Rule-based and ML-based agents
├── network/            # Network topology and graph logic
├── faults/             # Fault injection modules
├── data/               # Generated datasets
├── models/             # Trained ML models
├── main.py             # Entry point — runs the full system
├── train.py            # Dataset generation pipeline
└── predict.py          # Inference and path prediction
```

---

## ⚙️ Setup

```bash
git clone <repo-url>
cd zfh_core
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## ▶️ Usage

**1. Generate dataset:**
```bash
python train.py
```

**2. Train the model:**
```bash
python models/train_model.py
```

**3. Run the system:**
```bash
python main.py
```

---

## 🔭 Future Work

- [ ] Multi-fault handling
- [ ] Graph Neural Networks (GNN) integration
- [ ] Root Cause Analysis agent
- [ ] Network optimization agent

---

## 👨‍💻 Author

**Aditya Khandelwal**
