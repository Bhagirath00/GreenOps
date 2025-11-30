# Cell 5: Initialize Agent with Dynamic Model Discovery

# 1. Setup Model Architecture with Auto-Discovery
# We stop guessing names and ask the API what is available.

def get_available_model(tools, system_instruction):
    print("🔍 Scanning for available Gemini models...")
    try:
        # List all models available to this API Key
        available_models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                available_models.append(m.name)
        
        print(f"   📋 Found {len(available_models)} models: {available_models}")
        
        # Priority List (prefer Flash, then Pro, then anything else)
        # look for partial matches in the available list
        priority_keywords = ['flash', 'pro', 'gemini']
        
        selected_model_name = None
        
        # Strategy 1: Find best match based on priority
        for keyword in priority_keywords:
            for model_name in available_models:
                if keyword in model_name:
                    selected_model_name = model_name
                    break
            if selected_model_name: break
            
        # Strategy 2: If no keyword match, take the first one
        if not selected_model_name and available_models:
            selected_model_name = available_models[0]
            
        if not selected_model_name:
            raise RuntimeError("No models found that support 'generateContent'.")

        print(f"   � Attempting to use: {selected_model_name}")
        
        # Initialize
        model = genai.GenerativeModel(
            model_name=selected_model_name, 
            tools=tools,
            system_instruction=system_instruction
        )
        
        # Test Connection
        response = model.generate_content("Test connection.")
        print(f"   ✅ Success! Connected to {selected_model_name}")
        return model

    except Exception as e:
        print(f"   ❌ Error during model discovery: {e}")
        raise e

system_instruction = """
You are GreenOps, an Enterprise Carbon-Aware DevOps Assistant.

YOUR CORE MISSION:
Reduce the carbon footprint of cloud computing tasks by optimizing *when* they run.

OPERATIONAL PROTOCOLS:
1. **ALWAYS** check `get_carbon_intensity` before making a deployment decision.
2. **IF Carbon < 200g:** The Grid is GREEN. Deploy Immediately using `deploy_task`.
3. **IF Carbon > 200g:** The Grid is DIRTY.
   - You MUST call `find_greenest_window` to find a better time.
   - Then call `deploy_task` with the `scheduled_for` parameter set to that time.
4. **Explain** your reasoning to the user using the data (e.g., "I saved 40% carbon by waiting until 2 AM").

REPORTING STYLE:
- Be professional, precise, and data-driven.
- Use emojis (🌿, 🏭, 🚀) to indicate status.
"""

# Initialize the best available model
model = get_available_model(tools_list, system_instruction)
print(f"✅ FINAL SELECTED MODEL: {model.model_name}")

# Initialize Chat Session
chat = model.start_chat(enable_automatic_function_calling=False)

# 2. Define Enterprise Retry Logic (The "Anti-Crash" System)
def send_message_safe(message):
    retries = 3
    base_wait = 30
    
    for i in range(retries):
        try:
            return chat.send_message(message)
        except ResourceExhausted:
            wait = base_wait * (i + 1)
            print(f"⚠️ API Rate Limit Reached. Pausing system for {wait}s to recharge...")
            time.sleep(wait)
            print("▶️ Resuming operations...")
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")
            return None
            
    print("❌ Critical Failure: API Quota exhausted after max retries.")
    return None

print("✅ GreenOps Agent Initialized & Online.")