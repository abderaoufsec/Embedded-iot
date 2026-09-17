import json
import random
import time
from datetime import datetime

import yaml
from kafka import KafkaProducer


# ==========================================
# LOAD CONFIG
# ==========================================

with open("producer/config.yaml", "r") as file:
    config = yaml.safe_load(file)

BOOTSTRAP_SERVERS = config["kafka"]["bootstrap_servers"]
TOPIC_NAME = config["topics"]["sensor_data"]

TOTAL_SPOTS = config["parking"]["total_spots"]
INTERVAL = config["parking"]["sensor_interval_seconds"]


# ==========================================
# CREATE PRODUCER
# ==========================================

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,

    value_serializer=lambda v: json.dumps(v).encode("utf-8"),

    retries=5,
    acks='all'
)


# ==========================================
# GENERATE SMART PARKING DATA
# ==========================================

def generate_parking_data():

    spot_number = random.randint(1, TOTAL_SPOTS)

    occupied = random.choice([True, False])

    data = {

        # Student 2 + 3 compatible fields
        "spot_id": f"A-{spot_number:03}",

        "sensor_id": f"SEN-{spot_number:03}",

        "status": "occupied" if occupied else "free",

        "floor": random.randint(1, 3),

        "zone": random.choice(["A", "B", "C"]),

        "duration_minutes": random.randint(0, 300),

        "temperature": random.randint(20, 60),

        "timestamp": datetime.now().isoformat()
    }

    return data


# ==========================================
# MAIN LOOP
# ==========================================

print("\n🚗 Smart Parking Producer Started...\n")

try:

    while True:

        parking_data = generate_parking_data()

        producer.send(TOPIC_NAME, value=parking_data)

        producer.flush()

        print("✅ Sent:")
        print(json.dumps(parking_data, indent=4))

        print("-" * 50)

        time.sleep(INTERVAL)

except KeyboardInterrupt:

    print("\n🛑 Producer stopped.")

finally:

    producer.close()