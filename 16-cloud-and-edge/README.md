# Phase 16 — Cloud and Edge

> **Goal:** Understand cloud and edge computing architectures for IoT systems and implement end-to-end IoT data pipelines.
>
> **Prerequisite:** Phase 15 — Embedded Security
>
> **Outcome:** You can design and implement cloud and edge architectures for IoT systems with proper data flow, reliability, and security.

---

## What You Will Learn

By completing this phase, you will understand:

- **Cloud Computing:** Cloud services, models, and providers
- **Edge Computing:** Edge processing, local intelligence, decision making
- **Architecture:** Device → Edge → Gateway → Cloud → Application
- **Data Ingestion:** MQTT, HTTP APIs, CoAP, data formats
- **Data Processing:** Time-series data, analytics, aggregation
- **Storage:** Databases, time-series databases, object storage
- **APIs:** REST, GraphQL, API design, authentication
- **Reliability:** Buffering, retry strategies, offline operation
- **Scalability:** Load balancing, auto-scaling, performance
- **Cost:** Cloud cost management, optimization
- **Docker:** Containerization concepts
- **Observability:** Monitoring, logging, metrics

---

## Prerequisites

**Before starting this phase, you should have:**

- ✅ Completed Phases 0-15
- ✅ Understanding of networking (Phase 9)
- ✅ Understanding of MQTT (Phase 10)
- ✅ Understanding of Linux (Phase 11)
- ✅ Understanding of Raspberry Pi (Phase 12)
- ✅ Understanding of security (Phase 15)

**Required Hardware:**
- Raspberry Pi (as edge/gateway)
- ESP32 (as device)
- Network connection

**Required Software:**
- Docker (optional)
- Cloud platform account (optional)
- MQTT broker (local or cloud)

---

## Learning Outcomes

After completing this phase, you will be able to:

- Explain cloud vs edge computing
- Design IoT system architecture
- Implement data ingestion (MQTT, HTTP)
- Design and use REST APIs
- Store and query time-series data
- Implement buffering and retry strategies
- Design for offline operation
- Understand scalability concepts
- Estimate cloud costs
- Implement monitoring and logging
- Use Docker for containerization

---

## Why This Matters

**Cloud vs Edge:**
- **Cloud:** Centralized processing, unlimited resources, higher latency
- **Edge:** Distributed processing, limited resources, lower latency
- **Hybrid:** Best of both worlds

**Architecture Matters:**
- Poor architecture leads to unreliability
- Poor performance
- High costs
- Security issues

**Data Flow:**
```
Device → Edge → Gateway → Cloud → Application
```

**Key Challenges:**
- Network reliability
- Data volume
- Latency requirements
- Security
- Cost management

---

## Core Concepts

### Cloud Computing

**Cloud Service Models:**
- **IaaS:** Infrastructure as a Service (AWS EC2, Azure VM)
- **PaaS:** Platform as a Service (AWS Lambda, Azure Functions)
- **SaaS:** Software as a Service (AWS IoT Core, Azure IoT Hub)

**Cloud Deployment Models:**
- **Public:** Shared infrastructure (AWS, Azure, GCP)
- **Private:** Dedicated infrastructure
- **Hybrid:** Combination of public and private

**Cloud Providers:**
- AWS (Amazon Web Services)
- Azure (Microsoft)
- GCP (Google Cloud Platform)
- Provider-agnostic design preferred

**Cloud Services for IoT:**
- IoT platforms (AWS IoT Core, Azure IoT Hub)
- Message brokers (AWS IoT Core, Azure Event Hubs)
- Databases (DynamoDB, Cosmos DB)
- Storage (S3, Blob Storage)
- Compute (EC2, Functions)

---

### Edge Computing

**Edge Computing:**
- Processing closer to data source
- Reduced latency
- Reduced bandwidth
- Offline capability
- Local decision making

**Edge vs Cloud:**
- **Edge:** Low latency, local processing, limited resources
- **Cloud:** High latency, centralized processing, unlimited resources

**Edge Use Cases:**
- Real-time control loops
- Local data filtering
- Bandwidth optimization
- Offline operation
- Privacy preservation

**Edge Devices:**
- Raspberry Pi
- Industrial gateways
- Edge servers
- Smart cameras

---

### Architecture

**Device Layer:**
- Sensors and actuators
- MCUs (ESP32, STM32)
- Data collection
- Local processing

**Edge Layer:**
- Gateways
- Local aggregation
- Protocol translation
- Local intelligence

**Cloud Layer:**
- Data storage
- Data processing
- Analytics
- Application logic

**Application Layer:**
- User interfaces
- Dashboards
- Alerts
- Control interfaces

**Data Flow:**
```
Device → MQTT → Edge Gateway → Cloud Broker → Database → Application
```

---

### Data Ingestion

**MQTT:**
- Publish/subscribe model
- Lightweight protocol
- Efficient for IoT
- Quality of Service levels

**HTTP/HTTPS:**
- Request/response model
- RESTful APIs
- Universal compatibility
- Higher overhead

**CoAP:**
- Constrained Application Protocol
- Designed for constrained devices
- UDP-based
- REST-like

**Data Formats:**
- JSON (human-readable, verbose)
- CBOR (binary, compact)
- Protocol Buffers (binary, efficient)
- MessagePack (binary, efficient)

---

### Data Processing

**Time-Series Data:**
- Data indexed by time
- Sensor readings
- Metrics
- Historical analysis

**Aggregation:**
- Summarize data over time windows
- Reduce data volume
- Extract insights
- Support downsampling

**Analytics:**
- Real-time analytics
- Batch analytics
- Predictive analytics
- Anomaly detection

**Stream Processing:**
- Process data as it arrives
- Windowed operations
- Complex event processing
- Real-time alerts

---

### Storage

**Relational Databases:**
- Structured data
- SQL queries
- ACID transactions
- Examples: PostgreSQL, MySQL

**Time-Series Databases:**
- Optimized for time-series data
- Efficient time-based queries
- Compression
- Examples: InfluxDB, TimescaleDB

**Object Storage:**
- Unstructured data
- Scalable
- Cost-effective
- Examples: S3, Blob Storage

**NoSQL Databases:**
- Flexible schema
- Scalable
- Examples: DynamoDB, MongoDB

---

### APIs

**REST (Representational State Transfer):**
- Resource-based
- HTTP methods (GET, POST, PUT, DELETE)
- Stateless
- JSON/XML data

**API Design:**
- Resource naming
- Versioning
- Error handling
- Authentication

**Authentication:**
- API keys
- OAuth 2.0
- JWT (JSON Web Tokens)
- Mutual TLS

**Rate Limiting:**
- Prevent abuse
- Fair usage
- Throttling
- Quotas

---

### Reliability

**Buffering:**
- Store data locally when cloud unavailable
- Queue for later transmission
- Prevent data loss
- Implement persistence

**Retry Strategies:**
- Exponential backoff
- Jitter
- Maximum retries
- Dead letter queue

**Offline Operation:**
- Continue functioning without cloud
- Local decision making
- Data buffering
- Sync when available

**Idempotency:**
- Safe to retry operations
- No side effects from retries
- Important for reliability

---

### Scalability

**Horizontal Scaling:**
- Add more instances
- Load balancing
- Auto-scaling
- Stateless design

**Vertical Scaling:**
- Increase instance size
- More CPU, memory
- Limited by instance size

**Load Balancing:**
- Distribute traffic
- Health checks
- Session affinity
- Geographic distribution

**Auto-scaling:**
- Scale based on demand
- Metrics-based triggers
- Cost optimization
- Performance optimization

---

### Cost Management

**Cost Factors:**
- Compute (CPU, memory)
- Storage
- Network transfer
- API calls
- Data transfer out

**Optimization:**
- Right-sizing resources
- Data compression
- Efficient data formats
- Reserved instances
- Spot instances

**Monitoring:**
- Cost alerts
- Budgets
- Cost allocation
- Usage analysis

---

### Docker

**Containerization:**
- Package application with dependencies
- Consistent environments
- Easy deployment
- Resource isolation

**Docker Concepts:**
- Images
- Containers
- Dockerfile
- Registries
- Compose

**Benefits:**
- Portability
- Reproducibility
- Scalability
- Resource efficiency

---

### Observability

**Monitoring:**
- Metrics (CPU, memory, network)
- Performance monitoring
- Health checks
- Alerting

**Logging:**
- Structured logs
- Log aggregation
- Log analysis
- Search capabilities

**Tracing:**
- Distributed tracing
- Request flow
- Performance analysis
- Debugging

**Dashboards:**
- Visualize metrics
- Real-time monitoring
- Historical analysis
- Alert visualization

---

## Exercises

### Exercise 1: Cloud vs Edge
**Objective:** Understand cloud vs edge computing.

**Tasks:**
1. What is cloud computing?
2. What is edge computing?
3. When would you use cloud?
4. When would you use edge?
5. What are the trade-offs?

**Expected Outcome:** You understand cloud vs edge.

### Exercise 2: Architecture Design
**Objective:** Design IoT system architecture.

**Tasks:**
1. What are the layers of IoT architecture?
2. What is the role of a gateway?
3. How does data flow from device to cloud?
4. What is local-first design?
5. How do you handle offline operation?

**Expected Outcome:** You understand IoT architecture.

### Exercise 3: Data Ingestion
**Objective:** Understand data ingestion methods.

**Tasks:**
1. What is MQTT?
2. What is HTTP?
3. What is CoAP?
4. When would you use MQTT vs HTTP?
5. What are common data formats?

**Expected Outcome:** You understand data ingestion.

### Exercise 4: Time-Series Data
**Objective:** Understand time-series data.

**Tasks:**
1. What is time-series data?
2. What is a time-series database?
3. How do you aggregate time-series data?
4. What is downsampling?
5. What are time-series use cases?

**Expected Outcome:** You understand time-series data.

### Exercise 5: REST APIs
**Objective:** Understand REST API design.

**Tasks:**
1. What is REST?
2. What are HTTP methods?
3. How do you design resources?
4. What is idempotency?
5. How do you handle errors?

**Expected Outcome:** You understand REST APIs.

### Exercise 6: Reliability
**Objective:** Understand reliability strategies.

**Tasks:**
1. What is buffering?
2. What is exponential backoff?
3. What is offline operation?
4. What is idempotency?
5. How do you ensure reliability?

**Expected Outcome:** You understand reliability.

### Exercise 7: Scalability
**Objective:** Understand scalability concepts.

**Tasks:**
1. What is horizontal scaling?
2. What is vertical scaling?
3. What is load balancing?
4. What is auto-scaling?
5. How do you design for scalability?

**Expected Outcome:** You understand scalability.

### Exercise 8: Cost Management
**Objective:** Understand cloud costs.

**Tasks:**
1. What are the main cost factors?
2. How do you optimize costs?
3. What is right-sizing?
4. What are reserved instances?
5. How do you monitor costs?

**Expected Outcome:** You understand cost management.

### Exercise 9: Docker
**Objective:** Understand containerization.

**Tasks:**
1. What is Docker?
2. What is a container?
3. What is an image?
4. What is a Dockerfile?
5. What are the benefits of containers?

**Expected Outcome:** You understand Docker.

### Exercise 10: Observability
**Objective:** Understand observability.

**Tasks:**
1. What is monitoring?
2. What is logging?
3. What is tracing?
4. What is a dashboard?
5. How do you implement observability?

**Expected Outcome:** You understand observability.

---

## Labs

### Lab 1: MQTT Cloud Ingestion
**Objective:** Implement MQTT data ingestion to cloud.

**Prerequisites:**
- MQTT broker (local or cloud)
- ESP32 or Raspberry Pi

**Procedure:**

**1. Cloud MQTT Broker:**
- Use AWS IoT Core or Mosquitto cloud
- Configure authentication
- Create topics

**2. Device Publish:**
```c
#include "mqtt_client.h"

void publish_data() {
    mqtt_client_publish(topic, payload, len, 1, 0);
}
```

**3. Cloud Subscribe:**
- Subscribe to topics
- Process data
- Store in database

**Expected Behavior:**
- Device publishes to cloud broker
- Cloud receives data
- Data stored in database

**Completion Criteria:**
- MQTT cloud ingestion working
- Understanding of cloud MQTT
- Data flow verified

---

### Lab 2: REST API Design
**Objective:** Design and implement REST API.

**Prerequisites:**
- Python or Node.js
- Flask or Express

**Procedure:**

**1. Design API:**
```
GET /devices - List devices
POST /devices - Create device
GET /devices/{id} - Get device
PUT /devices/{id} - Update device
DELETE /devices/{id} - Delete device
```

**2. Implement API (Python Flask):**
```python
from flask import Flask, jsonify, request

app = Flask(__name__)

devices = []

@app.route('/devices', methods=['GET'])
def get_devices():
    return jsonify(devices)

@app.route('/devices', methods=['POST'])
def create_device():
    device = request.json
    devices.append(device)
    return jsonify(device), 201
```

**3. Test API:**
```bash
curl -X GET http://localhost:5000/devices
curl -X POST http://localhost:5000/devices -H "Content-Type: application/json" -d '{"name":"device1"}'
```

**Expected Behavior:**
- API responds correctly
- Resources created and retrieved
- HTTP methods working

**Completion Criteria:**
- REST API implemented
- Understanding of REST design
- API tested

---

### Lab 3: Time-Series Database
**Objective:** Use time-series database for IoT data.

**Prerequisites:**
- InfluxDB or TimescaleDB
- Python or Node.js

**Procedure:**

**1. Install InfluxDB:**
```bash
docker run -d -p 8086:8086 influxdb
```

**2. Write Data:**
```python
from influxdb_client import InfluxDBClient

client = InfluxDBClient(url="http://localhost:8086", token="token", org="org")
write_api = client.write_api()

point = Point("sensor").tag("device", "esp32").field("temperature", 25.5)
write_api.write(bucket="iot", record=point)
```

**3. Query Data:**
```python
query_api = client.query_api()
result = query_api.query('from(bucket:"iot") |> range(start: -1h)')
```

**Expected Behavior:**
- Data written to time-series DB
- Data queried successfully
- Time-based queries working

**Completion Criteria:**
- Time-series database working
- Understanding of time-series data
- Queries successful

---

### Lab 4: Buffering and Retry
**Objective:** Implement data buffering and retry logic.

**Prerequisites:**
- ESP32 or Raspberry Pi
- Local storage

**Procedure:**

**1. Buffer Implementation:**
```python
import json
import os

class DataBuffer:
    def __init__(self, filename):
        self.filename = filename
        self.buffer = []
        self.load()

    def add(self, data):
        self.buffer.append(data)
        self.save()

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.buffer, f)

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.buffer = json.load(f)
```

**2. Retry with Exponential Backoff:**
```python
import time
import random

def publish_with_retry(data, max_retries=5):
    for attempt in range(max_retries):
        try:
            mqtt_client.publish(data)
            return True
        except Exception as e:
            if attempt < max_retries - 1:
                delay = (2 ** attempt) + random.random()
                time.sleep(delay)
    return False
```

**Expected Behavior:**
- Data buffered locally
- Retry on failure
- Exponential backoff working

**Completion Criteria:**
- Buffering implemented
- Retry logic working
- Understanding of reliability

---

### Lab 5: Offline Operation
**Objective:** Implement offline operation with sync.

**Prerequisites:**
- Completed Lab 4

**Procedure:**

**1. Detect Connectivity:**
```python
def is_online():
    try:
        requests.get('http://mqtt-broker', timeout=5)
        return True
    except:
        return False
```

**2. Local Operation:**
```python
def process_data(data):
    if is_online():
        publish_with_retry(data)
    else:
        buffer.add(data)
```

**3. Sync on Reconnect:**
```python
def sync_buffer():
    while buffer.buffer and is_online():
        data = buffer.buffer[0]
        if publish_with_retry(data):
            buffer.buffer.pop(0)
            buffer.save()
```

**Expected Behavior:**
- System works offline
- Data buffered
- Sync on reconnect

**Completion Criteria:**
- Offline operation working
- Sync logic implemented
- Understanding of local-first design

---

### Lab 6: Docker Containerization
**Objective:** Containerize IoT gateway application.

**Prerequisites:**
- Docker installed
- Gateway application

**Procedure:**

**1. Create Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "gateway.py"]
```

**2. Build Image:**
```bash
docker build -t iot-gateway .
```

**3. Run Container:**
```bash
docker run -d --name gateway iot-gateway
```

**4. Compose for Multi-Container:**
```yaml
version: '3'
services:
  gateway:
    build: .
    ports:
      - "5000:5000"
  mqtt:
    image: eclipse-mosquitto
    ports:
      - "1883:1883"
```

**Expected Behavior:**
- Image builds successfully
- Container runs
- Application works in container

**Completion Criteria:**
- Docker containerization working
- Understanding of containers
- Dockerfile created

---

### Lab 7: Monitoring and Logging
**Objective:** Implement monitoring and logging.

**Prerequisites:**
- Running application

**Procedure:**

**1. Structured Logging:**
```python
import logging
import json

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'message': record.getMessage(),
            'logger': record.name
        }
        return json.dumps(log_record)

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
    format='%(message)s'
)
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
```

**2. Metrics Collection:**
```python
import time

class Metrics:
    def __init__(self):
        self.counters = {}
        self.gauges = {}

    def increment(self, name):
        self.counters[name] = self.counters.get(name, 0) + 1

    def set_gauge(self, name, value):
        self.gauges[name] = value

metrics = Metrics()
metrics.increment('messages_sent')
metrics.set_gauge('cpu_usage', 75.5)
```

**3. Health Check Endpoint:**
```python
@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time(),
        'metrics': metrics.gauges
    })
```

**Expected Behavior:**
- Structured logs generated
- Metrics collected
- Health check working

**Completion Criteria:**
- Logging implemented
- Metrics collected
- Health check endpoint

---

### Lab 8: Local-First Design
**Objective:** Design system for local-first operation.

**Prerequisites:**
- Completed previous labs

**Procedure:**

**1. Architecture:**
- Local database (SQLite)
- Local processing
- Cloud sync when available
- UI works offline

**2. Implementation:**
```python
class LocalFirstSystem:
    def __init__(self):
        self.local_db = SQLiteDB()
        self.cloud_client = CloudClient()
        self.buffer = DataBuffer()

    def process(self, data):
        # Always process locally
        self.local_db.insert(data)
        
        # Try cloud sync
        if self.cloud_client.is_available():
            self.sync_to_cloud()
        else:
            self.buffer.add(data)

    def sync_to_cloud(self):
        # Sync buffered data
        while self.buffer.has_data():
            data = self.buffer.get_next()
            if self.cloud_client.send(data):
                self.buffer.remove(data)
```

**Expected Behavior:**
- System works offline
- Local processing continues
- Sync when available

**Completion Criteria:**
- Local-first design implemented
- Offline operation verified
- Sync logic working

---

### Lab 9: Cost Analysis
**Objective:** Analyze and optimize cloud costs.

**Prerequisites:**
- Cloud account (optional, can simulate)

**Procedure:**

**1. Identify Cost Factors:**
- Compute instances
- Storage
- Data transfer
- API calls
- Database operations

**2. Estimate Costs:**
```
Compute: $20/month (t3.medium x 2)
Storage: $10/month (100GB S3)
Data Transfer: $5/month (100GB out)
Database: $15/month (RDS t3.micro)
Total: $50/month
```

**3. Optimization Strategies:**
- Use smaller instances
- Compress data
- Reduce data transfer
- Use reserved instances
- Spot instances for non-critical workloads

**Expected Behavior:**
- Costs identified
- Optimization strategies documented
- Cost reduction plan

**Completion Criteria:**
- Cost analysis performed
- Optimization strategies identified
- Understanding of cloud costs

---

### Lab 10: End-to-End Architecture
**Objective:** Implement complete end-to-end IoT system.

**Prerequisites:**
- Completed previous labs

**Procedure:**

**1. System Components:**
- ESP32 device (sensor)
- Raspberry Pi gateway
- MQTT broker
- Time-series database
- REST API
- Dashboard

**2. Data Flow:**
```
ESP32 → MQTT → Gateway → Processing → Database → API → Dashboard
```

**3. Implementation:**
- Device publishes sensor data
- Gateway subscribes and processes
- Data stored in time-series DB
- API queries data
- Dashboard visualizes

**Expected Behavior:**
- End-to-end data flow working
- All components integrated
- System reliable

**Completion Criteria:**
- Complete system working
- All components integrated
- End-to-end verification

---

## Project

### Project: Edge IoT Gateway

**Objective:** Build a complete edge IoT gateway with cloud integration.

**Requirements:**
- Device connection (MQTT)
- Protocol translation
- Local data buffering
- Cloud sync
- Local time-series database
- REST API
- Monitoring and logging
- Offline operation
- Docker containerization
- Security (TLS, authentication)

**Implementation:**
- Raspberry Pi as gateway
- Mosquitto for MQTT
- InfluxDB for time-series data
- Flask for REST API
- Docker for containerization
- TLS for security

**Deliverables:**
- Working gateway system
- Architecture documentation
- API documentation
- Deployment guide
- Monitoring setup

**Time Estimate:** 20-24 hours

**Project Structure:**
```
edge-iot-gateway/
├── README.md
├── src/
│   ├── gateway.py
│   ├── mqtt_handler.py
│   ├── data_processor.py
│   ├── api.py
│   └── config.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── tests/
│   └── test_gateway.py
├── docs/
│   ├── architecture.md
│   └── api_docs.md
└── results/
    └── performance.md
```

**Note:** This project teaches edge computing, cloud integration, data pipelines, and end-to-end IoT system architecture.

---

## Common Mistakes

### Mistake 1: No Offline Support
**Problem:** System fails when network unavailable
**Consequence:** System unusable offline
**Solution:** Implement buffering and offline operation

### Mistake 2: No Buffering
**Problem:** Data lost during network outage
**Consequence:** Data loss
**Solution:** Implement local buffering

### Mistake 3: No Retry Logic
**Problem:** Transient failures cause permanent failure
**Consequence:** Poor reliability
**Solution:** Implement retry with exponential backoff

### Mistake 4: No Idempotency
**Problem:** Retries cause duplicate operations
**Consequence:** Data corruption
**Solution:** Design idempotent operations

### Mistake 5: Wrong Storage Choice
**Problem:** Using relational DB for time-series data
**Consequence:** Poor performance, high cost
**Solution:** Use time-series database

### Mistake 6: No Monitoring
**Problem:** No visibility into system health
**Consequence:** Issues undetected
**Solution:** Implement monitoring and logging

### Mistake 7: No Cost Management
**Problem:** Unexpected cloud costs
**Consequence:** Budget overruns
**Solution:** Monitor and optimize costs

### Mistake 8: Tight Coupling
**Problem:** Components tightly coupled to cloud provider
**Consequence:** Vendor lock-in
**Solution:** Design for portability

### Mistake 9: No Security
**Problem:** Unencrypted communication
**Consequence:** Data exposure
**Solution:** Use TLS, authentication

### Mistake 10: No Scalability Design
**Problem:** System cannot handle growth
**Consequence:** Performance degradation
**Solution:** Design for scalability from start

---

## Knowledge Test

Answer these questions without looking at the materials:

1. What is cloud computing?
2. What is edge computing?
3. What is the difference between IaaS, PaaS, and SaaS?
4. What is MQTT?
5. What is a time-series database?
6. What is REST?
7. What is idempotency?
8. What is exponential backoff?
9. What is Docker?
10. What is buffering?
11. What is local-first design?
12. What is load balancing?
13. What is auto-scaling?
14. What are the main cloud cost factors?
15. What is monitoring?
16. What is logging?
17. What is CoAP?
18. What is horizontal scaling?
19. What is vertical scaling?
20. How do you design for offline operation?

**Passing Score:** 16/20 correct answers

---

## Practical Test

Complete these practical tasks:

1. **MQTT Ingestion:** Implement MQTT data to cloud
2. **REST API:** Design and implement REST API
3. **Time-Series DB:** Use time-series database for sensor data
4. **Buffering:** Implement data buffering and retry
5. **Offline Operation:** Implement offline operation with sync
6. **Docker:** Containerize gateway application
7. **Monitoring:** Implement monitoring and logging
8. **Local-First:** Design local-first system
9. **Cost Analysis:** Analyze cloud costs
10. **End-to-End:** Implement complete IoT system

**Documentation Required:**
- Architecture diagrams
- API documentation
- Deployment guide
- Cost analysis
- Performance results

**Passing Criteria:** All tasks completed with proper architecture demonstrated.

---

## Completion Checklist

Before moving to Phase 17, verify you have:

- [ ] Understand cloud vs edge computing
- [ ] Can design IoT system architecture
- [ ] Can implement data ingestion (MQTT, HTTP)
- [ ] Can design REST APIs
- [ ] Can use time-series databases
- [ ] Can implement buffering and retry
- [ ] Can design for offline operation
- [ ] Understand scalability concepts
- [ ] Can estimate cloud costs
- [ ] Can implement monitoring and logging
- [ ] Can use Docker for containerization
- [ ] Understand end-to-end architecture
- **Completed Lab 1** - MQTT Cloud Ingestion
- **Completed Lab 2** - REST API Design
- **Completed Lab 3** - Time-Series Database
- **Completed Lab 4** - Buffering and Retry
- **Completed Lab 5** - Offline Operation
- **Completed Lab 6** - Docker Containerization
- **Completed Lab 7** - Monitoring and Logging
- **Completed Lab 8** - Local-First Design
- **Completed Lab 9** - Cost Analysis
- **Completed Lab 10** - End-to-End Architecture
- [ ] Passed the knowledge test (16/20 correct)
- [ ] Passed the practical test
- [ ] Completed the Edge IoT Gateway project

---

## Do Not Continue Until...

**Do not start Phase 17 until:**

1. You have passed the knowledge test (16/20 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You can design IoT system architecture
5. You can implement data ingestion and storage
6. You can design for reliability and offline operation
7. You can implement monitoring and logging
8. You can estimate and optimize cloud costs
9. You can use Docker for containerization
10. You understand end-to-end IoT system design

**Cloud and edge computing are essential for modern IoT systems. Understanding architecture, data pipelines, reliability, scalability, and cost management is critical before learning professional MCU development with STM32, where resource constraints and real-time requirements require different design approaches.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 17 — STM32**

Phase 17 will teach you professional MCU development with STM32, ARM Cortex-M architecture, register-level programming, and debugging, building on the embedded systems knowledge you have acquired throughout the curriculum.

---

**Cloud and edge computing provide the infrastructure for scalable, reliable IoT systems. Understanding architecture, data flow, reliability, and cost management is essential for building production-grade IoT solutions.**
