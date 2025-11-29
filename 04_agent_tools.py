# Cell 4: Define Enterprise Agent Tools (Fixed Return Types)

def get_carbon_intensity():
    return carbon_fetcher.get_current_intensity()

def get_carbon_forecast(hours: int = 24):
    return {"forecast": carbon_fetcher.get_forecast(hours)}

def find_greenest_window(hours: int = 24, duration: int = 2):
    forecast = carbon_fetcher.get_forecast(hours)
    
    # FIX: Ensure we return a Dict, not a String
    if not forecast or "error" in forecast[0]:
        return {"error": "Forecast unavailable, using current data fallback."}
        
    best_window = None
    min_avg = 1000
    
    try:
        for i in range(len(forecast) - duration):
            window = forecast[i:i+duration]
            avg = sum(f['intensity'] for f in window) / duration
            if avg < min_avg:
                min_avg = avg
                best_window = {
                    "start_time": window[0]['time'],
                    "end_time": window[-1]['time'],
                    "avg_carbon": round(avg, 2)
                }
    except Exception as e:
        return {"error": f"Calculation error: {str(e)}"}
            
    return best_window if best_window else {"message": "No window found"}

def deploy_task(task_name: str, scheduled_for: str = None):
    current_data = carbon_fetcher.get_current_intensity()
    return task_manager.create_task(task_name, current_data, scheduled_for)

def get_deployment_stats():
    return {
        "total_jobs": len(task_manager.tasks),
        "status_breakdown": [f"{t['name']}: {t['status']}" for t in task_manager.tasks]
    }

tools_list = [get_carbon_intensity, get_carbon_forecast, find_greenest_window, deploy_task, get_deployment_stats]
print("✅ Enterprise Tools Defined (Type-Safe).")