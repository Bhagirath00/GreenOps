# Cell 2: Configure Gemini API
from kaggle_secrets import UserSecretsClient

try:
    user_secrets = UserSecretsClient()
    # Ensure your Secret is named 'GEMINI_API_KEY' or 'GOOGLE_API_KEY'
    # We check for both to be safe
    try:
        api_key = user_secrets.get_secret("GEMINI_API_KEY")
    except:
        api_key = user_secrets.get_secret("GOOGLE_API_KEY")
        
    genai.configure(api_key=api_key)
    print("✅ Gemini API Configured Successfully.")
except Exception as e:
    print(f"❌ Error: Could not retrieve API Key. Check Add-ons -> Secrets. Error: {e}")