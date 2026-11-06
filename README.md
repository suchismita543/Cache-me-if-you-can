# ☀️ CoolRoute: Heat-Aware Pedestrian Navigation System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20App-green.svg)](https://flask.palletsprojects.com/)
[![OSMnx](https://img.shields.io/badge/OSMnx-NetworkX-orange.svg)](https://osmnx.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **"Walking in extreme heat is a health risk, not just an inconvenience."** CoolRoute is an intelligent, microclimate-aware pedestrian routing engine that computes optimal paths by balancing travel time against thermal exposure, shade coverage, and hydration refuge points.

---

## 📌 The Problem & The Gap
Traditional commercial navigation tools (like Google Maps) optimize strictly for distance and speed, ignoring solar radiation, surface albedo heat retention, and canopy shade. During severe heatwaves in urban centers like Bhubaneswar, these time-only algorithms force pedestrians onto high-stress, heat-trapping asphalt routes.

**CoolRoute** bridges this gap by introducing transparent, multi-criteria trade-off pathfinding grounded in urban computing research.

---

## 📐 The Math: Transparent Trade-off Formula
CoolRoute utilizes a composite cost function for network edge weighting:

$$\text{Cost} = [\alpha \times \text{Time}] + [\beta \times \text{Heat Score}]$$

Where the **Heat Score ($X$)** dynamically aggregates:
*   **Base Air Temperature & Humidity:** Sourced from NASA POWER telemetry data.
*   **Surface Thermodynamics:** Distinguishing heat absorption between asphalt, concrete, dirt, and grass.
*   **Shade Mitigation:** Factoring in building shadows and tree canopies.
*   **Refuge Intelligence:** Factoring in proximity to drinking water amenities and rest stops.
*   **$\alpha$ and $\beta$ Weight Coefficients:** Hyperparameters controlling the user's trade-off between speed and thermal comfort.

---

## 🛠️ Project Architecture & Pipeline

Our spatial data processing pipeline operates sequentially from raw data ingestion to web routing:

1.  **Data Extraction (`01_fetch_graph.py`, `02_fetch_buildings.py`, `03_fetch_trees.py`):** Downloads OSM pedestrian networks, building footprints, and green spaces.
2.  **Shadow & Microclimate Projection (`05_project_shadows.py`, `06_apply_shade.py`):** Calculates sun altitude/azimuth to map spatial shade coverage over walking edges.
3.  **Thermal Scoring (`07_calculate_heat_score.py`):** Computes edge-level thermal penalties based on surface material and time-of-day multipliers.
4.  **Pathfinding (`08_route_finder.py`):** Computes comparative routes (Fastest vs. Coolest) using NetworkX.
5.  **Visualization (`visualize_route.py`):** Renders interactive map overlays comparing the fastest vs. coolest paths.
6.  **Web Backend (`flaskr/` & `app.py`):** Flask application factory rendering the web interface.

---

## 🚀 Getting Started Locally

### **1. Clone the Repository**
```bash
git clone https://github.com/suchismita543/Cache-me-if-you-can.git
cd Cache-me-if-you-can
```

### **2. Create and Activate a Virtual Environment**
```bash
python -m venv myenv
# On Linux/macOS:
source myenv/bin/activate
# On Windows:
# myenv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Flask Web Application**
Using Flask's application factory structure:
```bash
flask --app flaskr run --debug
```
Open your browser and navigate to: **`http://127.0.0.1:5000`**

---

## 📚 Literature Grounding & References
Our project architecture and algorithms draw directly from peer-reviewed research:
1. **Wen, J., et al. (2025).** *Walking Smart in the Heat: A Dynamic Shade-Oriented Pathfinding Approach.* Computers, Environment and Urban Systems. DOI: [10.1016/j.compenvurbsys.2025.102337](https://doi.org/10.1016/j.compenvurbsys.2025.102337)
2. **Buo, I., et al. (2026).** *Cool Routes: Real-Time Human Thermal Exposure Routing.* Building and Environment. DOI: [10.1016/j.buildenv.2026.114622](https://doi.org/10.1016/j.buildenv.2026.114622)
3. **Ma, X., et al. (2025).** *Active Route Choice to Minimize Pedestrian Thermal Discomfort.* Sustainable Cities and Society. DOI: [10.1016/j.scs.2025.106697](https://doi.org/10.1016/j.scs.2025.106697)
4. **Melnikov, V. R., et al. (2022).** *Behavioural Thermal Regulation Explains Pedestrian Path Choices.* Scientific Reports, 12, 2441. DOI: [10.1038/s41598-022-06383-5](https://doi.org/10.1038/s41598-022-06383-5)
5. **Mansour, S., et al. (2026).** *User-Comfort Pathfinding: Multi-Criteria Pedestrian Routing.* ISPRS Int. Journal of Geo-Information, 15(7), 313. DOI: [10.3390/ijgi15070313](https://doi.org/10.3390/ijgi15070313)
6. **Kolaxidis, N., et al. (2025).** *Mitigating Heat Stress by Reducing Solar Exposure in Pedestrian Routing.* Transactions in GIS, 29(6), e70110. DOI: [10.1111/tgis.70110](https://doi.org/10.1111/tgis.70110)

---

## 👥 Team: Cache me if you can
*   Suchismita Singh
*   Swastik Shuvam Behera
*   Tanmaya Mishra
*   G Akila Reddy
