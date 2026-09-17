# consumer/processor.py
import json

def process_parking_message(raw_message):
    """
    Parses and validates incoming parking sensor data.
    Returns (processed_data, alert_needed, alert_reason)
    """
    # Deserialize JSON string
    data = json.loads(raw_message)
    
    # Basic Validation
    required_fields = ['spot_id', 'status', 'duration_minutes', 'timestamp']
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
            
    spot_id = data['spot_id']
    status = data['status']
    duration = data['duration_minutes']
    
    alert_needed = False
    alert_reason = None
    
    # Example Real-Time Processing Rule: Overtime Parking Alert
    if status == 'occupied' and duration > 180:
        alert_needed = True
        alert_reason = f"Spot {spot_id} has been occupied for an excessive duration ({duration} mins)."
        
    # Example Rule: Critical Anomaly (e.g., negative duration values)
    elif duration < 0:
        alert_needed = True
        alert_reason = f"Sensor anomaly detected at Spot {spot_id}: Negative duration recorded."

    return data, alert_needed, alert_reason