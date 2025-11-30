

<div align="center">

![GreenOps Banner](https://capsule-render.vercel.app/api?type=waving&color=00b894&height=200&section=header&text=GreenOps%20Enterprise&fontSize=70&animation=fadeIn&fontAlignY=35&desc=AI-Powered%20Sustainable%20DevOps&descAlignY=55&descAlign=50)

# 🌿 GreenOps Enterprise

[![Gemini 1.5 Flash](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Carbon API](https://img.shields.io/badge/Data-UK%20National%20Grid-00b894?style=for-the-badge&logo=leaf&logoColor=white)](https://carbonintensity.org.uk/)
[![Python](https://img.shields.io/badge/Code-Python%203.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

</div>

---

## 🚀 Overview

**GreenOps** is an autonomous AI agent that optimizes cloud deployments based on real-time carbon intensity. Instead of deploying blindly, it checks the grid status and intelligently schedules workloads for "green windows"—reducing carbon emissions by up to **40%**.

### **Powered By**
*   🧠 **Google Gemini 1.5 Flash**: The reasoning engine that decides *when* to deploy.
*   🔌 **UK National Grid Carbon Intensity API**: Real-time energy generation data (Wind, Solar, Gas, Coal).

---

## 💻 Want to Run Locally?

We have a dedicated local execution mode for testing on your laptop!

👉 **[Click Here for Local Setup Guide](Local/README_LOCAL.md)**

*(Includes instructions for API keys, dependencies, and running the simulation script)*

---

## 📋 The Problem vs. Solution

### **The Problem: Invisible Carbon**
*   Cloud computing emits **more carbon than the airline industry**.
*   Deploying a heavy job at **6 PM (Coal/Gas)** = **300g CO2/kWh**.
*   Deploying the same job at **2 AM (Wind)** = **<50g CO2/kWh**.
*   Most DevOps tools **ignore this completely**.

### **The Solution: Autonomous Agent**
GreenOps acts as a "Sustainability Gatekeeper":
1.  **Intercepts** deployment requests.
2.  **Checks** live grid data via API.
3.  **Decides**:
    *   ✅ **Green Grid?** Deploy immediately.
    *   🏭 **Dirty Grid?** Schedule for later (e.g., 3 AM).
    *   🚨 **Critical Emergency?** Override and deploy instantly.

---

## 🏗️ Architecture

```mermaid
graph TD
    User[👤 User Request] --> Agent[🤖 Gemini Agent]
    Agent --> Tools{🧰 Agent Tools}
    
    Tools -->|Get Intensity| GridAPI[🔌 UK National Grid API]
    Tools -->|Calculate| Forecast[Pre-computed Forecast]
    
    GridAPI -->|Return Data| Agent
    
    Agent -->|Decision| Action{⚡ Action}
    Action -->|Green (<200g)| Deploy[✅ Deploy Now]
    Action -->|Dirty (>200g)| Schedule[🕒 Schedule for 3 AM]
    Action -->|Critical| Override[🚨 Emergency Override]
```

---

## 🧪 Real-World Scenarios

| Scenario | Grid Status | Agent Decision | Impact |
|:---|:---|:---|:---|
| **Nightly Build** | 🏭 Dirty (Gas) | **Wait 6 hours** for Wind peak | 📉 **-84% Carbon** |
| **Security Hotfix** | 🏭 Dirty (Gas) | **Deploy Immediately** (Critical) | 🛡️ **Safety First** |
| **Data Migration** | ☁️ Moderate | **Wait 22 hours** for Solar peak | 🤝 **Human Choice** |

---

## 📂 Repository Structure

```
GreenOps/
├── 01_setup_dependencies.py    # Kaggle Cell 1
├── ...                         # (Other Kaggle Cells)
├── 12_final_report.py          # Kaggle Cell 12
├── Local/                      # 💻 LOCAL EXECUTION FOLDER
│   ├── greenops_local.py       # Run this on your laptop!
│   └── README_LOCAL.md         # Instructions
├── greenops_map.html           # Generated Output
└── README.md                   # This file
```

---

## 🙏 Acknowledgments

Built for the **Google AI Agents Hackathon** (November 2025).

*   **LLM**: Gemini 1.5 Flash
*   **Data**: Carbon Intensity API (National Grid ESO)

---

<div align="center">

**Code Smarter. Breathe Easier.** 🌿

</div>
