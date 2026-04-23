# Zero Fault Horizon (ZFH) - Core System

## 🚀 Overview
This project is a prototype of an AI-driven self-healing network system.

It simulates network failures and uses Machine Learning to predict optimal rerouting paths.

---

## 🧠 Features

- Network simulation using graphs (NetworkX)
- Fault injection (link failures)
- Rule-based agent (V1)
- ML-based agent (V2)
- Dataset generation pipeline
- Model training using Random Forest

---

## 🔄 System Flow

Network → Fault → ML Model → Path Prediction → Fix Applied

---

## 📁 Project Structure


zfh_core/
├── agents/
├── network/
├── faults/
├── data/
├── models/
├── main.py
├── train.py
├── predict.py


---

## ⚙️ Setup

```bash
git clone <repo-url>
cd zfh_core
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
▶️ Run

Generate dataset:

python train.py

Train model:

python models/train_model.py

Run system:

python main.py
🧠 Future Work
Multi-fault handling
Graph Neural Networks
Root Cause Analysis agent
Network optimization agent
👨‍💻 Author

Aditya Khandelwal
