# Cell 9: Scenario 3 - Predictive Forecasting

print("="*60)
print("🧪 TEST SCENARIO 3: Future Intelligence")
print("="*60)

# ask the agent to prove its work by showing the data
user_request = "Can you show me the Carbon Forecast for the next 24 hours? I want to see the data."

run_turn(user_request)

print("\n⏳ Cooldown: Waiting 10s to respect API Rate Limits...")
time.sleep(10)