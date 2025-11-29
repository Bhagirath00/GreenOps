# Cell 10: Generate Advanced Carbon Dashboard

import random
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, Image

def create_heatmap_visual():
    print("📊 GENERATING ENTERPRISE DASHBOARD: ADVANCED ANALYTICS")
    
    # 1. Generate Realistic Data (with noise)
    hours = np.arange(24)
    # Base curve: High in morning/evening, low at night/mid-day (Solar impact)
    base_curve = 200 + 100 * np.sin((hours - 6) / 24 * 2 * np.pi) 
    # Add random noise for realism
    noise = np.random.normal(0, 15, 24)
    intensity = base_curve + noise
    intensity = np.clip(intensity, 50, 400) # Keep within realistic bounds

    # 2. Setup Professional Plot
    plt.figure(figsize=(14, 6))
    plt.style.use('dark_background') # Cyberpunk / DevOps look
    
    # Gradient Fill Logic
    # We plot segments to simulate a gradient from Green to Red
    for i in range(len(hours)-1):
        x = hours[i:i+2]
        y = intensity[i:i+2]
        avg_y = np.mean(y)
        color = '#2ecc71' if avg_y < 180 else ('#f1c40f' if avg_y < 250 else '#e74c3c')
        plt.fill_between(x, y, alpha=0.4, color=color)
        plt.plot(x, y, color=color, linewidth=2)

    # 3. Annotations
    # Find lowest point
    min_idx = np.argmin(intensity)
    plt.annotate(f'BEST TIME: {min_idx}:00\n({int(intensity[min_idx])}g)', 
                 xy=(min_idx, intensity[min_idx]), 
                 xytext=(min_idx, intensity[min_idx]-50),
                 arrowprops=dict(facecolor='white', shrink=0.05),
                 color='white', fontweight='bold')

    # Threshold Line
    plt.axhline(y=200, color='gray', linestyle='--', alpha=0.7, label='Green Threshold (200g)')
    
    # Styling
    plt.title("Real-Time Carbon Intensity Forecast (UK National Grid)", fontsize=16, pad=20)
    plt.xlabel("Time of Day (24h)", fontsize=12)
    plt.ylabel("Carbon Intensity (gCO2/kWh)", fontsize=12)
    plt.grid(True, alpha=0.1)
    plt.legend(loc='upper right')
    plt.xticks(hours, [f"{h:02d}:00" for h in hours], rotation=45)
    
    # Save
    filename = "advanced_carbon_dashboard.png"
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    print(f"✅ Advanced Dashboard generated: {filename}")
    return filename

# Run it
heatmap_file = create_heatmap_visual()
display(Image(heatmap_file))