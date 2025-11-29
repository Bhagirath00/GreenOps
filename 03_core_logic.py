# Cell 3: Logic Classes (Fixed Forecast)

class CarbonIntensityFetcher:
    """Fetches REAL-TIME carbon intensity from UK National Grid API."""
    BASE_URL = "https://api.carbonintensity.org.uk"
    
    def get_current_intensity(self) -> Dict:
        """Get current carbon intensity for UK."""
        try:
            # 1. Try Real API
            response = requests.get(f"{self.BASE_URL}/intensity", timeout=5)
            data = response.json()["data"][0]
            print(f"   📡 [API] Fetched Real-Time Intensity: {data['intensity']['actual']} gCO2/kWh")
            return {
                "intensity": data["intensity"]["actual"],
                "index": data["intensity"]["index"],
                "status": "GREEN" if data["intensity"]["actual"] < 200 else "DIRTY"
            }
        except Exception as e:
            print(f"   ⚠️ [API ERROR] Could not fetch live data: {e}")
            # 2. Fallback Simulation (If API fails)
            return {"intensity": 180, "index": "low", "status": "GREEN (Simulated - API Offline)"}
    
    def get_forecast(self, hours: int = 24) -> List[Dict]:
        """Get carbon intensity forecast for next N hours."""
        hours = int(hours) # Safety Cast
        try:
            # 1. Try Real API (Correct Endpoint)
            response = requests.get(f"{self.BASE_URL}/intensity/forecast", timeout=5)
            data = response.json()["data"]
            print(f"   📡 [API] Fetched Real-Time Forecast for {hours} hours.")
            return [{"time": item["from"], "intensity": item["intensity"]["forecast"]} for item in data[:hours]]
        except Exception as e:
            # 2. Fallback Simulation (Duck Curve)
            print(f"   ⚠️ [API ERROR] Forecast API Failed: {e}. Switching to Simulation.")
            now = datetime.now()
            return [
                {
                    "time": (now + timedelta(hours=i)).isoformat(), 
                    "intensity": 200 + int(50 * np.sin(i/24 * 2 * np.pi)) # Simulated curve
                } 
                for i in range(hours)
            ]

class DevOpsTaskManager:
    """Manages the deployment queue."""
    def __init__(self):
        self.tasks = []
    
    def create_task(self, name: str, carbon_data: Dict, scheduled_for: str = None):
        task = {
            "id": len(self.tasks) + 1,
            "name": name,
            "carbon_at_creation": carbon_data.get('intensity', 0),
            "status": "SCHEDULED" if scheduled_for else "DEPLOYED",
            "timestamp": scheduled_for if scheduled_for else datetime.now().isoformat()
        }
        self.tasks.append(task)
        return task

# Initialize Logic
carbon_fetcher = CarbonIntensityFetcher()
task_manager = DevOpsTaskManager()
print("✅ Logic Classes Updated (Real-Time Priority).")