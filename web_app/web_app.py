import streamlit as st
import json
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Supply Chain Intelligence Dashboard",
    page_icon="🚢",
    layout="wide"
)

st.title("🚢 Autonomous Supply Chain Intelligence Pipeline")
st.caption("Powered by CrewAI, Gemini API, and GitHub Actions")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📡 Daily Logistics Brief")
    st.info("Status: Active | Source: Supply Chain Dive RSS")
    
    # Display Intelligence Output
    st.markdown("""
    ### Executive Alert: Freight & Port Disruption
    * **Analysis**: Operational analysis complete via CrewAI Agents.
    * **Action**: Review inland route options and safety stock buffer levels.
    """)

with col2:
    st.subheader("⚙️ System Status")
    st.json({
        "status": "Operational",
        "engine": "Gemini 2.0 Flash",
        "automation": "GitHub Actions",
        "monthly_cost": "$0.00"
    })