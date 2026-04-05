import time
import mysql.connector
import os

# --- CONFIG ---
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Prajakta@567.", # Replace with your password
    "database": "cyber_security_db"
}
LOG_FILE = "server_access.log"

print("CyberShield Sensor: ONLINE")

while True:
    if os.path.exists(LOG_FILE):
        # 1. Read the file
        with open(LOG_FILE, "r") as f:
            content = f.read().strip()
        
        # 2. Check if there is data and if it's a threat
        if content:
            print(f"Data detected: {content}")
            
            if "FAILED" in content.upper():
                print("THREAT FOUND! Connecting to DB...")
                try:
                    conn = mysql.connector.connect(**DB_CONFIG)
                    cursor = conn.cursor()
                    
                    # Get IP (Assumes format: 192.168.1.1, FAILED)
                    ip = content.split(",")[0].strip() if "," in content else "Unknown"
                    
                    cursor.execute(
                        "INSERT INTO ThreatLogs (source_ip, event_type, severity_level, asset_criticality) VALUES (%s, %s, %s, %s)",
                        (ip, "Real-Time Log Alert", 5, 10)
                    )
                    conn.commit()
                    conn.close()
                    print("Dashboard Updated!")
                except Exception as e:
                    print(f"DB Error: {e}")
            
            # 3. WIPE THE FILE (To prevent infinite loops)
            with open(LOG_FILE, "w") as f:
                f.write("")
            print("Sensor Reset (File Cleared).")

    time.sleep(1) # Check every second