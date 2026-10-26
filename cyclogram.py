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
    
    /* Scaled up Neon Blue Title */
    h1 {
        font-family: 'Orbitron', sans-serif !important;
        color: #00f0ff !important;
        text-shadow: 0 0 14px rgba(0, 240, 255, 0.7), 0 0 28px rgba(0, 240, 255, 0.4);
        letter-spacing: 3px;
        font-size: 4.2rem !important;
        margin-bottom: 0.2rem !important;
        margin-top: 0.5rem !important;
    }

    /* Section Headers */
    h3 {
        font-family: 'Orbitron', sans-serif !important;
        color: #00f0ff !important;
        text-shadow: 0 0 10px rgba(0, 240, 255, 0.6), 0 0 20px rgba(0, 240, 255, 0.3);
        letter-spacing: 2px;
        margin-top: 1.8rem !important;
        margin-bottom: 0.6rem !important;
        font-size: 1.4rem !important;
    }
    
    /* Standardized clean unbold text styling across all elements */
    p, span, label {
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 1.15rem !important;
        font-weight: 400 !important;
    }
    
    /* Clean vertical alignment rows replacing HTML bullet containers */
    .hud-row {
        color: #b0e0e6 !important;
        margin-bottom: 8px;
        padding-left: 0px !important;
        margin-left: 0px !important;
    }

    /* Telemetry Status Badge Base Layout */
    .telemetry-badge {
        font-family: 'Orbitron', sans-serif;
        padding: 6px 12px;
        border-radius: 4px;
        font-size: 0.85rem;
        display: inline-block;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    
    /* State: Ready (All 6 items positive) */
    .badge-ready {
        background: rgba(0, 240, 255, 0.1);
        border: 1px solid #00f0ff;
        color: #00f0ff;
        text-shadow: 0 0 5px rgba(0, 240, 255, 0.5);
        box-shadow: 0 0 10px rgba(0, 240, 255, 0.2);
    }

    /* State: Halt (5 or less items positive) */
    .badge-halt {
        background: rgba(255, 68, 68, 0.1);
        border: 1px solid #ff4444;
        color: #ff4444;
        text-shadow: 0 0 5px rgba(255, 68, 68, 0.5);
        box-shadow: 0 0 10px rgba(255, 68, 68, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<h1>CYCLOGRAM</h1>", unsafe_allow_html=True)

# Placeholder container for system gate logic status updates
status_placeholder = st.empty()

st.write("Pre-Market Analysis & Execution Gates protocol configuration.")

# --- SECTION 1: PRE-MARKET ANALYSIS ---
st.markdown("<h3>⚡ Pre-Market Analysis</h3>", unsafe_allow_html=True)

label1 = "1. Lunokhod Sfera: Market Analysis | Market Regime"
label2 = "2. Molniya: Economics News Squawk"
label3 = "3. Buran - MKF-6: OHLC Zones and Levels"
label4 = "4. Vostok: Indicators (MTS, MRC, MRD, MAS, Volume)"
label5 = "5. Telemetry: Risk Math"
label6 = "6. Psychological-Physiological Support Station"

def render_cyber_toggle(label_text, unique_key):
    choice = st.selectbox(
        label_text, 
        options=["[+] POSITIVE", "[-] NEGATIVE"], 
        index=0, 
        key=unique_key,
        label_visibility="collapsed"
    )
    
    if choice == "[+] POSITIVE":
        st.markdown(f"<p style='color: #00f0ff !important; margin-top: -10px; margin-bottom: 15px;'>{label_text} <span style='font-weight: 700 !important; color: #00f0ff;'>[+]</span></p>", unsafe_allow_html=True)
        return True
    else:
        st.markdown(f"<p style='color: #ff4444 !important; margin-top: -10px; margin-bottom: 15px;'>{label_text} <span style='font-weight: 700 !important; color: #ff4444;'>[-]</span></p>", unsafe_allow_html=True)
        return False

s1 = render_cyber_toggle(label1, "s1_key")
s2 = render_cyber_toggle(label2, "s2_key")
s3 = render_cyber_toggle(label3, "s3_key")
s4 = render_cyber_toggle(label4, "s4_key")
s5 = render_cyber_toggle(label5, "s5_key")
s6 = render_cyber_toggle(label5, "s6_key")

# --- EXECUTE GATE STATUS LOGIC COUPLING ---
if s1 and s2 and s3 and s4 and s5 and s6:
    status_placeholder.markdown("<div class='telemetry-badge badge-ready'>SYSTEM STATUS: READY - POSITIVE</div>", unsafe_allow_html=True)
else:
    status_placeholder.markdown("<div class='telemetry-badge badge-halt'>SYSTEM STATUS: HALT - NEGATIVE</div>", unsafe_allow_html=True)

# --- SECTION 2: DURING TRADE ---
st.markdown("<h3>🎯 During Trade</h3>", unsafe_allow_html=True)
st.markdown("""
<p class="hud-row">1. Candle closed 1:1 ➡️ Break Even Stop</p>
<p class="hud-row">2. One open position per trade</p>
<p class="hud-row">3. Cut position if necessary up to discretion</p>
""", unsafe_allow_html=True)

# --- SECTION 3: POST-TRADE ---
st.markdown("<h3>📊 Post-Trade</h3>", unsafe_allow_html=True)
st.markdown("""
<p class="hud-row">1. Mandatory Execution Cooldown</p>
<p class="hud-row">2. Trade Logged in Risk Telemetry after resolved trade</p>
<p class="hud-row">3. Read Risk Telemetry Decision Science Station</p>
""", unsafe_allow_html=True)

# --- SECTION 4: CONTROL RULES ---
st.markdown("<h3>⚠️ Control Rules</h3>", unsafe_allow_html=True)
st.markdown("""
<p class="hud-row">1. All procedural steps considered before execution.</p>
<p class="hud-row">2. Check all variables with awareness.</p>
<p class="hud-row">3. Be Ready and informed or SKIP setup.</p>
""", unsafe_allow_html=True)
