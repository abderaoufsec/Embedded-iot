"""
database.py - Student 3: Database Management
Smart Parking IoT System
Handles SQLite database creation and operations.
"""

import sqlite3
import os
import logging
from datetime import datetime

# ─────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────
DB_PATH = os.path.join(os.path.dirname(__file__), "parking.db")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [DATABASE] %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# ─────────────────────────────────────────
# Database Initialization
# ─────────────────────────────────────────
def get_connection():
    """Return a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # allows dict-like access
    return conn


def initialize_database():
    """
    Create all tables if they don't exist yet.
    Tables:
        - parking_events  : raw sensor readings
        - alerts          : generated alerts
        - parking_spots   : current status of each spot
    """
    conn = get_connection()
    cursor = conn.cursor()

    # --- parking_events table ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parking_events (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            spot_id     TEXT    NOT NULL,
            sensor_id   TEXT    NOT NULL,
            status      TEXT    NOT NULL,       -- 'occupied' | 'free'
            floor       INTEGER NOT NULL,
            zone        TEXT    NOT NULL,
            timestamp   TEXT    NOT NULL,
            created_at  TEXT    DEFAULT (datetime('now'))
        )
    """)

    # --- alerts table ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            alert_type   TEXT NOT NULL,          -- 'FULL_ZONE' | 'SPOT_TAKEN' | ...
            spot_id      TEXT,
            zone         TEXT,
            floor        INTEGER,
            message      TEXT NOT NULL,
            severity     TEXT DEFAULT 'INFO',    -- 'INFO' | 'WARNING' | 'CRITICAL'
            timestamp    TEXT NOT NULL,
            created_at   TEXT DEFAULT (datetime('now'))
        )
    """)

    # --- parking_spots table (current state) ---
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS parking_spots (
            spot_id      TEXT PRIMARY KEY,
            sensor_id    TEXT NOT NULL,
            status       TEXT NOT NULL DEFAULT 'free',
            floor        INTEGER NOT NULL,
            zone         TEXT NOT NULL,
            last_updated TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    logger.info("✅ Database initialized at: %s", DB_PATH)


# ─────────────────────────────────────────
# Write Operations
# ─────────────────────────────────────────
def insert_parking_event(data: dict):
    """
    Insert a raw parking sensor event.
    Expected keys: spot_id, sensor_id, status, floor, zone, timestamp
    """
    conn = get_connection()
    try:
        conn.execute("""
            INSERT INTO parking_events (spot_id, sensor_id, status, floor, zone, timestamp)
            VALUES (:spot_id, :sensor_id, :status, :floor, :zone, :timestamp)
        """, data)

        # Also update current spot state
        conn.execute("""
            INSERT INTO parking_spots (spot_id, sensor_id, status, floor, zone, last_updated)
            VALUES (:spot_id, :sensor_id, :status, :floor, :zone, :timestamp)
            ON CONFLICT(spot_id) DO UPDATE SET
                status       = excluded.status,
                last_updated = excluded.last_updated
        """, data)

        conn.commit()
        logger.debug("📥 Event saved → spot %s | status: %s", data.get("spot_id"), data.get("status"))

    except Exception as e:
        logger.error("❌ Failed to insert event: %s", e)
    finally:
        conn.close()


def insert_alert(data: dict):
    """
    Insert an alert record.
    Expected keys: alert_type, spot_id, zone, floor, message, severity, timestamp
    """
    conn = get_connection()
    try:
        conn.execute("""
            INSERT INTO alerts (alert_type, spot_id, zone, floor, message, severity, timestamp)
            VALUES (:alert_type, :spot_id, :zone, :floor, :message, :severity, :timestamp)
        """, data)
        conn.commit()
        logger.info("🚨 Alert saved → [%s] %s", data.get("severity"), data.get("message"))

    except Exception as e:
        logger.error("❌ Failed to insert alert: %s", e)
    finally:
        conn.close()


# ─────────────────────────────────────────
# Read Operations
# ─────────────────────────────────────────
def get_current_occupancy():
    """
    Returns a summary dict with total, occupied, and free spots.
    """
    conn = get_connection()
    try:
        row = conn.execute("""
            SELECT
                COUNT(*)                                    AS total,
                SUM(CASE WHEN status='occupied' THEN 1 ELSE 0 END) AS occupied,
                SUM(CASE WHEN status='free'     THEN 1 ELSE 0 END) AS free
            FROM parking_spots
        """).fetchone()
        return dict(row) if row else {"total": 0, "occupied": 0, "free": 0}
    finally:
        conn.close()


def get_occupancy_by_zone():
    """
    Returns occupancy grouped by zone.
    """
    conn = get_connection()
    try:
        rows = conn.execute("""
            SELECT
                zone,
                COUNT(*)                                         AS total,
                SUM(CASE WHEN status='occupied' THEN 1 ELSE 0 END) AS occupied,
                SUM(CASE WHEN status='free'     THEN 1 ELSE 0 END) AS free
            FROM parking_spots
            GROUP BY zone
            ORDER BY zone
        """).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def get_occupancy_by_floor():
    """
    Returns occupancy grouped by floor.
    """
    conn = get_connection()
    try:
        rows = conn.execute("""
            SELECT
                floor,
                COUNT(*)                                         AS total,
                SUM(CASE WHEN status='occupied' THEN 1 ELSE 0 END) AS occupied,
                SUM(CASE WHEN status='free'     THEN 1 ELSE 0 END) AS free
            FROM parking_spots
            GROUP BY floor
            ORDER BY floor
        """).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def get_recent_events(limit: int = 50):
    """
    Returns the most recent parking events.
    """
    conn = get_connection()
    try:
        rows = conn.execute("""
            SELECT * FROM parking_events
            ORDER BY id DESC
            LIMIT ?
        """, (limit,)).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def get_recent_alerts(limit: int = 20):
    """
    Returns the most recent alerts.
    """
    conn = get_connection()
    try:
        rows = conn.execute("""
            SELECT * FROM alerts
            ORDER BY id DESC
            LIMIT ?
        """, (limit,)).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def get_all_spots():
    """
    Returns all current parking spot states.
    """
    conn = get_connection()
    try:
        rows = conn.execute("""
            SELECT * FROM parking_spots ORDER BY floor, zone, spot_id
        """).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def get_events_over_time(minutes: int = 60):
    """
    Returns event counts per minute for the last N minutes (for charts).
    """
    conn = get_connection()
    try:
        rows = conn.execute("""
            SELECT
                strftime('%Y-%m-%d %H:%M', timestamp) AS minute,
                SUM(CASE WHEN status='occupied' THEN 1 ELSE 0 END) AS occupied,
                SUM(CASE WHEN status='free'     THEN 1 ELSE 0 END) AS free,
                COUNT(*) AS total
            FROM parking_events
            WHERE timestamp >= datetime('now', ? || ' minutes')
            GROUP BY minute
            ORDER BY minute
        """, (f"-{minutes}",)).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


# ─────────────────────────────────────────
# Utility
# ─────────────────────────────────────────
def clear_all_data():
    """
    Wipe all data (useful for demos / resets).
    """
    conn = get_connection()
    conn.execute("DELETE FROM parking_events")
    conn.execute("DELETE FROM alerts")
    conn.execute("DELETE FROM parking_spots")
    conn.commit()
    conn.close()
    logger.warning("⚠️  All data cleared from database.")


# ─────────────────────────────────────────
# Entry point – run directly to test
# ─────────────────────────────────────────
if __name__ == "__main__":
    initialize_database()
    print("Database ready at:", DB_PATH)

    # Quick smoke test
    sample_event = {
        "spot_id":   "A-001",
        "sensor_id": "SEN-001",
        "status":    "occupied",
        "floor":     1,
        "zone":      "A",
        "timestamp": datetime.now().isoformat()
    }
    insert_parking_event(sample_event)

    sample_alert = {
        "alert_type": "SPOT_TAKEN",
        "spot_id":    "A-001",
        "zone":       "A",
        "floor":      1,
        "message":    "Spot A-001 is now occupied",
        "severity":   "INFO",
        "timestamp":  datetime.now().isoformat()
    }
    insert_alert(sample_alert)

    print("Occupancy:", get_current_occupancy())
    print("By zone:",   get_occupancy_by_zone())
    print("Test passed ✅")
