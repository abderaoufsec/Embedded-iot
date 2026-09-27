# Phase 10 — MQTT and IoT

> **Goal:** Develop practical expertise in MQTT protocol and IoT architecture, enabling you to build complete networked embedded systems that publish telemetry, receive commands, and integrate into IoT monitoring systems.
>
> **Prerequisite:** Phase 6 — ESP32, Phase 9 — Networking
>
> **Outcome:** You can implement MQTT on ESP32, design IoT architectures, build telemetry systems, and understand publish/subscribe messaging patterns.

---

## What You Will Learn

By completing this phase, you will understand:

- **MQTT Fundamentals:** Publish/subscribe architecture, broker, client, topics, messaging
- **MQTT Protocol:** Control packets, connection lifecycle, QoS levels, retained messages, Last Will and Testament
- **MQTT Topics:** Topic hierarchy, wildcards, topic design best practices
- **MQTT Broker:** Role, installation, configuration, Mosquitto
- **MQTT Security:** Authentication, authorization, TLS, secure vs insecure connections
- **ESP32 + MQTT:** Wi-Fi connection, MQTT connection, publishing, subscribing, reconnect logic
- **Payload Formats:** Plain text, numeric, JSON, tradeoffs
- **IoT Architecture:** Device → Connectivity → Messaging → Processing → Storage → Visualization
- **Debugging:** MQTT troubleshooting, broker logs, Wireshark, MQTT CLI tools
- **Practical Implementation:** Building complete IoT monitoring nodes

---

## Prerequisites

**Before starting this phase, you should have:**

- ✅ Completed Phase 0 — Orientation
- ✅ Completed Phase 1 — Computer Fundamentals
- ✅ Completed Phase 2 — C Programming
- ✅ Completed Phase 3 — Digital Electronics
- ✅ Completed Phase 4 — Electronics
- ✅ Completed Phase 5 — Microcontrollers
- ✅ Completed Phase 6 — ESP32
- ✅ Completed Phase 7 — Sensors and Actuators
- ✅ Completed Phase 8 — Embedded Communication
- ✅ Completed Phase 9 — Networking
- ✅ Understanding of ESP32 Wi-Fi from Phase 6
- ✅ Understanding of TCP/IP from Phase 9
- ✅ Understanding of sockets from Phase 9

**Hardware required for labs:**
- ESP32 development board
- Sensor (e.g., temperature sensor DS18B20, or potentiometer for analog)
- LED and resistor (220Ω or 330Ω)
- Breadboard and jumper wires
- PC with network connectivity

**Software required:**
- Arduino IDE or ESP-IDF
- Mosquitto MQTT broker (open-source)
- MQTT client tools (MQTTX, mosquitto_pub/sub, or similar)
- Serial terminal software

---

## Learning Outcomes

After completing this phase, you will be able to:

- Explain MQTT publish/subscribe architecture
- Understand MQTT control packets and connection lifecycle
- Choose appropriate QoS levels for different applications
- Design MQTT topic hierarchies
- Install and configure Mosquitto MQTT broker
- Implement MQTT clients on ESP32
- Publish telemetry data with structured payloads
- Subscribe to commands and control actuators
- Implement reconnection logic for MQTT and Wi-Fi
- Understand MQTT security fundamentals
- Design basic IoT architectures
- Debug MQTT connectivity issues
- Build complete IoT monitoring nodes

---

## Concepts

### What is MQTT?

**MQTT (Message Queuing Telemetry Transport):**
- Lightweight publish/subscribe messaging protocol
- Designed for constrained devices and low-bandwidth networks
- Originally developed by IBM (now OASIS standard)
- Ideal for IoT and embedded systems

**Why MQTT Exists:**
- HTTP is request/response (not ideal for real-time)
- HTTP has high overhead (headers, text-based)
- MQTT is binary, lightweight, efficient
- MQTT supports one-to-many communication natively
- MQTT works well on unreliable networks

**MQTT vs HTTP:**

| Characteristic | MQTT | HTTP |
|---------------|------|------|
| Architecture | Publish/Subscribe | Request/Response |
| Overhead | Low (2-byte header) | High (text headers) |
| Communication | One-to-many (natively) | One-to-one |
| Latency | Low | Higher |
| Bandwidth | Efficient | Less efficient |
| State | Broker maintains state | Stateless |
| Use Case | IoT, telemetry, real-time | Web, API, file transfer |

**When to Use MQTT:**
- IoT devices with limited resources
- Real-time telemetry
- One-to-many communication
- Unreliable networks
- Low bandwidth requirements
- Sensor networks

**When to Use HTTP:**
- Web applications
- REST APIs
- File transfer
- Request/response patterns
- When HTTP infrastructure already exists

---

### MQTT Architecture

**Publish/Subscribe Pattern:**

**Publisher:**
- Device that sends messages
- Does not know who receives messages
- Publishes to a topic

**Subscriber:**
- Device that receives messages
- Subscribes to topics of interest
- Does not know who published messages

**Broker:**
- Central server that routes messages
- Maintains client connections
- Routes messages from publishers to subscribers
- Maintains session state
- Handles authentication and authorization

**Decoupling:**
- Publishers and subscribers are decoupled
- They don't need to know about each other
- Broker handles routing
- Enables flexible architectures

**Example Architecture:**
```
Temperature Sensor (Publisher)
    ↓
    MQTT Broker
    ↓
    ↓                    ↓
Dashboard (Subscriber)  Database (Subscriber)
```

**Why This Matters:**
- Decoupling enables scalable systems
- New subscribers can be added without changing publishers
- Publishers can be added without changing subscribers
- Broker centralizes communication logic

---

### MQTT Topics

**Topic:**
- Hierarchical string that identifies message content
- UTF-8 encoded
- Case-sensitive
- Example: `sensors/temperature/living-room`

**Topic Hierarchy:**
- Separated by forward slash `/`
- Examples:
  - `sensors/temperature`
  - `sensors/temperature/room1`
  - `devices/device01/status`
  - `home/living-room/light`

**Topic Design Principles:**
- Use forward slash `/` as separator
- Use descriptive names
- Keep hierarchy logical
- Avoid spaces and special characters
- Use consistent naming convention

**Generic Examples:**
```
sensors/temperature
sensors/humidity
sensors/pressure
devices/device01/telemetry
devices/device01/status
devices/device01/commands
home/living-room/temperature
home/kitchen/humidity
industrial/machine01/vibration
industrial/machine01/current
```

**Topic Wildcards:**

**Single-level wildcard: `+`**
- Matches exactly one topic level
- Example: `sensors/+/temperature` matches:
  - `sensors/room1/temperature`
  - `sensors/room2/temperature`
- Does NOT match:
  - `sensors/room1/room2/temperature`

**Multi-level wildcard: `#`**
- Matches zero or more topic levels
- Must be the last character in subscription
- Example: `sensors/#` matches:
  - `sensors/temperature`
  - `sensors/room1/temperature`
  - `sensors/room1/room2/temperature`
- Does NOT match:
  - `sensors` (depending on broker implementation)

**Example Subscriptions:**
- `sensors/temperature` - Exact match
- `sensors/+` - All sensors (one level)
- `sensors/#` - All sensors and subtopics
- `devices/+/status` - All device status topics
- `home/living-room/#` - All living-room topics

**Why This Matters:**
- Topic design affects system architecture
- Wildcards enable flexible subscriptions
- Good topic design scales with system growth

---

### MQTT Messages

**Message Components:**
- **Topic:** Where message is published
- **Payload:** Actual data (can be empty)
- **QoS:** Quality of Service level
- **Retain flag:** Whether broker should retain message
- **Properties:** MQTT 5.0 additional metadata

**Payload Formats:**

**Plain Text:**
- Simple string
- Example: `25.4`
- Pros: Simple, human-readable
- Cons: Limited structure, no typing

**Numeric:**
- Number in string
- Example: `25.4` or `25`
- Pros: Simple for single values
- Cons: No metadata, ambiguous

**JSON:**
- Structured data
- Example:
```json
{
  "device_id": "device01",
  "temperature": 25.4,
  "humidity": 60.2,
  "timestamp": 1234567890
}
```
- Pros: Structured, typed, extensible
- Cons: Larger size, requires parsing

**Payload Design:**
- Include device identification
- Include timestamp when useful
- Include units in value or metadata
- Keep size reasonable for constrained devices
- Validate on receiver side

**Why This Matters:**
- Payload design affects interoperability
- Structured payloads enable complex systems
- Size affects bandwidth and processing

---

### MQTT Control Packets

**MQTT is binary protocol with control packets:**

**CONNECT:**
- Client connects to broker
- Includes client ID, credentials, will message
- Broker responds with CONNACK

**CONNACK:**
- Broker response to CONNECT
- Indicates connection accepted or rejected
- Includes return code

**PUBLISH:**
- Client publishes message to topic
- Includes topic, payload, QoS, retain flag

**PUBACK:**
- Acknowledgment for QoS 1 publish
- Confirms message received

**PUBREC:**
- Received acknowledgment for QoS 2 publish

**PUBREL:**
- Release for QoS 2 publish

**PUBCOMP:**
- Complete for QoS 2 publish

**SUBSCRIBE:**
- Client subscribes to topics
- Includes topic filters and QoS levels
- Broker responds with SUBACK

**SUBACK:**
- Broker acknowledgment of subscription
- Includes granted QoS levels

**UNSUBSCRIBE:**
- Client unsubscribes from topics
- Broker responds with UNSUBACK

**UNSUBACK:**
- Broker acknowledgment of unsubscription

**PINGREQ:**
- Client keep-alive ping
- Maintains connection

**PINGRESP:**
- Broker response to PINGREQ
- Confirms connection alive

**DISCONNECT:**
- Client disconnects gracefully
- Broker cleans up session

**Why This Matters:**
- Understanding control packets helps debugging
- Connection lifecycle affects reliability
- QoS levels use different packet flows

---

### MQTT Quality of Service (QoS)

**QoS defines message delivery guarantees:**

**QoS 0 - At Most Once:**
- Fire and forget
- No acknowledgment
- Message may be lost
- Lowest overhead
- Fastest
- Use for: Non-critical data, frequent updates

**QoS 1 - At Least Once:**
- Acknowledgment required
- Message may be duplicated
- Guaranteed delivery (eventually)
- Medium overhead
- Use for: Important telemetry, commands

**QoS 2 - Exactly Once:**
- Four-way handshake
- No duplication, no loss
- Highest overhead
- Slowest
- Use for: Critical commands, financial transactions

**QoS Flow:**

**QoS 0:**
```
Publisher → PUBLISH → Broker → PUBLISH → Subscriber
```

**QoS 1:**
```
Publisher → PUBLISH → Broker → PUBACK → Publisher
Publisher → PUBLISH → Subscriber
```

**QoS 2:**
```
Publisher → PUBLISH → Broker → PUBREC → Publisher
Publisher → PUBREL → Broker → PUBCOMP → Publisher
Broker → PUBLISH → Subscriber → PUBACK → Broker
```

**Choosing QoS:**
- **Temperature sensor:** QoS 0 (frequent updates, loss acceptable)
- **Important command:** QoS 1 (guaranteed delivery)
- **Critical action:** QoS 2 (exactly once, no duplication)
- **Status update:** QoS 1 (ensure received)

**Why This Matters:**
- QoS affects reliability and performance
- Higher QoS = more overhead
- Choose appropriate QoS for use case

---

### Retained Messages

**Retained Message:**
- Broker stores last message on topic
- New subscribers receive retained message immediately
- Useful for state, configuration, status

**Use Cases:**
- Device status (online/offline)
- Current temperature
- Configuration values
- Last known state

**Example:**
```
Device publishes to: devices/device01/status
Payload: "online"
Retain flag: true

New subscriber to devices/device01/status
Immediately receives: "online"
```

**Behavior:**
- Only last retained message stored
- New retained message replaces previous
- Broker removes retained message if message with retain=0 published
- Some brokers have limits on retained message size

**Design Considerations:**
- Use for state, not events
- Keep payload size reasonable
- Don't use for high-frequency data
- Clear retained messages when appropriate

**Why This Matters:**
- Retained messages provide immediate state
- Useful for dashboards and monitoring
- Prevents stale data on new connections

---

### Last Will and Testament (LWT)

**LWT:**
- Message broker publishes if client disconnects unexpectedly
- Configured during CONNECT
- Indicates client died or lost connection

**Use Cases:**
- Device offline notification
- Connection loss alert
- System health monitoring

**Example:**
```
Client connects with LWT:
Topic: devices/device01/status
Payload: "offline"
QoS: 1
Retain: true

If client disconnects unexpectedly:
Broker publishes to devices/device01/status
Payload: "offline"
```

**Graceful vs Unexpected:**
- Graceful DISCONNECT: LWT not published
- Unexpected disconnect: LWT published
- Lost connection: LWT published

**Design Considerations:**
- Use LWT for offline status
- Configure appropriate QoS
- Consider retain flag for state
- Test disconnection scenarios

**Why This Matters:**
- LWT provides connection monitoring
- Critical for health and status systems
- Enables automated alerting

---

### MQTT Sessions

**Session:**
- State maintained by broker for client
- Includes subscriptions and undelivered messages
- Identified by client ID

**Clean Session:**
- `clean session = true`: Broker discards session state on disconnect
- `clean session = false`: Broker maintains session state across reconnects

**Session State:**
- Subscriptions
- Undelivered QoS 1/2 messages
- Client ID

**Use Cases:**
- **Clean session true:** Temporary clients, mobile devices
- **Clean session false:** Persistent devices, reliable delivery

**Client ID:**
- Must be unique per broker
- If duplicate client ID connects, previous connection terminated
- Can be auto-generated by some libraries
- Use consistent ID for reconnection

**Why This Matters:**
- Session behavior affects message delivery
- Clean session vs persistent affects reliability
- Client ID conflicts cause connection issues

---

### MQTT Broker

**Broker Role:**
- Central message router
- Maintains client connections
- Handles authentication and authorization
- Stores retained messages
- Manages sessions
- Enforces QoS guarantees

**Mosquitto:**
- Open-source MQTT broker
- Lightweight, easy to install
- Widely used
- Supports MQTT 3.1.1 and 5.0

**Installation:**
- **Windows:** Download installer from mosquitto.org
- **Linux:** `sudo apt install mosquitto mosquitto-clients`
- **macOS:** `brew install mosquitto`

**Configuration:**
- Configuration file: `mosquitto.conf`
- Default port: 1883 (insecure), 8883 (TLS)
- Basic authentication
- Access control lists

**Starting Broker:**
```bash
# Default configuration
mosquitto

# With configuration file
mosquitto -c mosquitto.conf

# With verbose logging
mosquitto -v
```

**Testing Broker:**
```bash
# Subscribe to topic
mosquitto_sub -h localhost -t "test/topic"

# Publish to topic
mosquitto_pub -h localhost -t "test/topic" -m "Hello"
```

**Why This Matters:**
- Broker is central to MQTT architecture
- Understanding broker configuration is essential
- Local broker enables development and testing

---

### MQTT Security

**Why Security Matters:**
- Unauthenticated MQTT allows anyone to connect
- Unencrypted MQTT exposes data
- Unauthorized access can control devices
- IoT devices often deployed in insecure environments

**Authentication:**
- Verify client identity
- Username/password
- Client certificates (TLS)
- Token-based (less common)

**Authorization:**
- Control what clients can do
- Topic access control
- ACL (Access Control List)
- Publish/subscribe permissions

**TLS (Transport Layer Security):**
- Encrypts communication
- Port 8883 (vs 1883 for insecure)
- Prevents eavesdropping
- Validates broker identity

**Ports:**
- **1883:** MQTT over TCP (insecure)
- **8883:** MQTT over TLS (secure)
- **8083:** MQTT over WebSockets (insecure)
- **8084:** MQTT over secure WebSockets

**Credential Management:**
- Never hardcode credentials in source code
- Use environment variables
- Use configuration files (secured)
- Use secure storage (ESP32 NVS)

**Mosquitto Security:**
```conf
# Password file
password_file /etc/mosquitto/passwd

# Allow anonymous (disable for security)
allow_anonymous false

# ACL file
acl_file /etc/mosquitto/acl
```

**Why This Matters:**
- Security is critical for IoT
- Unsecured devices can be exploited
- Authentication and authorization protect systems

---

### ESP32 + MQTT

**Building on Phase 6 and 9:**

**Workflow:**
1. Connect to Wi-Fi (Phase 6, 9)
2. Connect to MQTT broker
3. Publish telemetry
4. Subscribe to commands
5. Process incoming messages
6. Handle disconnections
7. Reconnect as needed

**ESP32 MQTT Libraries:**
- **Arduino-ESP32:** PubSubClient library
- **ESP-IDF:** ESP-MQTT component

**Connection Lifecycle:**
```
Setup
  ↓
Wi-Fi Connect
  ↓
MQTT Connect
  ↓
Subscribe to topics
  ↓
Loop:
  - Read sensors
  - Publish telemetry
  - Process incoming messages
  - Check connection
  - Reconnect if needed
```

**Publishing:**
```cpp
client.publish("sensors/temperature", "25.4");
```

**Subscribing:**
```cpp
client.subscribe("devices/device01/commands");
```

**Callback:**
```cpp
void callback(char* topic, byte* payload, unsigned int length) {
  // Process incoming message
}
```

**Reconnection Logic:**
- Check Wi-Fi connection
- Check MQTT connection
- Reconnect Wi-Fi if needed
- Reconnect MQTT if needed
- Resubscribe to topics after reconnect

**Why This Matters:**
- ESP32 MQTT enables IoT systems
- Reconnection logic is critical for reliability
- Wi-Fi and MQTT both need robust handling

---

### IoT Architecture

**Basic IoT Architecture:**

**Device Layer:**
- Sensors, actuators, microcontrollers
- Data acquisition, control
- Local processing

**Connectivity Layer:**
- Network interfaces (Wi-Fi, Ethernet, cellular)
- Communication protocols (MQTT, HTTP, CoAP)
- Edge gateway

**Messaging Layer:**
- Message broker (MQTT broker)
- Message routing
- Protocol translation

**Processing Layer:**
- Data processing
- Analytics
- Business logic
- Rules engine

**Storage Layer:**
- Time-series databases
- Relational databases
- Cloud storage
- Local storage

**Visualization Layer:**
- Dashboards
- Mobile apps
- Web interfaces
- Alerts

**Example Architecture:**
```
Sensor Device
    ↓ (Wi-Fi)
    ↓
    MQTT Broker
    ↓
    ↓                    ↓                    ↓
Dashboard          Database           Rule Engine
```

**Generic IoT System Example:**
```
Industrial Sensor Node
    ↓
    ESP32
    ↓
    Wi-Fi
    ↓
    MQTT Broker
    ↓
    ↓                    ↓
Monitoring Dashboard   Database
```

**Why This Matters:**
- Understanding architecture enables system design
- Each layer has specific responsibilities
- IoT systems are multi-layered

---

## Exact Resources

### Resource 1: MQTT Specification
- **Provider:** OASIS (Official)
- **Level:** Advanced
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Official MQTT 3.1.1 and 5.0 specifications
- **URL:** https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html

### Resource 2: Mosquitto Documentation
- **Provider:** Eclipse Foundation (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Mosquitto MQTT broker documentation
- **URL:** https://mosquitto.org/documentation/

### Resource 3: HiveMQ MQTT Essentials
- **Provider:** HiveMQ (Structured learning)
- **Level:** Beginner
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Comprehensive MQTT tutorial series
- **URL:** https://www.hivemq.com/mqtt-essentials/

### Resource 4: ESP-MQTT Documentation
- **Provider:** Espressif (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** ESP-IDF MQTT component documentation
- **URL:** https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/mqtt.html

### Resource 5: PubSubClient Library
- **Provider:** Nick O'Leary (Open Source)
- **Level:** Beginner
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Arduino MQTT client library
- **URL:** https://pubsubclient.knolleary.net/

### Resource 6: MQTTX Client
- **Provider:** EMQX (Open Source)
- **Level:** Beginner
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Cross-platform MQTT client tool
- **URL:** https://mqttx.app/

---

## Study Order

Follow this exact sequence:

1. **Study MQTT fundamentals** (what is MQTT, why it exists, architecture)
2. **Understand publish/subscribe pattern**
3. **Study MQTT topics and wildcards**
4. **Study MQTT control packets and connection lifecycle**
5. **Study QoS levels** (0, 1, 2)
6. **Study retained messages**
7. **Study Last Will and Testament**
8. **Study MQTT sessions and client IDs**
9. **Study MQTT broker role** (Mosquitto)
10. **Study MQTT security** (authentication, authorization, TLS)
11. **Study ESP32 + MQTT workflow**
12. **Study payload formats** (plain text, JSON)
13. **Study IoT architecture** (device → connectivity → messaging → processing → storage → visualization)
14. **Complete all exercises**
15. **Complete all labs**
16. **Complete the project**
17. **Take the knowledge test**
18. **Take the practical test**
19. **Review completion checklist**

---

## Exercises

### Exercise 1: MQTT Architecture

**Objective:** Understand MQTT publish/subscribe architecture.

**Tasks:**
1. Draw an MQTT architecture with 2 publishers and 3 subscribers
2. Explain the role of the broker
3. How are publishers and subscribers decoupled?
4. What happens if a new subscriber joins?
5. What happens if a publisher disconnects?

**Expected Outcome:** You understand MQTT architecture and decoupling.

### Exercise 2: Topic Design

**Objective:** Design MQTT topic hierarchies.

**Tasks:**
1. Design a topic hierarchy for temperature sensors in multiple rooms
2. Design a topic hierarchy for device status and commands
3. Design a topic hierarchy for an industrial machine monitoring system
4. Explain what `sensors/+/temperature` matches
5. Explain what `home/living-room/#` matches

**Expected Outcome:** You can design effective topic hierarchies.

### Exercise 3: QoS Selection

**Objective:** Choose appropriate QoS levels.

**Tasks:**
1. A temperature sensor updates every second. What QoS?
2. A critical command to turn off a machine. What QoS?
3. A heartbeat/status message. What QoS?
4. A financial transaction message. What QoS?
5. Explain the tradeoff between QoS level and overhead.

**Expected Outcome:** You can choose appropriate QoS for use cases.

### Exercise 4: Retained Messages

**Objective:** Understand retained message behavior.

**Tasks:**
1. When should you use retained messages?
2. When should you NOT use retained messages?
3. How does a new subscriber benefit from retained messages?
4. How do you clear a retained message?
5. What happens if multiple retained messages are published to the same topic?

**Expected Outcome:** You understand retained message use cases.

### Exercise 5: Payload Design

**Objective:** Design effective MQTT payloads.

**Tasks:**
1. Design a JSON payload for temperature telemetry
2. Design a JSON payload for device status
3. Why include a timestamp in payload?
4. Why include device ID in payload?
5. What are the tradeoffs between plain text and JSON?

**Expected Outcome:** You can design effective payloads.

### Exercise 6: Security Considerations

**Objective:** Understand MQTT security requirements.

**Tasks:**
1. Why is unauthenticated MQTT dangerous?
2. What is the difference between port 1883 and 8883?
3. Why should you never hardcode credentials?
4. What is the difference between authentication and authorization?
5. How would you secure credentials on an ESP32?

**Expected Outcome:** You understand MQTT security fundamentals.

---

## Labs

### Lab 1: MQTT Concepts Simulation

**Objective:** Understand MQTT publish/subscribe without hardware.

**Prerequisites:**
- Understanding of MQTT fundamentals

**Components:**
- None (conceptual)

**Theory:**
- Simulate MQTT system with paper/whiteboard
- Practice topic design
- Practice wildcard subscriptions

**Exercise:**
1. Design a topic hierarchy for a home automation system
2. Identify publishers (sensors) and subscribers (controllers, dashboards)
3. Show which topics each device publishes/subscribes to
4. Use wildcards to show flexible subscriptions
5. Show what happens when a new device is added

**Expected Outcome:**
- Clear understanding of MQTT architecture
- Practice with topic design
- Understanding of publish/subscribe decoupling

**Completion Criteria:**
- Can design topic hierarchies
- Understand publish/subscribe pattern
- Can identify publishers and subscribers

---

### Lab 2: Local MQTT Broker

**Objective:** Install and run Mosquitto MQTT broker locally.

**Prerequisites:**
- PC with network connectivity

**Components:**
- PC

**Theory:**
- Mosquitto is open-source MQTT broker
- Runs locally for development
- Default port 1883

**Procedure:**

**Windows:**
1. Download Mosquitto from https://mosquitto.org/download/
2. Install with default settings
3. Start Mosquitto from Start Menu or command line
4. Verify broker is running (should see no errors)

**Linux:**
```bash
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl start mosquitto
sudo systemctl status mosquitto
```

**macOS:**
```bash
brew install mosquitto
brew services start mosquitto
```

**Testing:**
```bash
# Terminal 1: Subscribe
mosquitto_sub -h localhost -t "test/topic" -v

# Terminal 2: Publish
mosquitto_pub -h localhost -t "test/topic" -m "Hello MQTT"
```

**Expected Behavior:**
- Broker starts without errors
- Subscribe terminal shows published message
- No connection errors

**Troubleshooting:**
- Port already in use: Check for other MQTT brokers
- Connection refused: Check broker is running
- Permission denied: Use sudo on Linux

**Completion Criteria:**
- Mosquitto installed and running
- Can publish and subscribe
- Understand broker role

---

### Lab 3: MQTT CLI Tools

**Objective:** Use Mosquitto CLI tools for testing.

**Prerequisites:**
- Completed Lab 2
- Mosquitto broker running

**Components:**
- PC with Mosquitto installed

**Theory:**
- `mosquitto_pub`: Publish messages
- `mosquitto_sub`: Subscribe to topics
- `-v`: Verbose mode (show topic)
- `-r`: Retain flag
- `-q`: QoS level

**Procedure:**

**Basic Publish/Subscribe:**
```bash
# Terminal 1: Subscribe
mosquitto_sub -h localhost -t "sensors/temperature" -v

# Terminal 2: Publish
mosquitto_pub -h localhost -t "sensors/temperature" -m "25.4"
```

**Multiple Subscribers:**
```bash
# Terminal 1: Subscribe
mosquitto_sub -h localhost -t "sensors/temperature" -v

# Terminal 2: Subscribe
mosquitto_sub -h localhost -t "sensors/temperature" -v

# Terminal 3: Publish
mosquitto_pub -h localhost -t "sensors/temperature" -m "25.4"
# Both subscribers receive message
```

**Wildcards:**
```bash
# Terminal 1: Subscribe with wildcard
mosquitto_sub -h localhost -t "sensors/+" -v

# Terminal 2: Publish to different topics
mosquitto_pub -h localhost -t "sensors/temperature" -m "25.4"
mosquitto_pub -h localhost -t "sensors/humidity" -m "60.2"
# Subscriber receives both
```

**Retained Messages:**
```bash
# Publish with retain
mosquitto_pub -h localhost -t "devices/device01/status" -m "online" -r

# New subscriber immediately receives retained message
mosquitto_sub -h localhost -t "devices/device01/status" -v
```

**QoS Levels:**
```bash
# Publish with QoS 1
mosquitto_pub -h localhost -t "sensors/temperature" -m "25.4" -q 1

# Publish with QoS 2
mosquitto_pub -h localhost -t "sensors/temperature" -m "25.4" -q 2
```

**Expected Behavior:**
- Messages published to subscribed topics
- Wildcards match appropriately
- Retained messages received by new subscribers
- QoS levels configurable

**Document:**
- Examples of each command
- Wildcard behavior
- Retained message behavior

**Completion Criteria:**
- Can use mosquitto_pub and mosquitto_sub
- Understand wildcards
- Understand retained messages
- Understand QoS configuration

---

### Lab 4: QoS Demonstration

**Objective:** Observe QoS behavior differences.

**Prerequisites:**
- Completed Lab 2
- Mosquitto broker running

**Components:**
- PC with Mosquitto installed

**Theory:**
- QoS 0: No acknowledgment
- QoS 1: At least once (may duplicate)
- QoS 2: Exactly once (four-way handshake)

**Procedure:**

**QoS 0:**
```bash
# Terminal 1: Subscribe
mosquitto_sub -h localhost -t "test/qos0" -v

# Terminal 2: Publish QoS 0
mosquitto_pub -h localhost -t "test/qos0" -m "QoS 0 message" -q 0
# Message delivered (no acknowledgment visible in CLI)
```

**QoS 1:**
```bash
# Terminal 1: Subscribe
mosquitto_sub -h localhost -t "test/qos1" -v

# Terminal 2: Publish QoS 1
mosquitto_pub -h localhost -t "test/qos1" -m "QoS 1 message" -q 1
# Message delivered with acknowledgment
```

**QoS 2:**
```bash
# Terminal 1: Subscribe
mosquitto_sub -h localhost -t "test/qos2" -v

# Terminal 2: Publish QoS 2
mosquitto_pub -h localhost -t "test/qos2" -m "QoS 2 message" -q 2
# Message delivered with full handshake
```

**Broker Logs:**
```bash
# Start broker with verbose logging
mosquitto -v

# Observe QoS handshakes in logs
```

**Expected Behavior:**
- QoS 0: Simple delivery
- QoS 1: Acknowledgment visible in verbose logs
- QoS 2: Multiple steps visible in verbose logs

**Document:**
- Observed differences between QoS levels
- Broker log output for each QoS

**Completion Criteria:**
- Understand QoS level differences
- Can observe QoS behavior in logs
- Can choose appropriate QoS

---

### Lab 5: MQTT Security Basics

**Objective:** Configure basic MQTT authentication.

**Prerequisites:**
- Completed Lab 2
- Mosquitto broker installed

**Components:**
- PC with Mosquitto installed

**Theory:**
- Authentication verifies client identity
- Username/password basic authentication
- Disable anonymous access for security

**Procedure:**

**Create Password File:**
```bash
# Create password file
mosquitto_passwd -c /etc/mosquitto/passwd username
# Enter password when prompted
```

**Configure Broker:**
```bash
# Create configuration file
echo "listener 1883" > mosquitto.conf
echo "allow_anonymous false" >> mosquitto.conf
echo "password_file /etc/mosquitto/passwd" >> mosquitto.conf
```

**Start Broker with Config:**
```bash
mosquitto -c mosquitto.conf
```

**Test Authentication:**
```bash
# Try without credentials (should fail)
mosquitto_sub -h localhost -t "test/topic"

# Try with credentials (should succeed)
mosquitto_sub -h localhost -t "test/topic" -u username -P password
```

**Publish with Authentication:**
```bash
mosquitto_pub -h localhost -t "test/topic" -m "Hello" -u username -P password
```

**Expected Behavior:**
- Connection without credentials fails
- Connection with credentials succeeds
- Messages published and received

**Document:**
- Configuration file contents
- Authentication testing results

**Troubleshooting:**
- Permission denied: Check file permissions
- Authentication fails: Verify username/password
- Configuration error: Check mosquitto.conf syntax

**Completion Criteria:**
- Can configure basic authentication
- Understand authentication vs authorization
- Can connect with credentials

---

### Lab 6: ESP32 MQTT Connection

**Objective:** Connect ESP32 to MQTT broker.

**Prerequisites:**
- Completed Phase 6 (ESP32)
- Completed Phase 9 (Networking)
- Completed Lab 2 (Mosquitto broker running)
- ESP32 development board

**Components:**
- ESP32 development board
- USB cable
- Wi-Fi network
- Mosquitto broker (local or accessible)

**Theory:**
- ESP32 connects to Wi-Fi first
- Then connects to MQTT broker
- Uses PubSubClient library for Arduino-ESP32

**Arduino-ESP32 Code:**
```cpp
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";
const char* mqtt_server = "192.168.1.100";  // Broker IP

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  
  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
  
  // Configure MQTT
  client.setServer(mqtt_server, 1883);
  
  // Connect to MQTT
  if (client.connect("ESP32Client")) {
    Serial.println("MQTT connected");
  } else {
    Serial.print("MQTT failed, rc=");
    Serial.print(client.state());
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (client.connect("ESP32Client")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}
```

**Expected Behavior:**
- ESP32 connects to Wi-Fi
- ESP32 connects to MQTT broker
- Serial monitor shows connection status

**Document:**
- Wi-Fi IP address
- MQTT broker IP
- Connection success/failure

**Troubleshooting:**
- Wi-Fi fails: Check SSID/password, signal strength
- MQTT fails: Check broker IP, broker running, network connectivity
- Connection drops: Check broker logs, network stability

**Completion Criteria:**
- ESP32 connects to Wi-Fi
- ESP32 connects to MQTT broker
- Understand connection workflow

---

### Lab 7: ESP32 Telemetry Publishing

**Objective:** Publish sensor telemetry via MQTT.

**Prerequisites:**
- Completed Lab 6
- Sensor (temperature sensor or potentiometer)

**Components:**
- ESP32 development board
- Sensor (DS18B20 or potentiometer)
- Mosquitto broker running

**Theory:**
- Read sensor data
- Format as JSON payload
- Publish to MQTT topic
- Use QoS 1 for reliability

**Arduino-ESP32 Code:**
```cpp
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";
const char* mqtt_server = "192.168.1.100";

WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  client.setServer(mqtt_server, 1883);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  
  unsigned long now = millis();
  if (now - lastMsg > 5000) {
    lastMsg = now;
    
    // Read sensor (example: potentiometer)
    int sensorValue = analogRead(A0);
    float voltage = sensorValue * (3.3 / 4095.0);
    
    // Create JSON payload
    char payload[100];
    snprintf(payload, sizeof(payload), 
             "{\"device_id\":\"esp32_01\",\"value\":%.2f}", voltage);
    
    // Publish
    client.publish("sensors/voltage", payload);
    Serial.println("Published: " + String(payload));
  }
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect("ESP32Client")) {
      Serial.println("connected");
    } else {
      delay(5000);
    }
  }
}
```

**Expected Behavior:**
- ESP32 reads sensor every 5 seconds
- JSON payload published to MQTT topic
- Serial monitor shows published payload

**Verify with Mosquitto:**
```bash
mosquitto_sub -h localhost -t "sensors/voltage" -v
```

**Document:**
- Sensor readings
- Published payloads
- MQTT topic used

**Completion Criteria:**
- Sensor data read successfully
- JSON payload formatted correctly
- Message published to MQTT
- Subscriber receives messages

---

### Lab 8: ESP32 Command Subscription

**Objective:** Subscribe to commands and control output.

**Prerequisites:**
- Completed Lab 6
- LED and resistor

**Components:**
- ESP32 development board
- LED
- Resistor (220Ω or 330Ω)
- Mosquitto broker running

**Theory:**
- Subscribe to command topic
- Process incoming messages
- Control GPIO based on command
- Callback function handles incoming messages

**Arduino-ESP32 Code:**
```cpp
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";
const char* mqtt_server = "192.168.1.100";
const int ledPin = 2;  // Built-in LED

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  
  if (client.connect("ESP32Client")) {
    client.subscribe("devices/esp32_01/commands");
    Serial.println("MQTT connected and subscribed");
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("]: ");
  
  String message = "";
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  Serial.println(message);
  
  // Process command
  if (message == "ON") {
    digitalWrite(ledPin, HIGH);
  } else if (message == "OFF") {
    digitalWrite(ledPin, LOW);
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}

void reconnect() {
  while (!client.connected()) {
    if (client.connect("ESP32Client")) {
      client.subscribe("devices/esp32_01/commands");
    } else {
      delay(5000);
    }
  }
}
```

**Expected Behavior:**
- ESP32 subscribes to command topic
- LED turns on/off based on command
- Serial monitor shows received commands

**Test with Mosquitto:**
```bash
# Turn LED on
mosquitto_pub -h localhost -t "devices/esp32_01/commands" -m "ON"

# Turn LED off
mosquitto_pub -h localhost -t "devices/esp32_01/commands" -m "OFF"
```

**Document:**
- Command topic used
- LED behavior
- Serial output

**Completion Criteria:**
- ESP32 subscribes to topic
- Commands received and processed
- GPIO controlled by MQTT
- Understand callback mechanism

---

### Lab 9: Reconnection and Fault Handling

**Objective:** Implement robust reconnection logic.

**Prerequisites:**
- Completed Lab 6 and 7

**Components:**
- ESP32 development board
- Mosquitto broker

**Theory:**
- Wi-Fi can disconnect
- MQTT broker can be unavailable
- Reconnection logic required
- State management across reconnections

**Arduino-ESP32 Code:**
```cpp
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";
const char* mqtt_server = "192.168.1.100";

WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastReconnectAttempt = 0;

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  client.setServer(mqtt_server, 1883);
}

void loop() {
  // Check Wi-Fi
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi disconnected, reconnecting...");
    WiFi.reconnect();
  }
  
  // Check MQTT
  if (!client.connected()) {
    unsigned long now = millis();
    if (now - lastReconnectAttempt > 5000) {
      lastReconnectAttempt = now;
      if (reconnect()) {
        lastReconnectAttempt = 0;
      }
    }
  } else {
    client.loop();
  }
}

boolean reconnect() {
  Serial.print("Attempting MQTT connection...");
  if (client.connect("ESP32Client")) {
    Serial.println("connected");
    // Resubscribe here
    return true;
  } else {
    Serial.print("failed, rc=");
    Serial.println(client.state());
    return false;
  }
}
```

**Expected Behavior:**
- ESP32 detects Wi-Fi disconnection
- ESP32 reconnects to Wi-Fi
- ESP32 reconnects to MQTT broker
- Serial monitor shows reconnection attempts

**Test:**
1. Start ESP32
2. Verify connection
3. Disconnect Wi-Fi (turn off router or ESP32)
4. Observe reconnection attempts
5. Reconnect Wi-Fi
6. Verify MQTT reconnection

**Document:**
- Reconnection behavior
- Time to reconnect
- Serial output

**Completion Criteria:**
- Wi-Fi reconnection implemented
- MQTT reconnection implemented
- System recovers from disconnections
- Understand fault handling

---

### Lab 10: Mini IoT System

**Objective:** Build complete IoT monitoring node.

**Prerequisites:**
- Completed Labs 6-9
- Sensor (temperature or potentiometer)
- LED

**Components:**
- ESP32 development board
- Sensor
- LED and resistor
- Mosquitto broker
- MQTT client tool (MQTTX or mosquitto_sub)

**Theory:**
- Combine telemetry publishing and command subscription
- Implement complete IoT node
- Use JSON payloads
- Implement status topic

**Requirements:**
- Wi-Fi connection
- MQTT connection
- Sensor telemetry publishing (JSON payload)
- LED control via command subscription
- Online/offline status (retained)
- Reconnection logic

**Arduino-ESP32 Code:**
```cpp
#include <WiFi.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";
const char* mqtt_server = "192.168.1.100";
const char* device_id = "esp32_monitor_01";

WiFiClient espClient;
PubSubClient client(espClient);
const int ledPin = 2;
unsigned long lastTelemetry = 0;

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  
  if (connectMQTT()) {
    Serial.println("System ready");
  }
}

void loop() {
  if (WiFi.status() != WL_CONNECTED) {
    WiFi.reconnect();
  }
  
  if (!client.connected()) {
    connectMQTT();
  }
  
  client.loop();
  
  // Publish telemetry every 5 seconds
  if (millis() - lastTelemetry > 5000) {
    lastTelemetry = millis();
    publishTelemetry();
  }
}

boolean connectMQTT() {
  if (client.connect(device_id)) {
    client.subscribe("devices/" + String(device_id) + "/commands");
    client.publish("devices/" + String(device_id) + "/status", "online", true);
    Serial.println("MQTT connected");
    return true;
  }
  return false;
}

void publishTelemetry() {
  int sensorValue = analogRead(A0);
  float voltage = sensorValue * (3.3 / 4095.0);
  
  StaticJsonDocument<200> doc;
  doc["device_id"] = device_id;
  doc["value"] = voltage;
  doc["timestamp"] = millis();
  
  char payload[200];
  serializeJson(doc, payload);
  
  client.publish("devices/" + String(device_id) + "/telemetry", payload);
  Serial.println("Telemetry: " + String(payload));
}

void callback(char* topic, byte* payload, unsigned int length) {
  String message = "";
  for (int i = 0; i < length; i++) {
    message += (char)payload[i];
  }
  
  if (message == "ON") {
    digitalWrite(ledPin, HIGH);
  } else if (message == "OFF") {
    digitalWrite(ledPin, LOW);
  }
}
```

**Expected Behavior:**
- ESP32 connects to Wi-Fi and MQTT
- Telemetry published every 5 seconds (JSON)
- LED controlled via commands
- Status published as retained message
- Reconnection on disconnect

**Test:**
```bash
# Subscribe to telemetry
mosquitto_sub -h localhost -t "devices/esp32_monitor_01/telemetry" -v

# Subscribe to status
mosquitto_sub -h localhost -t "devices/esp32_monitor_01/status" -v

# Send command
mosquitto_pub -h localhost -t "devices/esp32_monitor_01/commands" -m "ON"
```

**Document:**
- System architecture
- Topic design
- Payload format
- Test results
- Reconnection behavior

**Completion Criteria:**
- Complete IoT node working
- Telemetry publishing with JSON
- Command subscription working
- Status publishing with retain
- Reconnection logic working
- System robust to disconnections

---

## Projects

### Project: MQTT IoT Monitoring Node

**Objective:** Create a complete IoT monitoring node that publishes telemetry, receives commands, and integrates into an IoT system.

**Requirements:**
- Wi-Fi connection with reconnection logic
- MQTT connection with reconnection logic
- Sensor telemetry publishing (JSON payload)
- Device status publishing (retained)
- Command subscription for actuator control
- Error handling and fault tolerance
- Documentation

**Suggested Architecture:**
```
Sensor
    ↓
ESP32
    ↓
Wi-Fi
    ↓
MQTT Broker
    ↓
    ↓                    ↓
Monitoring Dashboard   Database
```

**Required Features:**
- Connect to Wi-Fi
- Connect to MQTT broker
- Read sensor data
- Publish telemetry with JSON payload
- Publish online/offline status (retained)
- Subscribe to command topic
- Control actuator (LED or relay)
- Implement reconnection logic
- Error handling

**Optional Extensions:**
- QoS 1 for critical messages
- Authentication
- Basic dashboard (MQTTX or web-based)
- Multiple sensors
- Configuration via MQTT

**Deliverables:**
- Working firmware (Arduino-ESP32)
- Circuit documentation
- Code with comments
- Topic design documentation
- Payload format documentation
- Testing documentation
- Reconnection testing results

**Time Estimate:** 8-10 hours

**Project Structure:**
```
mqtt-iot-monitoring-node/
├── README.md
├── circuit/
│   └── wiring.md
├── src/
│   └── main.ino
├── tests/
├── docs/
│   └── architecture.md
└── results/
    └── measurements.md
```

**Note:** This project teaches complete IoT system integration, preparing for advanced IoT architectures and cloud integration in later phases.

---

## Common Mistakes

### Mistake 1: Hardcoding Credentials
**Problem:** MQTT username/password in source code
**Consequence:** Security risk if code is shared
**Solution:** Use environment variables or secure configuration

### Mistake 2: Wrong Topic
**Problem:** Publishing to wrong topic, subscribing to wrong topic
**Consequence:** Messages not received
**Solution:** Double-check topic strings, use consistent naming

### Mistake 3: No Reconnection Logic
**Problem:** ESP32 never reconnects after disconnect
**Consequence:** System becomes permanently offline
**Solution:** Implement reconnection logic for both Wi-Fi and MQTT

### Mistake 4: Not Resubscribing After Reconnect
**Problem:** Subscriptions lost after MQTT reconnect
**Consequence:** Commands not received after reconnection
**Solution:** Resubscribe to topics in reconnection logic

### Mistake 5: Wrong QoS
**Problem:** Using QoS 2 for high-frequency data
**Consequence:** Excessive overhead, poor performance
**Solution:** Choose appropriate QoS for use case

### Mistake 6: No Status Publishing
**Problem:** No way to know if device is online
**Consequence:** Cannot monitor device health
**Solution:** Publish online/offline status with retain flag

### Mistake 7: Malformed JSON
**Problem:** Invalid JSON payload
**Consequence:** Parsing fails on receiver
**Solution:** Use JSON library, validate format

### Mistake 8: Blocking MQTT Loop
**Problem:** Long operations in callback or loop
**Consequence:** MQTT communication stalls
**Solution:** Keep operations short, use non-blocking code

### Mistake 9: Ignoring Callback Return Codes
**Problem:** Not checking connection return codes
**Consequence:** Connection failures go unnoticed
**Solution:** Check and log return codes

### Mistake 10: No Error Handling
**Problem:** No handling of connection failures
**Consequence:** System fails silently
**Solution:** Implement error handling and logging

---

## Troubleshooting

### MQTT Connection Problems
**Problem:** ESP32 cannot connect to MQTT broker
**Solutions:**
- Check broker IP address
- Check broker is running
- Check network connectivity (ping broker)
- Check Wi-Fi connection
- Check port (1883 vs 8883)
- Check firewall settings

### Authentication Problems
**Problem:** Authentication fails
**Solutions:**
- Check username/password
- Check broker configuration
- Check client ID conflicts
- Check ACL settings

### Subscription Problems
**Problem:** Not receiving subscribed messages
**Solutions:**
- Check topic string matches
- Check wildcard syntax
- Check broker logs
- Verify publisher is actually publishing
- Check QoS level mismatch

### Publishing Problems
**Problem:** Messages not reaching broker
**Solutions:**
- Check topic string
- Check connection status
- Check broker logs
- Check network connectivity
- Check payload size limits

### Reconnection Problems
**Problem:** Device does not reconnect
**Solutions:**
- Check reconnection logic is called
- Check Wi-Fi reconnection
- Check broker availability
- Check reconnection delay (not too short)
- Add logging to debug

### JSON Parsing Problems
**Problem:** JSON payload not parsed correctly
**Solutions:**
- Validate JSON format
- Check library usage
- Check buffer size
- Test payload manually
- Use JSON validator

### Retained Message Problems
**Problem:** Stale retained messages
**Solutions:**
- Publish empty message with retain=0 to clear
- Check retain flag usage
- Verify broker behavior

### Wildcard Problems
**Problem:** Wildcards not matching as expected
**Solutions:**
- Check `+` matches exactly one level
- Check `#` is at end of subscription
- Verify topic hierarchy
- Test with simple cases first

---

## Knowledge Test

Answer these questions without looking at the materials:

1. What is the main difference between MQTT and HTTP?
2. What is the role of the MQTT broker?
3. How are publishers and subscribers decoupled in MQTT?
4. What does the `+` wildcard match in MQTT topics?
5. What does the `#` wildcard match in MQTT topics?
6. What is the difference between QoS 0, 1, and 2?
7. When should you use retained messages?
8. What is Last Will and Testament (LWT)?
9. What is the difference between clean session true and false?
10. Why is client ID important in MQTT?
11. What is the difference between port 1883 and 8883?
12. Why should you never hardcode MQTT credentials?
13. What is the difference between authentication and authorization?
14. What is a typical IoT architecture?
15. Why is JSON a good payload format for MQTT?
16. What happens if a new subscriber joins and there is a retained message?
17. What is the purpose of the MQTT callback function?
18. Why is reconnection logic important for MQTT devices?
19. What should you do when an MQTT device reconnects?
20. What is the advantage of publish/subscribe over request/response?

**Passing Score:** 16/20 correct answers

---

## Practical Test

Complete this practical task:

**Build an ESP32 MQTT Monitoring Node:**

**Requirements:**
1. Connect ESP32 to Wi-Fi
2. Connect ESP32 to MQTT broker
3. Read a sensor (temperature or potentiometer)
4. Publish telemetry every 5 seconds with JSON payload including:
   - device_id
   - sensor value
   - timestamp
5. Publish online/offline status (retained)
6. Subscribe to command topic
7. Control an LED based on received commands
8. Implement reconnection logic for both Wi-Fi and MQTT
9. Document:
   - Wiring diagram
   - Topic design
   - Payload format
   - Testing procedure
   - Reconnection testing results

**Testing:**
- Verify telemetry publishing
- Verify status publishing
- Verify command subscription
- Verify LED control
- Test Wi-Fi disconnection and reconnection
- Test MQTT disconnection and reconnection

**Deliverables:**
- Working firmware
- Circuit documentation
- Topic design documentation
- Payload format documentation
- Test results
- Reconnection test results

**Passing Criteria:** All requirements met with documented testing.

---

## Completion Checklist

Before moving to Phase 11, verify you have:

- [ ] Understand MQTT publish/subscribe architecture
- [ ] Understand MQTT control packets and connection lifecycle
- [ ] Can design MQTT topic hierarchies
- [ ] Understand MQTT wildcards
- [ ] Understand QoS levels (0, 1, 2)
- [ ] Understand retained messages
- [ ] Understand Last Will and Testament
- [ ] Understand MQTT sessions and client IDs
- [ ] Can install and configure Mosquitto broker
- [ ] Can use MQTT CLI tools
- [ ] Understand MQTT security fundamentals
- [ ] Can implement ESP32 MQTT connection
- [ ] Can publish telemetry with JSON payload
- [ ] Can subscribe to commands
- [ ] Can implement reconnection logic
- [ ] Understand IoT architecture layers
- [ ] Completed all exercises
- [ ] Completed at least 5 labs
- [ ] Completed the MQTT IoT monitoring node project
- [ ] Passed the knowledge test (16/20 correct)
- [ ] Passed the practical test

---

## Do Not Continue Until...

**Do not start Phase 11 until:**

1. You have passed the knowledge test (16/20 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You understand MQTT publish/subscribe architecture
5. You can implement MQTT on ESP32
6. You have completed at least 5 labs
7. You have completed the MQTT IoT monitoring node project
8. You understand IoT architecture
9. You can design MQTT topics and payloads
10. You can implement reconnection logic

**MQTT is the foundation of IoT communication. Mastering MQTT enables you to build complete IoT systems that scale from single devices to complex distributed architectures.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 11 — Cloud and Edge Integration**

Phase 11 will teach you about cloud platforms, edge computing, data storage, dashboards, and advanced IoT architectures, building on the MQTT foundation you established here.

---

**MQTT enables IoT devices to communicate efficiently and reliably. Understanding MQTT architecture, QoS, security, and implementation is essential for any modern IoT system.**
