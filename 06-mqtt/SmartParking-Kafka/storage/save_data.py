"""
save_data.py - Student 3: Kafka → Database Bridge
Smart Parking IoT System

This module listens to Kafka topics and saves all messages
to the SQLite database. Run this alongside the main consumer.

Topics consumed:
    - parking-data   → saved as parking events
    - parking-alerts → saved as alerts
"""

import json
import logging
import signal
import sys
from datetime import datetime
from kafka import KafkaConsumer
from storage.database import (
    initialize_database,
    insert_parking_event,
    insert_alert
)

# ─────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────
KAFKA_BOOTSTRAP = "localhost:9092"
TOPICS          = ["parking-data", "parking-alerts"]
GROUP_ID        = "storage-group"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [SAVE_DATA] %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

running = True   # graceful shutdown flag


# ─────────────────────────────────────────
# Graceful Shutdown Handler
# ─────────────────────────────────────────
def handle_shutdown(signum, frame):
    global running
    logger.info("🛑 Shutdown signal received. Closing consumer...")
    running = False


signal.signal(signal.SIGINT,  handle_shutdown)
signal.signal(signal.SIGTERM, handle_shutdown)


# ─────────────────────────────────────────
# Message Handlers
# ─────────────────────────────────────────
def handle_parking_data(message: dict):
    """
    Validate and store a parking sensor reading.
    """
    required = {"spot_id", "sensor_id", "status", "floor", "zone", "timestamp"}
    if not required.issubset(message.keys()):
        logger.warning("⚠️  Incomplete parking-data message: %s", message)
        return

    if message["status"] not in ("occupied", "free"):
        logger.warning("⚠️  Unknown status '%s' for spot %s", message["status"], message["spot_id"])
        return

    insert_parking_event(message)


def handle_parking_alert(message: dict):
    """
    Validate and store a parking alert.
    """
    # Provide defaults so storage never fails on optional fields
    alert = {
        "alert_type": message.get("alert_type", "UNKNOWN"),
        "spot_id":    message.get("spot_id"),
        "zone":       message.get("zone"),
        "floor":      message.get("floor"),
        "message":    message.get("message", str(message)),
        "severity":   message.get("severity", "INFO"),
        "timestamp":  message.get("timestamp", datetime.now().isoformat()),
    }
    insert_alert(alert)


# ─────────────────────────────────────────
# Main Consumer Loop
# ─────────────────────────────────────────
def start_storage_consumer():
    logger.info("🚀 Starting storage consumer...")
    logger.info("   Topics : %s", TOPICS)
    logger.info("   Group  : %s", GROUP_ID)
    logger.info("   Broker : %s", KAFKA_BOOTSTRAP)

    # Ensure DB schema exists
    initialize_database()

    try:
        consumer = KafkaConsumer(
            *TOPICS,
            bootstrap_servers=KAFKA_BOOTSTRAP,
            group_id=GROUP_ID,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        )
        logger.info("✅ Connected to Kafka. Waiting for messages...\n")

    except Exception as e:
        logger.error("❌ Could not connect to Kafka: %s", e)
        sys.exit(1)

    # ── Main loop ─────────────────────────
    saved_count = 0
    while running:
        records = consumer.poll(timeout_ms=1000)   # non-blocking poll

        for tp, messages in records.items():
            for msg in messages:
                topic   = msg.topic
                payload = msg.value

                try:
                    if topic == "parking-data":
                        handle_parking_data(payload)
                    elif topic == "parking-alerts":
                        handle_parking_alert(payload)
                    else:
                        logger.debug("Unknown topic: %s", topic)

                    saved_count += 1
                    if saved_count % 100 == 0:
                        logger.info("📊 %d messages saved to database so far.", saved_count)

                except Exception as e:
                    logger.error("❌ Error processing message from %s: %s | msg: %s",
                                 topic, e, payload)

    # ── Cleanup ───────────────────────────
    consumer.close()
    logger.info("💾 Storage consumer stopped. Total saved: %d", saved_count)


# ─────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────
if __name__ == "__main__":
    start_storage_consumer()
