import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- PAGE SETUP ---
st.set_page_config(page_title="CyberShield SOC", layout="wide")

# Custom CSS for the "Dark Security" look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True) # FIXED THIS LINE

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=" ", # your sql workbench password
        database="cyber_security_db"
    )

# --- HEADER ---
st.title("🛰️ CyberShield: SOC Dashboard")
st.write(f"System Time: {datetime.now().strftime('%H:%M:%S')} | Status: ✅ Active")

try:
    conn = get_db_connection()
    df = pd.read_sql("SELECT * FROM ThreatLogs ORDER BY id DESC", conn)
    conn.close()

    if not df.empty:
        # Metrics Row
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Alerts", len(df))
        col2.metric("Unique IPs", df['source_ip'].nunique())
        col3.metric("Critical Threats", len(df[df['severity_level'] >= 5]))

        # Charts Row
        c1, c2 = st.columns(2)
        with c1:
            fig_pie = px.pie(df, names='event_type', title="Threat Types", template="plotly_dark")
            st.plotly_chart(fig_pie)
        with c2:
            top_ips = df['source_ip'].value_counts().head(5).reset_index()
            fig_bar = px.bar(top_ips, x='source_ip', y='count', title="Top Attackers", template="plotly_dark")
            st.plotly_chart(fig_bar)

        # Data Table
        st.subheader("Live Incident Logs")
        st.dataframe(df, use_container_width=True)
    else:
        st.info("System standby. No threats detected in logs.")

except Exception as e:
    st.error(f"Database Error: {e}")

if st.button("Refresh Dashboard"):
    st.rerun()
