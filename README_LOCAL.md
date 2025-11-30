# 💻 Running GreenOps Locally

Yes! You can run GreenOps on your laptop.

## Prerequisites
1.  **Python 3.10+** installed.
2.  **Gemini API Key** (Get it from [Google AI Studio](https://aistudio.google.com/apikey)).

## Quick Start

### 1. Install Dependencies
Open your terminal/command prompt and run:
```bash
pip install -r requirements.txt
```

### 2. Set Your API Key
You can set it as an environment variable (recommended):
**Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY="your_actual_api_key_here"
```
**Mac/Linux:**
```bash
export GOOGLE_API_KEY="your_actual_api_key_here"
```

*Or just run the script, and it will ask you to paste the key.*

### 3. Run the Agent
```bash
python greenops_local.py
```

## What Happens?
The script will:
1.  Connect to the UK National Grid.
2.  Initialize the Gemini 1.5 Flash agent.
3.  Run through 3 scenarios automatically:
    *   **Scenario A**: Routine deployment check.
    *   **Scenario B**: Scheduling a heavy job.
    *   **Scenario C**: Critical security override.
4.  Print a summary report at the end.

## Troubleshooting
*   **"Module not found"**: Make sure you ran `pip install -r requirements.txt`.
*   **"API Key Error"**: Ensure you pasted the key correctly without spaces.
*   **"429 Resource Exhausted"**: You hit the free tier limit. Wait a minute and try again.
