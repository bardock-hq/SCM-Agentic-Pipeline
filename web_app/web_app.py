import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="Supply Chain & AI Engineering Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #0072FF, #00C6FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #64748B;
        margin-bottom: 1.5rem;
    }
    .profile-card {
        background-color: #0F172A;
        border: 1px solid #1E293B;
        border-radius: 12px;
        padding: 1.5rem;
        color: #F8FAFC;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar - About Me
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400", width=120)
    st.title("About Me")
    st.write("👋 Hi! I build autonomous AI pipelines and supply chain analytics engines powered by Gemini & CrewAI.")
    st.markdown("---")
    st.markdown("🔗 **Connect with me:**")
    st.markdown("[💼 LinkedIn Profile](https://linkedin.com)")
    st.markdown("[🦋 Bluesky Feed](https://bsky.app)")
    st.markdown("[🐙 GitHub Repository](https://github.com/bardock-hq/SCM-Agentic-Pipeline)")

# Main Hero
st.markdown('<div class="hero-title">Autonomous AI & Supply Chain Portfolio</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Driven by Multi-Agent Intelligence (CrewAI + Gemini 2.0) & Automated Social Distribution</div>', unsafe_allow_html=True)

st.divider()

# Live System Status Metrics
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.metric(label="Agent Crew", value="CrewAI Core", delta="Active")
with c2:
    st.metric(label="LLM Brain", value="Gemini 2.0 Flash", delta="Connected")
with c3:
    st.metric(label="Social Auto-Publish", value="LinkedIn & Bluesky", delta="Automated")
with c4:
    st.metric(label="Media Studio", value="Google Flow AI", delta="Enabled")

st.divider()

# Tabs Layout
tab1, tab2, tab3 = st.tabs(["🚀 Live Market Intelligence", "🎬 Google Flow AI Media", "⚙️ System Architecture"])

with tab1:
    st.subheader("📰 Latest Autonomous SCM Intelligence Briefing")
    st.info("🤖 **CrewAI Agent Execution:** Autonomous analysis generated via RSS feed scrapers and Gemini LLM.")
    
    with st.expander("📌 View Executive Briefing", expanded=True):
        st.markdown("""
        **Global Logistics Overview:**
        * Container throughput across key transit hubs remains steady.
        * Intermodal rail safety buffers adjusted to mitigate West Coast delays.
        
        **Action Plan:**
        1. Shift spot freight to intermodal transport.
        2. Automate daily summaries to LinkedIn and Bluesky.
        """)

with tab2:
    st.subheader("🎬 Google Flow AI Studio")
    st.write("Incorporating AI-generated media from **Google Flow** into supply chain presentations.")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")  # Placeholder for Google Flow AI generated clip

with tab3:
    st.subheader("⚙️ Live CrewAI & Social Publisher Log")
    st.json({
        "crewai_status": "ONLINE",
        "llm_engine": "gemini-2.0-flash",
        "social_targets": ["LinkedIn", "Bluesky"],
        "cloud_automation": "GitHub Actions (08:00 UTC)"
    })