import streamlit as st

# --- STREAMLIT PAGE CONFIG ---
st.set_page_config(
    page_title="Cyclogram HUD",
    page_icon="🌌",
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# --- CYBERPUNK CUSTOM CSS ---
st.markdown("""
<style>
    @import url('https://googleapis.com');
    
    .stApp {
        background-color: #03080a;
        color: #e0f7fa;
        font-family: 'Rajdhani', sans-serif;
    }
    
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
        color: #00f0ff !important;
        text-shadow: 0 0 10px rgba(0, 240, 255, 0.6), 0 0 20px rgba(0, 240, 255, 0.3);
        letter-spacing: 2px;
    }
    
    .hud-card {
        background: rgba(5, 20, 26, 0.85);
        border-left: 4px solid #00f0ff;
        border-top: 1px solid rgba(0, 240, 255, 0.2);
        border-right: 1px solid rgba(0, 240, 255, 0.1);
        border-bottom: 1px solid rgba(0, 240, 255, 0.1);
        padding: 20px;
        border-radius: 0 12px 12px 0;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    }
    
    .control-card {
        background: rgba(26, 5, 5, 0.5);
        border-left: 4px solid #ff0055;
        border-top: 1px solid rgba(255, 0, 85, 0.2);
        padding: 20px;
        border-radius: 0 12px 12px 0;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(255, 0, 85, 0.1);
    }
    
    .stCheckbox label {
        font-size: 1.15rem !important;
        font-weight: 500 !important;
        color: #b0e0e6 !important;
    }
    
    .telemetry-badge {
        font-family: 'Orbitron', sans-serif;
        background: rgba(0, 240, 255, 0.1);
        border: 1px solid #00f0ff;
        color: #00f0ff;
        padding: 4px 10px;
        border-radius: 4px;
        font-size: 0.8rem;
        display: inline-block;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<h1>CYCLOGRAM</h1>", unsafe_allow_html=True)
st.write("Pre-Market Analysis & Execution Gates protocol configuration.")

# --- SECTION 1: PRE-MARKET ---
st.markdown("<h3>⚡ Pre-Market Analysis</h3>", unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="hud-card">', unsafe_allow_html=True)
    st.checkbox("1. Market Analysis (Market Structure + News Squawk) (Trends: CMA, VWAP Suite: VWS, Flow & Volume: RCR, Levels Momentum: LVM, Regime Classifier: ATR) Autocorrelations + Market Regime Classifier)", key="p1")
    st.checkbox("2. OHLC Zones Marked (Execute within zone only)", key="p2")
    st.checkbox("3. Indicator Stack (Vostok Proto: MTS + MRC)", key="p3")
    st.checkbox("4. Risk Telemetry Math", key="p4")
    st.checkbox("5. Psychological-Physiological Support Station", key="p5")
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 2: DURING TRADE ---
st.markdown("<h3>🎯 During Trade</h3>", unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="hud-card">', unsafe_allow_html=True)
    st.checkbox("1. Candle closed 1:1 ➡️ Break Even Stop", key="d1")
    st.checkbox("2. One open position per trade", key="d2")
    st.checkbox("3. Cut position if necessary up to discretion", key="d3")
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 3: POST-TRADE ---
st.markdown("<h3>📊 Post-Trade</h3>", unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="hud-card">', unsafe_allow_html=True)
    st.checkbox("1. Mandatory Execution Cooldown", key="po1")
    st.checkbox("2. Trade Logged in Risk Telemetry after resolved trade", key="po2")
    st.checkbox("3. Read Risk Telemetry Decision Science Station", key="po3")
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 4: CONTROL RULES ---
st.markdown("<h3 style='color: #ff0055 !important; text-shadow: 0 0 10px rgba(255,0,85,0.6);'>⚠️ Control Rules</h3>", unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="control-card">', unsafe_allow_html=True)
    st.checkbox("1. All procedural steps considered before execution.", key="c1")
    st.checkbox("2. Check all variables with awareness.", key="c2")
    st.checkbox("3. Be Ready and informed or SKIP setup.", key="c3")
    st.markdown('</div>', unsafe_allow_html=True)
