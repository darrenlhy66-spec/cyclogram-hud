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
    p, span, label, li {
        font-family: 'Rajdhani', sans-serif !important;
        font-size: 1.15rem !important;
        font-weight: 400 !important;
    }
    
    /* Clean custom unbold list item structure */
    ul {
        list-style-type: none;
        padding-left: 0rem;
        margin-top: 0.5rem;
    }
    
    li {
        position: relative;
        padding-left: 1.2rem;
        color: #b0e0e6 !important;
        margin-bottom: 8px;
    }
    
    /* Custom clean list dot */
    li::before {
        content: "•";
        position: absolute;
        left: 0;
        color: #b0e0e6;
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
    
    /* State: Ready (All 5 items positive) */
    .badge-ready {
        background: rgba(0, 240, 255, 0.1);
        border: 1px solid #00f0ff;
        color: #00f0ff;
        text-shadow: 0 0 5px rgba(0, 240, 255, 0.5);
        box-shadow: 0 0 10px rgba(0, 240, 255, 0.2);
    }

    /* State: Halt (4 or less items positive) */
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

# Labels text database mapping
label1 = "1. Market Analysis (Market Structure + News Squawk) (Trends: CMA, VWAP Suite: VWS, Flow & Volume: RCR, Levels Momentum: LVM, Regime Classifier: ATR) Autocorrelations + Market Regime Classifier)"
label2 = "2. OHLC Zones Marked (Execute within zone only)"
label3 = "3. Indicator Stack (Vostok Proto: MTS + MRC)"
label4 = "4. Risk Telemetry Math"
label5 = "5. Psychological-Physiological Support Station"

# Helper generator handling inline evaluation styles mapping cleanly
def render_cyber_toggle(label_text, unique_key):
    # Selectbox dropdown targeting active states
    choice = st.selectbox(
        label_text, 
        options=["[-] NEGATIVE", "[+] POSITIVE"], 
        index=0, 
        key=unique_key,
        label_visibility="collapsed"
    )
    
    # Check conditional colors styling rules
    if choice == "[+] POSITIVE":
        st.markdown(f"<p style='color: #00f0ff !important; margin-top: -10px; margin-bottom: 15px;'>{label_text} <span style='font-weight: 700 !important;'>[+]</span></p>", unsafe_allow_html=True)
        return True
    else:
        st.markdown(f"<p style='color: #ff4444 !important; margin-top: -10px; margin-bottom: 15px;'>{label_text} <span style='font-weight: 700 !important;'>[-]</span></p>", unsafe_allow_html=True)
        return False

# Execute custom toggles components processing sequence
s1 = render_cyber_toggle(label1, "s1_key")
s2 = render_cyber_toggle(label2, "s2_key")
s3 = render_cyber_toggle(label3, "s3_key")
s4 = render_cyber_toggle(label4, "s4_key")
s5 = render_cyber_toggle(label5, "s5_key")

# --- EXECUTE GATE STATUS LOGIC COUPLING ---
if s1 and s2 and s3 and s4 and s5:
    status_placeholder.markdown("<div class='telemetry-badge badge-ready'>SYSTEM STATUS: READY - POSITIVE</div>", unsafe_allow_html=True)
else:
    status_placeholder.markdown("<div class='telemetry-badge badge-halt'>SYSTEM STATUS: HALT - NEGATIVE</div>", unsafe_allow_html=True)

# --- SECTION 2: DURING TRADE ---
st.markdown("<h3>🎯 During Trade</h3>", unsafe_allow_html=True)
st.markdown("""
<ul>
    <li>1. Candle closed 1:1 ➡️ Break Even Stop</li>
    <li>2. One open position per trade</li>
    <li>3. Cut position if necessary up to discretion</li>
</ul>
""", unsafe_allow_html=True)

# --- SECTION 3: POST-TRADE ---
st.markdown("<h3>📊 Post-Trade</h3>", unsafe_allow_html=True)
st.markdown("""
<ul>
    <li>1. Mandatory Execution Cooldown</li>
    <li>2. Trade Logged in Risk Telemetry after resolved trade</li>
    <li>3. Read Risk Telemetry Decision Science Station</li>
</ul>
""", unsafe_allow_html=True)

# --- SECTION 4: CONTROL RULES ---
st.markdown("<h3>⚠️ Control Rules</h3>", unsafe_allow_html=True)
st.markdown("""
<ul>
    <li>1. All procedural steps considered before execution.</li>
    <li>2. Check all variables with awareness.</li>
    <li>3. Be Ready and informed or SKIP setup.</li>
</ul>
""", unsafe_allow_html=True)
