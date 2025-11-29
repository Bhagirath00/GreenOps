# Cell 7: Run Full Enterprise Simulation

# Turn 1: Check status for a standard job
# This forces the agent to check the live grid
run_turn("I need to deploy 'AI-Training-Job-v1'. It is a heavy workload. Should I do it now?")

print("⏳ System cooling down (20s)...")
time.sleep(20)

# Turn 2: Ask for a detailed forecast explanation
# This forces the agent to use the Forecast tool
run_turn("Can you explain why? Show me the forecast data for the next 24 hours.")

print("⏳ System cooling down (20s)...")
time.sleep(20)

# Turn 3: Force a constrained decision
# This forces the agent to use the Optimizer and Schedule tools
run_turn("Okay, find the absolute best time in the next 12 hours and schedule the job automatically.")

print("\n✅ DEMO COMPLETE. System entering standby.")