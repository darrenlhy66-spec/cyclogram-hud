import streamlit as st

# --- STREAMLIT PAGE CONFIG ---
st.set_page_config(
    page_title="Cyclogram HUD",
    page_icon="🌌",
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# --- CYBERPUNK NATIVE CSS ---
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    /* Main Background and text setup */
    .stApp {
        background-color: #03080a;
        color: #e0f7fa;
        font-family: 'Rajdhani', sans-serif;
    }
    
    /* Neon Blue Sci-Fi Headers */
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
        color: #00f0ff !important;
        text-shadow: 0 0 10px rgba(0, 240, 255, 0.6), 0 0 20px rgba(0, 240, 255, 0.3);
        letter-spacing: 2px;
        margin-top: 1.5rem !important;
        margin-bottom: 0.5rem !important;
    }
    
    /* Clean custom look for standard text */
    p, span, label {
        font-family: 'Rajdhani', sans-serif !important;
    }

    /* Style checkboxes directly without breaking layout containers */
    .stCheckbox label {
        font-size: 1.15rem !important;
        font-weight: 500 !important;
        color: #b0e0e6 !important;
        padding-top: 5px;
        padding-bottom: 5px;
    }

    /* Telemetry Status Badge */
    .telemetry-badge {
        font-family: 'Orbitron', sans-serif;
        background: rgba(0, 240, 255, 0.1);
        border: 1px solid #00f0ff;
        color: #00f0ff;
        padding: 6px 12px;
        border-radius: 4px;
        font-size: 0.85rem;
        display: inline-block;
        margin-top: 10px;
        margin-bottom: 15px;
        text-shadow: 0 0 5px rgba(0, 240, 255, 0.5);
        box-shadow: 0 0 10px rgba(0, 240, 255, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<h1>CYCLOGRAM</h1>", unsafe_allow_html=True)
st.markdown("<div class='telemetry-badge'>SYSTEM STATUS: READY</div>", unsafe_allow_html=True)
st.write("Pre-Market Analysis & Execution Gates protocol configuration.")

# --- SECTION 1: PRE-MARKET ---
st.markdown("<h3>⚡ Pre-Market Analysis</h3>", unsafe_allow_html=True)
st.checkbox("1. Market Analysis (Market Structure + News Squawk) (Trends: CMA, VWAP Suite: VWS, Flow & Volume: RCR, Levels Momentum: LVM, Regime Classifier: ATR) Autocorrelations + Market Regime Classifier)", key="p1")
st.checkbox("2. OHLC Zones Marked (Execute within zone only)", key="p2")
st.checkbox("3. Indicator Stack (Vostok Proto: MTS + MRC)", key="p3")
st.checkbox("4. Risk Telemetry Math", key="p4")
st.checkbox("5. Psychological-Physiological Support Station", key="p5")

# --- SECTION 2: DURING TRADE ---
st.markdown("<h3>🎯 During Trade</h3>", unsafe_allow_html=True)
st.checkbox("1. Candle closed 1:1 ➡️ Break Even Stop", key="d1")
st.checkbox("2. One open position per trade", key="d2")
st.checkbox("3. Cut position if necessary up to discretion", key="d3")

# --- SECTION 3: POST-TRADE ---
st.markdown("<h3>📊 Post-Trade</h3>", unsafe_allow_html=True)
st.checkbox("1. Mandatory Execution Cooldown", key="po1")
st.checkbox("2. Trade Logged in Risk Telemetry after resolved trade", key="po2")
st.checkbox("3. Read Risk Telemetry Decision Science Station", key="po3")

# --- SECTION 4: CONTROL RULES ---
st.markdown("<h3 style='color: #ff0055 !important; text-shadow: 0 0 10px rgba(255,0,85,0.6);'>⚠️ Control Rules</h3>", unsafe_allow_html=True)
st.checkbox("1. All procedural steps considered before execution.", key="c1")
st.checkbox("2. Check all variables with awareness.", key="c2")
st.checkbox("3. Be Ready and informed or SKIP setup.", key="c3")
