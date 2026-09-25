# MQTT Cheat Sheet

Quick reference for MQTT protocol and usage.

## Basic Concepts

### Architecture
```
Publisher ──PUBLISH──► Broker ──PUBLISH──► Subscriber
```

### Key Components
- **Broker**: Routes messages between clients
- **Publisher**: Sends messages to topics
- **Subscriber**: Receives messages from topics
- **Topic**: Hierarchical message routing

## Topic Structure

### Topic Name (Publishing)
```
home/livingroom/temperature
```

### Topic Filter (Subscribing)
```
home/+/temperature    // + matches one level
home/#               // # matches multiple levels
```

## QoS Levels

| QoS | Delivery | Use Case |
|-----|---------|----------|
| 0 | At most once | Non-critical data |
| 1 | At least once | Important data |
| 2 | Exactly once | Critical data |

## Common Patterns

### Telemetry Publishing
```
Topic: iot/devices/esp32-01/telemetry
Payload: {"temp": 24.5, "humidity": 52.1}
QoS: 1
```

### Command Subscription
```
Topic: iot/devices/esp32-01/command
QoS: 1
```

### Online/Offline Pattern
```
Online: Publish retained "online" to status topic
Will: Configure to publish "offline" on disconnect
```

## ESP32 MQTT Basic

### Connect
```c
client.setServer("broker.example.com", 1883);
client.setCallback(callback);
client.connect("esp32-01");
```

### Publish
```c
client.publish("topic", "message");
```

### Subscribe
```c
client.subscribe("topic");
```

## Security

### TLS
- Port 8883 for MQTT over TLS
- Use certificates for authentication
- Never send credentials in plaintext

### Best Practices
- Use unique client IDs
- Implement authentication
- Use topic authorization
- Don't commit credentials to Git

---

*This cheat sheet is a quick reference. For detailed understanding, study Phase 10 - MQTT and IoT.*
