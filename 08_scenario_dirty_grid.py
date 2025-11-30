# Cell 8: Scenario 2 - The Dirty Grid Test

print("="*60)
print("🧪 TEST SCENARIO 2: High Carbon Grid")
print("="*60)

# force a scenario where the user wants to run a heavy job
# The Agent should detect high carbon (simulated or real) and suggest a delay
user_request = "I have a massive data processing job (500GB). It is not urgent. When should I run it?"

run_turn(user_request)

print("\n⏳ Cooldown: Waiting 10s to respect API Rate Limits...")
time.sleep(10)