"""
app.py - Student 3: Live Dashboard
Smart Parking IoT System

Run with:  streamlit run dashboard/app.py
"""

import sys
import os
import time
import pandas as pd
import streamlit as st

# Allow importing from the storage folder
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "storage"))

from database import (
    initialize_database,
    get_current_occupancy,
    get_occupancy_by_zone,
    get_occupancy_by_floor,
    get_recent_events,
    get_recent_alerts,
    get_all_spots,
    get_events_over_time,
    clear_all_data,
)

# ─────────────────────────────────────────
# Page Config
# ─────────────────────────────────────────
st.set_page_config(
    page_title="🅿️ Smart Parking Dashboard",
    page_icon="🅿️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────
# Custom CSS
# ─────────────────────────────────────────
st.markdown("""
<style>
    /* ── Global ── */
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    /* ── Header ── */
    .dash-header {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        border-radius: 16px;
        padding: 28px 36px;
        margin-bottom: 24px;
        color: white;
    }
    .dash-header h1 { font-family: 'Space Mono', monospace; font-size: 2rem; margin: 0; }
    .dash-header p  { opacity: 0.7; margin: 6px 0 0; font-size: 0.9rem; }

    /* ── KPI Cards ── */
    .kpi-card {
        background: #1a1a2e;
        border: 1px solid #16213e;
        border-radius: 14px;
        padding: 22px 20px;
        text-align: center;
        color: white;
        transition: transform .2s;
    }
    .kpi-card:hover { transform: translateY(-3px); }
    .kpi-value  { font-size: 2.8rem; font-weight: 700; font-family: 'Space Mono', monospace; }
    .kpi-label  { font-size: 0.85rem; opacity: 0.65; text-transform: uppercase; letter-spacing: 1px; margin-top: 4px; }
    .kpi-pct    { font-size: 1.1rem; font-weight: 600; margin-top: 6px; }

    /* Colors per KPI */
    .kpi-blue   { border-top: 4px solid #4fc3f7; }
    .kpi-orange { border-top: 4px solid #ff9800; }
    .kpi-green  { border-top: 4px solid #66bb6a; }
    .kpi-red    { border-top: 4px solid #ef5350; }

    /* ── Alert Badges ── */
    .alert-info     { background:#1565c0; }
    .alert-warning  { background:#e65100; }
    .alert-critical { background:#b71c1c; }

    .alert-badge {
        display:inline-block;
        padding:2px 10px;
        border-radius:30px;
        font-size:0.75rem;
        font-weight:700;
        color:white;
        text-transform:uppercase;
    }

    /* ── Section titles ── */
    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #4fc3f7;
        letter-spacing: .5px;
        margin: 20px 0 10px;
        border-left: 4px solid #4fc3f7;
        padding-left: 10px;
    }

    /* ── Spot grid ── */
    .spot-grid { display: flex; flex-wrap: wrap; gap: 8px; }
    .spot {
        width: 56px; height: 44px;
        border-radius: 8px;
        display: flex; align-items: center; justify-content: center;
        font-size: 0.65rem; font-weight: 700;
        font-family: 'Space Mono', monospace;
        color: white;
    }
    .spot-free     { background: #2e7d32; border: 2px solid #43a047; }
    .spot-occupied { background: #c62828; border: 2px solid #ef5350; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# Ensure DB exists
# ─────────────────────────────────────────
initialize_database()

# ─────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    refresh_rate = st.slider("Auto-refresh (sec)", 2, 30, 5)
    events_limit = st.slider("Events to display",  10, 200, 50)
    alerts_limit = st.slider("Alerts to display",  5,  100, 20)

    st.markdown("---")
    st.markdown("### 🕹️ Controls")
    if st.button("🔄 Refresh Now"):
        st.rerun()

    with st.expander("⚠️ Danger Zone"):
        if st.button("🗑️ Clear All Data", type="primary"):
            clear_all_data()
            st.success("Data cleared!")
            time.sleep(1)
            st.rerun()

    st.markdown("---")
    st.caption("Smart Parking IoT System\nStudent 3 — Dashboard")

# ─────────────────────────────────────────
# Header
# ─────────────────────────────────────────
st.markdown("""
<div class="dash-header">
    <h1>🅿️ Smart Parking — Live Dashboard</h1>
    <p>Real-time monitoring powered by Apache Kafka + SQLite</p>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────
# KPI Row
# ─────────────────────────────────────────
occupancy = get_current_occupancy()
total    = occupancy["total"]    or 0
occupied = occupancy["occupied"] or 0
free     = occupancy["free"]     or 0
pct_occ  = round(occupied / total * 100, 1) if total else 0
pct_free = round(free     / total * 100, 1) if total else 0

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card kpi-blue">
        <div class="kpi-value">{total}</div>
        <div class="kpi-label">Total Spots</div>
        <div class="kpi-pct">100 %</div>
    </div>""", unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card kpi-orange">
        <div class="kpi-value">{occupied}</div>
        <div class="kpi-label">Occupied</div>
        <div class="kpi-pct">{pct_occ} %</div>
    </div>""", unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card kpi-green">
        <div class="kpi-value">{free}</div>
        <div class="kpi-label">Available</div>
        <div class="kpi-pct">{pct_free} %</div>
    </div>""", unsafe_allow_html=True)

with col4:
    alert_data = get_recent_alerts(limit=1000)
    critical_count = sum(1 for a in alert_data if a.get("severity") == "CRITICAL")
    st.markdown(f"""
    <div class="kpi-card kpi-red">
        <div class="kpi-value">{critical_count}</div>
        <div class="kpi-label">Critical Alerts</div>
        <div class="kpi-pct">⚠️ Active</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ─────────────────────────────────────────
# Occupancy Bar
# ─────────────────────────────────────────
st.markdown('<div class="section-title">📊 Overall Occupancy</div>', unsafe_allow_html=True)
st.progress(pct_occ / 100 if total else 0)
st.caption(f"{pct_occ}% occupied — {free} spots available out of {total}")

# ─────────────────────────────────────────
# Zone + Floor Charts
# ─────────────────────────────────────────
col_left, col_right = st.columns(2)

with col_left:
    st.markdown('<div class="section-title">🏢 Occupancy by Zone</div>', unsafe_allow_html=True)
    zone_data = get_occupancy_by_zone()
    if zone_data:
        df_zone = pd.DataFrame(zone_data)
        df_zone["occupancy_%"] = (df_zone["occupied"] / df_zone["total"] * 100).round(1)
        st.bar_chart(df_zone.set_index("zone")[["occupied", "free"]])
    else:
        st.info("No data yet — waiting for sensor messages.")

with col_right:
    st.markdown('<div class="section-title">🏗️ Occupancy by Floor</div>', unsafe_allow_html=True)
    floor_data = get_occupancy_by_floor()
    if floor_data:
        df_floor = pd.DataFrame(floor_data)
        df_floor["floor"] = df_floor["floor"].astype(str)
        st.bar_chart(df_floor.set_index("floor")[["occupied", "free"]])
    else:
        st.info("No data yet — waiting for sensor messages.")

# ─────────────────────────────────────────
# Activity Over Time
# ─────────────────────────────────────────
st.markdown('<div class="section-title">📈 Activity (last 60 min)</div>', unsafe_allow_html=True)
time_data = get_events_over_time(minutes=60)
if time_data:
    df_time = pd.DataFrame(time_data).set_index("minute")
    st.line_chart(df_time[["occupied", "free"]])
else:
    st.info("Not enough time-series data yet.")

# ─────────────────────────────────────────
# Spot Grid (visual map)
# ─────────────────────────────────────────
st.markdown('<div class="section-title">🗺️ Parking Map (Current State)</div>', unsafe_allow_html=True)
spots = get_all_spots()
if spots:
    df_spots = pd.DataFrame(spots)

    # Legend
    st.markdown("""
    <span style='background:#2e7d32;padding:3px 10px;border-radius:6px;color:white;font-size:.8rem;'>🟢 Free</span>&nbsp;
    <span style='background:#c62828;padding:3px 10px;border-radius:6px;color:white;font-size:.8rem;'>🔴 Occupied</span>
    """, unsafe_allow_html=True)

    for floor_num in sorted(df_spots["floor"].unique()):
        floor_spots = df_spots[df_spots["floor"] == floor_num]
        st.markdown(f"**Floor {floor_num}**")
        html_spots = '<div class="spot-grid">'
        for _, s in floor_spots.iterrows():
            css = "spot-occupied" if s["status"] == "occupied" else "spot-free"
            html_spots += f'<div class="spot {css}">{s["spot_id"]}</div>'
        html_spots += "</div><br>"
        st.markdown(html_spots, unsafe_allow_html=True)
else:
    st.info("No spots registered yet.")

# ─────────────────────────────────────────
# Recent Alerts
# ─────────────────────────────────────────
st.markdown('<div class="section-title">🚨 Recent Alerts</div>', unsafe_allow_html=True)
alerts = get_recent_alerts(limit=alerts_limit)
if alerts:
    for a in alerts:
        sev = a.get("severity", "INFO").upper()
        color_map = {"INFO": "🔵", "WARNING": "🟠", "CRITICAL": "🔴"}
        icon = color_map.get(sev, "⚪")
        with st.expander(f"{icon} [{sev}] {a.get('message', '')} — {a.get('timestamp', '')[:16]}"):
            st.json({k: v for k, v in a.items() if k not in ("id", "created_at")})
else:
    st.success("✅ No alerts — all systems normal.")

# ─────────────────────────────────────────
# Recent Events Table
# ─────────────────────────────────────────
st.markdown('<div class="section-title">📋 Recent Sensor Events</div>', unsafe_allow_html=True)
events = get_recent_events(limit=events_limit)
if events:
    df_events = pd.DataFrame(events)[["spot_id", "zone", "floor", "status", "sensor_id", "timestamp"]]
    df_events["status"] = df_events["status"].apply(
        lambda s: "🔴 Occupied" if s == "occupied" else "🟢 Free"
    )
    st.dataframe(df_events, use_container_width=True, hide_index=True)
else:
    st.info("No events recorded yet.")

# ─────────────────────────────────────────
# Zone Summary Table
# ─────────────────────────────────────────
if zone_data:
    st.markdown('<div class="section-title">📊 Zone Summary Table</div>', unsafe_allow_html=True)
    df_zone_table = pd.DataFrame(zone_data)
    df_zone_table["Occupancy %"] = (
        df_zone_table["occupied"] / df_zone_table["total"] * 100
    ).round(1).astype(str) + " %"
    df_zone_table.columns = ["Zone", "Total", "Occupied", "Free", "Occupancy %"]
    st.dataframe(df_zone_table, use_container_width=True, hide_index=True)

# ─────────────────────────────────────────
# Auto-refresh
# ─────────────────────────────────────────
st.markdown("---")
st.caption(f"⏱️ Auto-refreshing every {refresh_rate}s | Last update: {pd.Timestamp.now().strftime('%H:%M:%S')}")
time.sleep(refresh_rate)
st.rerun()
