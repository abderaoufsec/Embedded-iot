# MQTT Study Guide — Based on *Mastering MQTT: Your Ultimate Tutorial for MQTT*

> A practical study version of the uploaded book for your Embedded/IoT project. It keeps the important MQTT 3.1.1/5.0 concepts while separating essential knowledge from advanced features.

## 1. MQTT in one picture

```text
ESP32 (publisher)
       |
       | PUBLISH
       v
   MQTT BROKER
       |
       | PUBLISH
       v
Backend / Dashboard (subscriber)
```

MQTT is a lightweight messaging protocol designed for IoT. Its core model is **publish/subscribe**: publishers and subscribers are decoupled, while the broker routes messages. The book identifies four fundamental components: Publisher, Subscriber, Broker and Topic. fileciteturn1file6L1-L8

---

## 2. Broker

The broker:

- accepts client connections
- receives published messages
- matches publications against subscriptions
- forwards matching messages
- handles CONNECT/DISCONNECT
- handles SUBSCRIBE/UNSUBSCRIBE
- maintains session state when configured

The book uses **EMQX** as its broker for demonstrations and **MQTTX** as its MQTT testing client. fileciteturn1file0L1-L6

---

## 3. Client

Any program/device connecting to the broker is an MQTT client:

- ESP32
- Python application
- backend
- mobile app
- MQTTX

One client can both publish and subscribe.

---

## 4. Topics

A topic is the routing name for an MQTT message.

Examples:

```text
home/livingroom/temperature
home/livingroom/humidity
home/bedroom/temperature
```

The book describes topics as UTF-8 strings normally divided into levels with `/`. fileciteturn1file3L1-L5

### Topic name vs topic filter

**Topic name:** used when publishing.

```text
home/bedroom/temperature
```

**Topic filter:** used when subscribing.

```text
home/+/temperature
```

Wildcards are for subscriptions, not publication.

---

# 5. Wildcards

## `+` — one level

```text
sensor/+/temperature
```

Matches:

```text
sensor/1/temperature
sensor/2/temperature
sensor/bedroom/temperature
```

It does not match:

```text
sensor/1/room/temperature
```

because `+` represents exactly one level. fileciteturn1file3L5-L9

## `#` — multiple levels

```text
sensor/#
```

can match multiple levels below `sensor`.

`#` must occupy an entire level and be the final level.

Valid:

```text
sensor/#
```

Invalid:

```text
sensor/#/temperature
sensor/bedroom#
```

fileciteturn1file3L9-L13

---

# 6. Basic MQTT flow

Memorize:

```text
Client → CONNECT → Broker
Client ← CONNACK ← Broker

Client → SUBSCRIBE → Broker
Client ← SUBACK ← Broker

Publisher → PUBLISH → Broker
Subscriber ← PUBLISH ← Broker
```

Important packets:

```text
CONNECT
CONNACK
PUBLISH
SUBSCRIBE
SUBACK
UNSUBSCRIBE
UNSUBACK
PINGREQ
PINGRESP
DISCONNECT
```

MQTT 5.0 also has `AUTH` for enhanced authentication. fileciteturn1file18L1-L8

---

# 7. MQTT over TCP

MQTT commonly operates over TCP.

Typical ports:

```text
1883 → MQTT without TLS
8883 → MQTT over TLS
```

MQTT and TCP are not the same thing:

```text
MQTT = application messaging protocol
TCP  = transport protocol
```

MQTT can also be transported through WebSockets.

---

# 8. Client ID

Every MQTT connection uses a Client ID.

Example:

```text
esp32-01
```

For persistent sessions, the Client ID matters because the broker associates session state with it. Reconnecting with a different/dynamic ID creates a different session. fileciteturn1file5L1-L8

For your ESP32 devices, use a deliberate unique ID such as:

```text
esp32-01
esp32-02
```

---

# 9. Sessions

A session can contain MQTT state such as:

- subscriptions
- undelivered QoS messages
- incomplete QoS exchanges
- Will-related state

## MQTT 3.1.1

Uses:

```text
Clean Session
```

Conceptually:

```text
true  → temporary/new session
false → allow persistent session
```

A persistent session can allow appropriate offline QoS messages to be delivered after reconnecting, subject to broker limits. fileciteturn1file7L1-L8

## MQTT 5.0

MQTT 5.0 replaces Clean Session with:

```text
Clean Start
+
Session Expiry Interval
```

### Clean Start

```text
true  → start a new session
false → attempt to resume the existing session
```

### Session Expiry Interval

Controls how long the session remains after disconnection.

```text
0 → expires on disconnect
N → remains for N seconds
0xFFFFFFFF → maximum protocol interval
```

fileciteturn1file5L8-L16

---

# 10. Retained messages

A retained message is the latest retained message stored by the broker for a topic.

Example:

```text
Topic:   device/01/status
Payload: online
Retain:  true
```

A new subscriber can receive that latest state when subscribing.

This is especially useful for state:

```text
device/01/status
device/01/mode
device/01/config
```

Retained messages are separate from session state, so ending a session does not automatically delete them. fileciteturn1file7L8-L9

### Clearing retained state

The usual pattern is publishing an empty payload with the Retain flag set for the same topic.

---

# 11. QoS

MQTT has three QoS levels.

## QoS 0

**At most once**

```text
send
→ done
```

No MQTT retransmission mechanism for the application message.

Possible loss.

## QoS 1

**At least once**

Uses acknowledgment/retransmission.

Possible duplicate delivery.

## QoS 2

**Exactly once**

Uses a more extensive exchange to avoid duplicate application delivery.

More overhead.

fileciteturn1file16L1-L6

### Mental model

```text
QoS 0 → lowest overhead / loss possible
QoS 1 → acknowledged / duplicates possible
QoS 2 → strongest delivery semantics / highest overhead
```

Do not simply think:

> QoS 2 is always better.

Choose based on application requirements.

---

# 12. Critical QoS point

QoS does **not** mean:

> "The application on the subscriber successfully executed my command."

It concerns MQTT message delivery semantics.

If a controller needs confirmation that a device actually executed a command, use an application-level response pattern.

The book explicitly makes this distinction and introduces Request/Response for it. fileciteturn1file13L1-L8

---

# 13. QoS during subscription

A subscription specifies a maximum QoS for delivery.

The book summarizes the relationship as:

```text
Granted subscription QoS
= min(server maximum QoS,
      client's requested maximum QoS)

Forwarded QoS
= min(original publication QoS,
      granted subscription QoS)
```

fileciteturn1file15L1-L8

---

# 14. Keep Alive

Keep Alive helps detect broken or half-open connections.

The client supplies Keep Alive in CONNECT.

When otherwise idle, it can send:

```text
PINGREQ
```

and the broker responds:

```text
PINGRESP
```

The broker can consider the client disconnected when it receives no MQTT packet for **1.5 × Keep Alive**. fileciteturn0file0L1-L5

Example:

```text
Keep Alive = 60 s
1.5 × 60 = 90 s
```

---

# 15. Will Message

A Will Message is configured during connection.

If the client disappears abnormally, the broker publishes the Will.

Example:

```text
Will topic:
iot/devices/esp32-01/status

Will payload:
offline

Retain:
true
```

The book describes unexpected network failure, loss of contact during Keep Alive handling, and abnormal connection closure as situations associated with Will publication. fileciteturn0file0L1-L8

A normal MQTT `DISCONNECT` does not normally trigger the Will. fileciteturn1file4L1-L4

---

# 16. Recommended online/offline pattern

On successful connection:

```text
publish retained:
iot/devices/esp32-01/status = online
```

Configure Will:

```text
topic:
iot/devices/esp32-01/status

payload:
offline

retain:
true
```

Architecture:

```text
ESP32 connects
      ↓
online retained state

ESP32 unexpectedly disappears
      ↓
broker detects failure
      ↓
Will
      ↓
offline retained state
```

The book demonstrates combining retained state with the Will mechanism. fileciteturn1file4L1-L7

---

# 17. Security

Do not treat MQTT username/password as the complete security design.

The book explains that plaintext MQTT is insufficient for protecting communication and discusses TLS. fileciteturn1file5L14-L16

Think in layers:

```text
TLS
+
Authentication
+
Authorization / ACL
+
Secure credentials
+
Unique client identity
```

### Authentication

> Who are you?

### Authorization

> What are you allowed to do?

Example:

```text
esp32-01

CAN publish:
iot/devices/esp32-01/telemetry

CAN subscribe:
iot/devices/esp32-01/command

CANNOT publish:
iot/devices/esp32-02/telemetry
```

---

# 18. Request / Response — MQTT 5.0

Normal MQTT is asynchronous:

```text
Requester
   ↓ command
Device
```

If the requester needs a result:

```text
Requester
   ↓ command
Device
   ↓ result
Requester
```

MQTT 5.0 standardizes this using:

- Response Topic
- Correlation Data
- Response Information

fileciteturn1file13L1-L8

## Response Topic

Example:

```text
Request:
iot/devices/esp32-01/command

Response:
client/backend-01/response
```

Subscribe to the response topic **before** sending the request. fileciteturn1file13L1-L8

## Correlation Data

Allows the requester to associate a response with the original request when multiple requests/responses exist.

The responder returns the correlation data intact. fileciteturn1file13L1-L8

---

# 19. MQTT 5.0 properties

Know these by name and purpose:

```text
Response Topic
Correlation Data
Response Information
User Properties
Topic Alias
Payload Format Indicator
Content Type
Message Expiry Interval
Subscription Identifier
Maximum Packet Size
Reason Codes
Server Keep Alive
Session Expiry Interval
```

Do not spend days memorizing packet encodings.

---

# 20. User Properties

User Properties let applications attach custom metadata to MQTT messages.

Concept:

```text
message
+
application metadata
```

Example:

```text
source = esp32-01
version = 1.0
```

---

# 21. Topic Alias

Topic Alias allows MQTT 5.0 clients to reduce repeated transmission of long topic names.

Useful when bandwidth efficiency matters.

Not necessary for your first ESP32 project.

---

# 22. Payload Format / Content Type

MQTT 5.0 can describe the payload format/content type.

Example:

```text
Content Type:
application/json
```

This does not automatically validate the JSON. Your application still has to parse and validate it.

---

# 23. Message Expiry

MQTT 5.0 allows a message to have an expiry interval.

Useful when stale data has no value.

Example:

```text
temporary event
expiry = 10 seconds
```

---

# 24. Shared subscriptions

Shared subscriptions distribute messages among members of a shared group.

Format:

```text
$share/{ShareName}/{TopicFilter}
```

Example:

```text
$share/workers/sensor/+
```

Useful for:

- scaling backend consumers
- load balancing
- high availability

fileciteturn1file11L1-L8

This is generally a backend/scaling feature, not something you need for your first ESP32 node.

---

# 25. Subscription options

MQTT 5.0 provides:

```text
QoS
No Local
Retain As Published
Retain Handling
```

fileciteturn1file17L1-L8

For your first implementation, understand QoS. Learn the others when required.

---

# 26. No Local

When enabled, the broker does not forward the client's own publication back to that client through that subscription.

It is particularly useful in some bridge architectures. fileciteturn1file15L4-L8

---

# 27. Retain As Published

Controls whether the Retain flag is preserved when forwarding messages.

It is especially relevant to broker bridging. fileciteturn1file15L4-L8

---

# 28. Retain Handling

Controls retained-message delivery when a subscription is created:

```text
0 → send retained messages when subscription is established
1 → send only for a new subscription
2 → do not send retained messages when subscription is established
```

fileciteturn1file12L1-L8

---

# 29. Advanced features to postpone

Understand their purpose, but don't spend study time mastering them yet:

- Subscription Identifier
- Shared Subscriptions
- User Properties
- Topic Alias
- Payload Format Indicator
- Content Type
- Message Expiry
- Maximum Packet Size
- Enhanced Authentication
- detailed packet binary encoding

These are later-stage MQTT 5.0 topics in the uploaded book. fileciteturn1file2L1-L9

---

# 30. MQTTX practical labs

The book uses MQTTX for demonstrations. fileciteturn1file0L1-L6

## Lab 1 — Publish/Subscribe

Create:

```text
Client A = publisher
Client B = subscriber
```

B subscribes:

```text
lab/test
```

A publishes:

```text
hello mqtt
```

Verify B receives it.

---

## Lab 2 — Wildcards

Publish:

```text
sensor/1/temperature
sensor/2/temperature
sensor/3/temperature
```

Subscribe:

```text
sensor/+/temperature
```

Then:

```text
sensor/#
```

Observe the difference.

---

## Lab 3 — QoS

Test:

```text
QoS 0
QoS 1
QoS 2
```

Be able to explain the delivery semantics rather than merely observing a successful message.

---

## Lab 4 — Retained message

Publish:

```text
topic: lab/status
payload: online
retain: true
```

Disconnect.

Create a new subscriber and subscribe to:

```text
lab/status
```

Observe the retained state.

---

## Lab 5 — Session

Use MQTT 5.0:

```text
Client ID: lab-client
Clean Start: false
Session Expiry: non-zero
```

Create a subscription with suitable QoS.

Disconnect.

Publish while the client is offline.

Reconnect using the same Client ID/session arrangement and observe session recovery, subject to broker limits. fileciteturn1file9L1-L8

---

## Lab 6 — Keep Alive

Use a short Keep Alive.

Observe:

```text
PINGREQ
PINGRESP
```

Then interrupt connectivity and observe failure detection.

---

## Lab 7 — Will

Configure:

```text
Will topic:
lab/device/status

Will payload:
offline
```

Subscribe with another client.

Connect the first client, then simulate an abnormal disconnect.

Observe the Will.

---

## Lab 8 — Request/Response

Use:

```text
request:
device/01/command

response:
client/01/response
```

Flow:

```text
subscribe response
        ↓
publish command
        ↓
device receives command
        ↓
device publishes result
```

---

# 31. Move to ESP32

Now replace the MQTTX publisher with your ESP32.

Architecture:

```text
ESP32
  │
  │ Wi-Fi
  ↓
MQTT Broker
  │
  ↓
MQTTX / Backend
```

ESP32 publishes:

```text
iot/devices/esp32-01/telemetry
```

MQTTX subscribes.

---

# 32. Bidirectional ESP32 MQTT

Add commands.

```text
ESP32 → telemetry
MQTTX/backend → command
```

Example command:

```json
{
  "command": "set_led",
  "state": true
}
```

ESP32:

```text
receive
 ↓
validate
 ↓
execute
 ↓
optional response
```

---

# 33. Recommended topic architecture

For your project:

```text
iot/
└── devices/
    └── esp32-01/
        ├── telemetry
        ├── status
        ├── command
        └── response
```

Therefore:

```text
iot/devices/esp32-01/telemetry
iot/devices/esp32-01/status
iot/devices/esp32-01/command
iot/devices/esp32-01/response
```

This is a project convention, not an MQTT requirement.

---

# 34. Recommended telemetry payload

Start with:

```json
{
  "device_id": "esp32-01",
  "temperature": 24.5,
  "humidity": 52.1,
  "uptime": 12345
}
```

Later:

```json
{
  "device_id": "esp32-01",
  "timestamp": "...",
  "temperature": 24.5,
  "humidity": 52.1,
  "light": 430,
  "firmware": "1.0.0"
}
```

Keep payloads appropriate to the application.

---

# 35. ESP32 MQTT state machine

Your firmware should conceptually do:

```text
BOOT
 ↓
Initialize hardware
 ↓
Connect Wi-Fi
 ↓
Connect MQTT
 ↓
Subscribe to commands
 ↓
Publish retained ONLINE
 ↓
┌─────────────────────────────┐
│ Read sensors                │
│ Validate readings           │
│ Publish telemetry           │
│ Process commands            │
│ Monitor Wi-Fi               │
│ Monitor MQTT                │
│ Reconnect when necessary    │
└─────────────────────────────┘
```

Avoid long blocking delays.

---

# 36. MQTT security for your project

Your final system should aim for:

```text
ESP32
  │
  │ TLS
  ↓
MQTT Broker
```

with:

```text
authentication
+
topic authorization/ACL
```

Never commit:

```text
Wi-Fi passwords
MQTT passwords
API keys
certificates/private keys
tokens
```

to GitHub.

---

# 37. Troubleshooting

## ESP32 cannot connect

Check in this order:

```text
1. Wi-Fi connected?
2. IP address assigned?
3. Broker reachable?
4. Broker running?
5. Correct hostname/IP?
6. Correct port?
7. TLS required?
8. Credentials correct?
9. Client ID issue?
10. Broker authentication/ACL logs?
```

## Publisher works but subscriber gets nothing

Check:

```text
1. Topic name
2. Topic filter
3. Subscriber connection
4. SUBACK/result
5. ACL
6. QoS
7. Retained-message expectations
```

## ESP32 keeps disconnecting

Check:

```text
1. Wi-Fi signal
2. Power stability
3. Keep Alive
4. Broker logs
5. MQTT client errors
6. Memory
7. Blocking code
8. Reconnect logic
```

---

# 38. Final MQTT project

## ESP32 MQTT IoT Node

Hardware:

```text
ESP32
+
temperature/humidity sensor
+
LED
+
button
```

### Publish

```text
iot/devices/esp32-01/telemetry
iot/devices/esp32-01/status
```

### Subscribe

```text
iot/devices/esp32-01/command
```

### On boot

```text
initialize
 ↓
Wi-Fi
 ↓
MQTT
 ↓
publish retained ONLINE
```

### During operation

```text
read sensor
 ↓
validate
 ↓
publish telemetry
```

### Command

```text
receive
 ↓
validate
 ↓
execute
 ↓
response if needed
```

### Unexpected failure

```text
connection disappears
 ↓
broker detects failure
 ↓
Will = offline
```

---

# 39. What you MUST know before leaving MQTT

Be able to explain without notes:

### Architecture

```text
Client
Broker
Publisher
Subscriber
Topic
```

### Topics

```text
topic name
topic filter
+
#
```

### Connection

```text
CONNECT
CONNACK
DISCONNECT
```

### Messaging

```text
PUBLISH
SUBSCRIBE
SUBACK
UNSUBSCRIBE
UNSUBACK
```

### Reliability/state

```text
QoS 0/1/2
Retained Message
Session
Clean Start
Session Expiry
Keep Alive
Will Message
```

### Security

```text
TLS
Authentication
Authorization
ACL
```

### MQTT 5.0 application pattern

```text
Response Topic
Correlation Data
Request/Response
```

---

# 40. Final knowledge test

Answer these without looking:

1. What problem does MQTT solve?
2. What does the broker do?
3. Publisher vs subscriber?
4. Topic vs topic filter?
5. What does `+` mean?
6. What does `#` mean?
7. Can you publish using a wildcard?
8. QoS 0?
9. QoS 1?
10. QoS 2?
11. Can QoS 1 produce duplicates?
12. Does QoS mean the subscriber's application executed the command?
13. What is a retained message?
14. What is a session?
15. Clean Start vs Session Expiry?
16. Why does persistent session recovery depend on Client ID?
17. What is Keep Alive?
18. PINGREQ/PINGRESP?
19. What is a Will?
20. Normal vs abnormal disconnect?
21. TLS vs authentication?
22. Authentication vs authorization?
23. What is Request/Response?
24. Response Topic?
25. Correlation Data?
26. What are shared subscriptions?
27. What is one practical use of Message Expiry?
28. What is MQTT 5.0?
29. Which MQTT features will your ESP32 actually use?
30. How will your ESP32 recover after Wi-Fi/MQTT loss?

If you cannot answer several of these, revisit the corresponding section before continuing.

---

# 41. Your exact study order

Do not study the book randomly.

```text
PHASE A — CORE
1. MQTT concept
2. Broker
3. Client
4. Publish/Subscribe
5. Topics
6. Wildcards
7. CONNECT/CONNACK

        ↓

PHASE B — RELIABILITY
8. QoS
9. Retained messages
10. Sessions
11. Clean Start
12. Session Expiry
13. Keep Alive
14. Will Message

        ↓

PHASE C — SECURITY
15. TLS
16. Authentication
17. Authorization / ACL

        ↓

PHASE D — APPLICATION
18. Request/Response
19. Response Topic
20. Correlation Data

        ↓

PHASE E — ADVANCED MQTT 5.0
21. User Properties
22. Topic Alias
23. Payload Format / Content Type
24. Message Expiry
25. Shared Subscriptions
26. Subscription Options
27. Subscription Identifier
28. Reason Codes
29. Maximum Packet Size
30. Enhanced Authentication

        ↓

PHASE F — ESP32
31. MQTTX labs
32. ESP32 publisher
33. ESP32 subscriber
34. telemetry
35. commands
36. reconnect
37. Will/status
38. TLS/authentication/ACL
39. final IoT node
```

---

# 42. The one architecture to remember

```text
                    MQTT BROKER
                   /     |                        /      |                        ↓       ↓        ↓
              ESP32    Backend   Dashboard
                │
                │ PUBLISH
                ↓
     iot/devices/esp32-01/telemetry

              ESP32
                ↑
                │ SUBSCRIBE
                │
     iot/devices/esp32-01/command
```

Once you can build this reliably—with intentional QoS, retained status, Keep Alive, Will handling, reconnect logic and basic security—you have the MQTT foundation required for your Embedded IoT work.

---

## Source note

This guide is based on the uploaded *Mastering MQTT — Your Ultimate Tutorial for MQTT* and its chapter structure, including MQTT fundamentals, sessions, QoS, Keep Alive, Will Message, Request/Response and MQTT 5.0 advanced features. fileciteturn1file2L1-L9
