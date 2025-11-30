#  Run GreenOps Locally

This folder contains everything you need to run the GreenOps agent on your own machine.

## Prerequisites

1.  **Python 3.10+** installed.
2.  **Gemini API Key** (Get it from [Google AI Studio](https://aistudio.google.com/apikey)).

---

##  Quick Start Guide

### 1. Install Dependencies
Open your terminal in this folder and run:

```bash
pip install -r ../requirements.txt
```

### 2. ⚠️ CRITICAL: Upgrade Libraries
To avoid version conflicts, you **MUST** upgrade the Google AI library:

```bash
pip install --upgrade google-generativeai
pip install --upgrade pip
```

*(If you skip this, you might get a `protobuf` or `AttributeError`!)*

### 3. Set Your API Key
**Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY="your_actual_api_key_here"
```
**Mac/Linux:**
```bash
export GOOGLE_API_KEY="your_actual_api_key_here"
```

### 4. Run the Agent
```bash
python greenops_local.py
```

---

##  What to Expect

The script will:
1.  **Connect** to the real UK National Grid API.
2.  **Simulate** 3 scenarios (Microservice, Big Data, Security Patch).
3.  **Print** the agent's reasoning and decisions in real-time.

**Example Output:**
> 🤖 AGENT: The current carbon intensity is 68g (Green). Deploying immediately! 

---

## ❓ Troubleshooting

*   **`AttributeError: whichOneof`**: Run `pip install --upgrade google-generativeai`.
*   **`429 Resource Exhausted`**: You hit the free tier limit. Wait 60 seconds.
*   **`Module not found`**: Ensure you are in the `Local/` folder or pointing to the right `requirements.txt`.
