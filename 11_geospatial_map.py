# Cell 11: Generate Geospatial Command Center
import folium

def create_geo_map():
    print("🗺️ GENERATING ENTERPRISE DASHBOARD: GEO-MAP")
    
    # Center on Europe
    m = folium.Map(location=[50, 5], zoom_start=4, tiles="CartoDB dark_matter")
    
    # Define Data Centers
    datacenters = [
        {"name": "UK-South (London)", "coords": [51.50, -0.12], "status": "GREEN", "carbon": 90},
        {"name": "EU-Central (Frankfurt)", "coords": [50.11, 8.68], "status": "DIRTY", "carbon": 340},
        {"name": "EU-West (Paris)", "coords": [48.85, 2.35], "status": "GREEN", "carbon": 55},
        {"name": "US-East (N. Virginia)", "coords": [39.04, -77.48], "status": "MODERATE", "carbon": 210}
    ]
    
    for dc in datacenters:
        color = "green" if dc["status"] == "GREEN" else "red"
        if dc["status"] == "MODERATE": color = "orange"
        
        popup_text = f"""
        <b>{dc['name']}</b><br>
        Status: {dc['status']}<br>
        Carbon: {dc['carbon']}g
        """
        
        folium.Marker(
            location=dc["coords"],
            popup=popup_text,
            icon=folium.Icon(color=color, icon="cloud", prefix="fa")
        ).add_to(m)
        
        # Connect them to show "Network"
        folium.PolyLine(
            locations=[[51.50, -0.12], dc["coords"]],
            color="cyan", weight=0.5, opacity=0.3
        ).add_to(m)
        
    filename = "greenops_map.html"
    m.save(filename)
    print(f"✅ Interactive Map generated: {filename}")
    return filename

# Run it
map_file = create_geo_map()