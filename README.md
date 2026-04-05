# Cyber-Shield-Analytics
CyberShield Analytics is a full-stack cybersecurity monitoring solution designed to detect, log, and visualize potential network threats in real-time. 
By combining a Python-based "Watcher" script with a Streamlit web interface and a MySQL backend, this system provides security analysts with an instant view of system health and risk levels.

<p>
  <img src="cybershield_dashboard.png" width="700"/>
</p>

## Key Features:
- Live Log Monitoring: Automatically scans server logs for keywords like "FAILED" or "ATTACK."
- Dynamic Risk Scoring: Calculates threat levels based on event severity and asset criticality.
- Interactive Dashboard: Displays total alerts, unique attackers, and threat distribution using Plotly charts.
- Database Integration: Securely stores all incident data in a MySQL database for long-term audit trails.

## Tech Stack
- Frontend: Streamlit (Python)
- Backend: Python 3.x
- Database: MySQL
- Development Environment: VS Code

## How to Run the System

### 1. Set Up the Database
- Open your MySQL Workbench.
- Create a cyber_security_db database
- Run the provided cyber_security_db.sql to create the tables & storing for data

### 3. Install Dependencies
```python
pip install streamlit mysql-connector-python plotly pandas
```

### 4. Run the Detector
Open a terminal and start the background script that monitors the logs:
```python
python detector.py
```
<p>
  <img src="showcase_&_results/run_detector.png" width="700"/>
</p>

### 5. Launch the Dashboard
Open a second terminal and run the UI:
```python
streamlit run ap.py
```
<p>
  <img src="showcase_&_results/run_ap.png" width="700"/>
</p>

### 6. How It Works (The Logic)Detection: 
The detector.py script acts as a "Watcher." it stays active (using a while loop) and reads the server_access.log file every few seconds.

Analysis: When it finds a threat, it calculates a Risk Score using the formula:
```python
                       Risk Score = Severity * Asset Criticality
```
Storage: The script uses mysql-connector to INSERT the threat details (IP, Type, Timestamp) into your database.
Visualization: The Streamlit app.py queries the database and turns those raw rows of data into beautiful, easy-to-read charts.

### 7. Result Grid
- result_grid1
<p>
  <img src="showcase_&_results/result_grid1.png" width="700"/>
</p>

- result_grid2
<p>
  <img src="showcase_&_results/result_grid2.png" width="700"/>
</p>
