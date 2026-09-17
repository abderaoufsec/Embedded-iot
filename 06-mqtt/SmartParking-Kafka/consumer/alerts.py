# consumer/alerts.py
import json
from kafka import KafkaProducer

class AlertSystem:
    def __init__(self, bootstrap_servers=['localhost:9092'], topic='parking-alerts'):
        self.topic = topic
        # Initialize producer specifically for routing alerts
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )

    def send_alert(self, spot_id, reason, original_data):
        """
        Publishes an alert payload to the parking-alerts topic.
        """
        alert_payload = {
            "event": "PARKING_ALERT",
            "spot_id": spot_id,
            "reason": reason,
            "timestamp": original_data.get("timestamp"),
            "severity": "HIGH"
        }
        
        try:
            self.producer.send(self.topic, value=alert_payload)
            self.producer.flush()
            print(f"⚠️  [ALERT SENT] Spot {spot_id}: {reason}")
        except Exception as e:
            print(f"❌ Failed to publish alert to Kafka: {e}")