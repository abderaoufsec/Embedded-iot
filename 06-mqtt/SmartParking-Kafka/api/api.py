"""
api.py - Student 3: REST API (Optional)
Smart Parking IoT System

Run with:  uvicorn api.api:app --reload --port 8000
Docs at:   http://localhost:8000/docs
"""

import sys
import os
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
    insert_parking_event,
    insert_alert,
)

# ─────────────────────────────────────────
# App Bootstrap
# ─────────────────────────────────────────
app = FastAPI(
    title="🅿️ Smart Parking API",
    description="REST API for the Smart Parking IoT System (Student 3 module)",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    initialize_database()


# ─────────────────────────────────────────
# Schemas
# ─────────────────────────────────────────
class ParkingEventIn(BaseModel):
    spot_id:   str
    sensor_id: str
    status:    str          # 'occupied' | 'free'
    floor:     int
    zone:      str
    timestamp: Optional[str] = None

class AlertIn(BaseModel):
    alert_type: str
    spot_id:    Optional[str] = None
    zone:       Optional[str] = None
    floor:      Optional[int] = None
    message:    str
    severity:   str = "INFO"
    timestamp:  Optional[str] = None


# ─────────────────────────────────────────
# Routes
# ─────────────────────────────────────────

# ── Health Check ──────────────────────────
@app.get("/", tags=["Health"])
def root():
    return {"status": "ok", "service": "Smart Parking API", "time": datetime.now().isoformat()}

@app.get("/health", tags=["Health"])
def health():
    occ = get_current_occupancy()
    return {"status": "healthy", "db": "sqlite", "occupancy": occ}


# ── Occupancy ──────────────────────────
@app.get("/occupancy", tags=["Occupancy"],
         summary="Overall parking occupancy")
def occupancy():
    """Returns total / occupied / free spot counts."""
    data = get_current_occupancy()
    total = data["total"] or 1   # avoid division by zero
    data["occupancy_pct"] = round(data["occupied"] / total * 100, 1)
    return data

@app.get("/occupancy/zones", tags=["Occupancy"],
         summary="Occupancy broken down by zone")
def occupancy_by_zone():
    return get_occupancy_by_zone()

@app.get("/occupancy/floors", tags=["Occupancy"],
         summary="Occupancy broken down by floor")
def occupancy_by_floor():
    return get_occupancy_by_floor()


# ── Spots ──────────────────────────────
@app.get("/spots", tags=["Spots"],
         summary="List all parking spots and their current status")
def list_spots():
    return get_all_spots()

@app.get("/spots/{spot_id}", tags=["Spots"],
         summary="Get the current status of a specific spot")
def get_spot(spot_id: str):
    spots = get_all_spots()
    match = next((s for s in spots if s["spot_id"] == spot_id), None)
    if not match:
        raise HTTPException(status_code=404, detail=f"Spot '{spot_id}' not found")
    return match


# ── Events ─────────────────────────────
@app.get("/events", tags=["Events"],
         summary="List recent sensor events")
def list_events(limit: int = Query(50, ge=1, le=500)):
    return get_recent_events(limit=limit)

@app.post("/events", tags=["Events"], status_code=201,
          summary="Manually insert a sensor event (testing)")
def create_event(payload: ParkingEventIn):
    if payload.status not in ("occupied", "free"):
        raise HTTPException(status_code=422, detail="status must be 'occupied' or 'free'")
    data = payload.dict()
    data["timestamp"] = data["timestamp"] or datetime.now().isoformat()
    insert_parking_event(data)
    return {"message": "Event saved", "data": data}

@app.get("/events/timeline", tags=["Events"],
         summary="Event counts per minute (for charts)")
def events_timeline(minutes: int = Query(60, ge=5, le=1440)):
    return get_events_over_time(minutes=minutes)


# ── Alerts ─────────────────────────────
@app.get("/alerts", tags=["Alerts"],
         summary="List recent alerts")
def list_alerts(limit: int = Query(20, ge=1, le=500)):
    return get_recent_alerts(limit=limit)

@app.post("/alerts", tags=["Alerts"], status_code=201,
          summary="Manually insert an alert (testing)")
def create_alert(payload: AlertIn):
    data = payload.dict()
    data["timestamp"] = data["timestamp"] or datetime.now().isoformat()
    insert_alert(data)
    return {"message": "Alert saved", "data": data}

@app.get("/alerts/critical", tags=["Alerts"],
         summary="List only CRITICAL alerts")
def list_critical_alerts():
    all_alerts = get_recent_alerts(limit=1000)
    return [a for a in all_alerts if a.get("severity") == "CRITICAL"]


# ─────────────────────────────────────────
# Run directly (dev)
# ─────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
