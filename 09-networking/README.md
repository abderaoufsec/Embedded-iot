# Phase 9 — Networking

> **Goal:** Develop practical expertise in networking fundamentals for embedded systems, including TCP/IP, Ethernet, Wi-Fi, and network troubleshooting—preparing for IoT implementation.
>
> **Prerequisite:** Phase 6 — ESP32, Phase 8 — Embedded Communication
>
> **Outcome:** You can implement networked embedded systems, understand TCP/IP protocols, configure network parameters, and troubleshoot network problems.

---

## What You Will Learn

By completing this phase, you will understand:

- **Networking Fundamentals:** Hosts, nodes, clients, servers, topology, packets, addressing, ports
- **OSI and TCP/IP Models:** Conceptual layers, encapsulation, real protocol mapping
- **Ethernet:** MAC addresses, frames, switches, ARP, basic troubleshooting
- **IP Addressing:** IPv4, subnet masks, CIDR, subnetting, private ranges, gateways
- **IPv6:** Address format, compression, link-local, global unicast
- **ARP:** IP-to-MAC resolution, ARP cache, troubleshooting
- **ICMP:** Ping, echo request/reply, TTL, traceroute
- **TCP:** Ports, sockets, connection-oriented, handshake, reliability
- **UDP:** Connectionless, datagrams, overhead, use cases
- **DHCP:** Dynamic addressing, DORA process, IP assignment
- **DNS:** Hostname resolution, queries, caching
- **Wi-Fi for Embedded:** Station mode, AP mode, DHCP, reconnection
- **Sockets:** IP + port, TCP/UDP sockets, client/server model
- **Network Troubleshooting:** Systematic workflow, tools (ping, traceroute, nslookup)
- **Packet Inspection:** Wireshark basics

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
- ✅ Understanding of UART from Phase 6 and 8
- ✅ Understanding of Wi-Fi from Phase 6
- ✅ Understanding of binary and hexadecimal from Phase 1

**Hardware required for labs:**
- ESP32 development board
- PC with network connectivity
- Router or Wi-Fi access point
- USB cable for ESP32 programming

**Software required:**
- Serial terminal software
- Network tools (ping, traceroute, nslookup, ipconfig/ip)
- Wireshark (optional but recommended)

---

## Learning Outcomes

After completing this phase, you will be able to:

- Explain networking fundamentals and terminology
- Understand OSI and TCP/IP models
- Calculate IPv4 subnets
- Understand IPv6 addressing basics
- Use ARP, ICMP, DHCP, DNS protocols
- Implement TCP client/server communication
- Implement UDP communication
- Configure ESP32 Wi-Fi networking
- Implement sockets on ESP32
- Troubleshoot network problems systematically
- Use network diagnostic tools
- Inspect packets with Wireshark
- Design networked embedded systems

---

## Concepts

### Networking Fundamentals

**Network:**
- Collection of connected devices
- Enables communication and resource sharing
- Can be local (LAN) or wide (WAN)

**Host:**
- Computer or device on a network
- Has a network interface
- Identified by IP address

**Node:**
- Generic term for any device on a network
- Can be host, router, switch, etc.

**Client:**
- Device that requests services
- Initiates communication
- Examples: Web browser, email client

**Server:**
- Device that provides services
- Responds to client requests
- Examples: Web server, email server

**Peer-to-Peer:**
- Devices act as both client and server
- No central server
- Examples: File sharing, some messaging

**LAN (Local Area Network):**
- Network covering small geographic area
- Typical: Home, office, building
- High speed, low latency

**WAN (Wide Area Network):**
- Network covering large geographic area
- Typical: Internet, corporate network
- Lower speed, higher latency

**Topology:**
- Physical arrangement of network
- Examples: Star, bus, ring, mesh
- Affects reliability and performance

**Packets:**
- Units of data transmitted over network
- Include header and payload
- Routed independently

**Frames:**
- Layer 2 (data link) units
- Include MAC addresses
- Encapsulated in packets

**Addressing:**
- Mechanism to identify devices
- MAC address (layer 2)
- IP address (layer 3)
- Port number (layer 4)

**Ports:**
- Identify specific application/service
- 16-bit number (0-65535)
- Examples: 80 (HTTP), 443 (HTTPS), 22 (SSH)

**Protocols:**
- Rules for communication
- Define format, timing, error handling
- Examples: TCP, UDP, HTTP, DNS

**Why this matters:** Networking is the foundation of IoT and modern embedded systems. Understanding these fundamentals is essential for networked device development.

---

### OSI and TCP/IP Models

**OSI Model (Conceptual):**
- 7 layers for understanding network functions
- Reference model, not strictly implemented
- Layers: Physical, Data Link, Network, Transport, Session, Presentation, Application

**TCP/IP Model (Practical):**
- 4 layers used in real networks
- Layers: Link, Internet, Transport, Application

**Layer Mapping:**

| OSI Layer | TCP/IP Layer | Example Protocols |
|-----------|--------------|-------------------|
| Application | Application | HTTP, DNS, SMTP |
| Presentation | Application | TLS/SSL, JPEG |
| Session | Application | TCP session setup |
| Transport | Transport | TCP, UDP |
| Network | Internet | IP, ICMP |
| Data Link | Link | Ethernet, Wi-Fi |
| Physical | Link | Cables, radio |

**Encapsulation:**
- Data wrapped with headers at each layer
- Example: HTTP → TCP → IP → Ethernet → Physical

**Decapsulation:**
- Headers removed at each layer
- Data extracted and passed up

**Why this matters:** Understanding layers helps in debugging. A problem at one layer (e.g., IP) manifests at higher layers (e.g., HTTP).

---

### Ethernet

**Ethernet:**
- Most common LAN technology
- Layer 2 (data link) protocol
- Uses MAC addresses

**Ethernet Frame:**
```
[Preamble] [Destination MAC] [Source MAC] [Type] [Payload] [FCS]
```

**MAC Address:**
- 48-bit unique identifier
- Burned into network interface
- Format: XX:XX:XX:XX:XX:XX (hexadecimal)
- Example: 00:11:22:33:44:55

**Switches:**
- Connect devices in LAN
- Forward frames based on MAC address
- Learn MAC addresses from traffic
- Reduce collisions compared to hubs

**Broadcast:**
- Frame sent to all devices
- Destination MAC: FF:FF:FF:FF:FF:FF
- Used for ARP, DHCP discovery

**Unicast:**
- Frame sent to specific device
- Destination MAC: specific MAC address
- Most common communication

**Multicast:**
- Frame sent to group of devices
- Destination MAC: 01:00:5E:XX:XX:XX
- Used for streaming, group communication

**Collision Domain:**
- Network segment where collisions can occur
- Switches reduce collision domains
- Each switch port is separate collision domain

**ARP (Address Resolution Protocol):**
- Maps IP address to MAC address
- Broadcast: "Who has IP X.X.X.X?"
- Response: "I have IP X.X.X.X, my MAC is YY:YY:YY:YY:YY:YY"
- Caches results in ARP table

**Ethernet Cabling:**
- Twisted pair (most common)
- Categories: Cat5, Cat5e, Cat6, Cat6a
- Max length: 100 meters for copper

**Link Negotiation:**
- Devices negotiate speed and duplex
- Auto-negotiation: 10/100/1000 Mbps
- Mismatch can cause errors

**Basic Troubleshooting:**
- Check link lights
- Check cable connectivity
- Check speed/duplex mismatch
- Check MAC address conflicts

**Why this matters:** Ethernet is the foundation of most LANs. Understanding MAC addresses, switches, and ARP is essential for network troubleshooting.

---

### IP Addressing

**IPv4 Address:**
- 32-bit address
- Dotted decimal: X.X.X.X
- Each octet: 0-255
- Example: 192.168.1.1

**Subnet Mask:**
- Defines network portion vs host portion
- Dotted decimal: X.X.X.X
- Binary: 1s for network, 0s for host
- Example: 255.255.255.0

**CIDR (Classless Inter-Domain Routing):**
- Notation: IP/Prefix
- Prefix: number of network bits
- Example: 192.168.1.0/24

**Network Address:**
- All host bits = 0
- Identifies the network
- Example: 192.168.1.0/24

**Host Address:**
- Specific device on network
- Can vary within subnet
- Example: 192.168.1.100

**Broadcast Address:**
- All host bits = 1
- Used to send to all hosts on network
- Example: 192.168.1.255/24

**Default Gateway:**
- Router that connects to other networks
- Used for traffic outside local subnet
- Example: 192.168.1.1

**Private IPv4 Ranges:**
- 10.0.0.0/8 (10.0.0.0 - 10.255.255.255)
- 172.16.0.0/12 (172.16.0.0 - 172.31.255.255)
- 192.168.0.0/16 (192.168.0.0 - 192.168.255.255)
- Not routable on internet
- Used for internal networks

**Public IPv4:**
- Routable on internet
- Unique globally
- Assigned by ISP

**Loopback:**
- 127.0.0.1
- Refers to local device
- Used for testing

**APIPA (Automatic Private IP Addressing):**
- 169.254.0.0/16
- Assigned when DHCP fails
- Link-local communication only

**Subnetting:**
- Dividing network into smaller subnets
- Improves efficiency and security
- Requires calculating network, broadcast, host range

**Subnetting Example:**
- Network: 192.168.1.0/24
- Subnet mask: 255.255.255.0
- Network address: 192.168.1.0
- Broadcast address: 192.168.1.255
- Usable hosts: 192.168.1.1 - 192.168.1.254 (254 hosts)

**Subnetting Calculation:**
- Network address: IP AND subnet mask
- Broadcast address: Network address + (~subnet mask)
- Usable hosts: 2^(32 - prefix) - 2

**Why this matters:** IP addressing is fundamental to networking. Understanding subnetting is essential for network design and troubleshooting.

---

### IPv6

**Why IPv6:**
- IPv4 address exhaustion
- 32-bit IPv4 = ~4.3 billion addresses
- 128-bit IPv6 = ~3.4 × 10^38 addresses

**IPv6 Address Format:**
- 128-bit address
- Hexadecimal groups: XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX
- Example: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

**Compression Rules:**
- Leading zeros in each group can be omitted
- Example: 2001:db8:85a3:0:0:8a2e:370:7334
- One consecutive sequence of zero groups can be replaced with ::
- Example: 2001:db8:85a3::8a2e:370:7334

**Prefix:**
- Network portion of address
- Notation: /prefix
- Example: 2001:db8::/32

**Link-Local Addresses:**
- fe80::/10
- Automatically assigned on each interface
- Only valid on local link
- Similar to IPv4 APIPA

**Global Unicast:**
- Routable on internet
- Unique globally
- Assigned by ISP or RIR

**Loopback:**
- ::1
- Equivalent to 127.0.0.1 in IPv4

**Neighbor Discovery:**
- Similar to ARP
- Maps IPv6 to MAC address
- Uses ICMPv6

**Why this matters:** IPv6 is the future of networking. Understanding IPv6 basics is increasingly important for networked devices.

---

### ARP

**ARP (Address Resolution Protocol):**
- Maps IP address to MAC address
- Layer 2 protocol
- Used in IPv4 networks

**ARP Request:**
- Broadcast: "Who has IP X.X.X.X? Tell MAC.YY.YY.YY.YY.YY"
- Sent to MAC: FF:FF:FF:FF:FF:FF

**ARP Reply:**
- Unicast: "I have IP X.X.X.X, my MAC is ZZ:ZZ:ZZ:ZZ:ZZ:ZZ"
- Sent to requester's MAC

**ARP Cache:**
- Stores IP-to-MAC mappings
- Timeout: typically minutes
- View with: arp -a (Windows), ip neigh (Linux)

**ARP Example:**
```
Device A (IP: 192.168.1.1, MAC: AA:AA:AA:AA:AA:AA)
Device B (IP: 192.168.1.2, MAC: BB:BB:BB:BB:BB:BB)

A wants to send to B:
1. A checks ARP cache for 192.168.1.2
2. Not found, A sends ARP request (broadcast)
3. B receives request, sees it's for its IP
4. B sends ARP reply to A
5. A adds B's IP-MAC to cache
6. A can now send frames to B
```

**ARP Troubleshooting:**
- Wrong MAC in cache: Clear cache
- No response: Device not on network
- Duplicate IP: ARP conflict

**Why this matters:** ARP is essential for IP communication. Understanding ARP helps diagnose connectivity problems.

---

### ICMP

**ICMP (Internet Control Message Protocol):**
- Used for error reporting and diagnostics
- Layer 3 protocol
- Encapsulated in IP packets

**Ping:**
- Uses ICMP Echo Request
- Device responds with Echo Reply
- Tests connectivity and latency

**Echo Request:**
- Type 8
- Sent to destination IP
- Includes sequence number and timestamp

**Echo Reply:**
- Type 0
- Sent in response to Echo Request
- Includes same sequence number and timestamp

**TTL (Time To Live):**
- Limits packet lifetime
- Decremented by each router
- Prevents routing loops
- When TTL = 0, packet discarded

**ICMP Error Messages:**
- Destination Unreachable
- Time Exceeded
- Redirect
- Parameter Problem

**Traceroute/Tracert:**
- Uses ICMP Time Exceeded
- Sends packets with increasing TTL
- Each router responds when TTL expires
- Shows path to destination

**ICMP Examples:**
```
Ping 192.168.1.1:
Pinging 192.168.1.1 with 32 bytes of data:
Reply from 192.168.1.1: bytes=32 time=1ms TTL=64
Reply from 192.168.1.1: bytes=32 time=1ms TTL=64

Traceroute google.com:
1  1 ms  1 ms  1 ms  192.168.1.1
2  10 ms 10 ms 10 ms  10.0.0.1
3  15 ms 15 ms 15 ms  142.250.80.1
```

**ICMP Troubleshooting:**
- No ping response: Device down, firewall blocking, routing issue
- High latency: Network congestion, long path
- Time Exceeded: Routing loop, TTL too low

**Why this matters:** ICMP is essential for network diagnostics. Ping and traceroute are fundamental troubleshooting tools.

---

### TCP

**TCP (Transmission Control Protocol):**
- Connection-oriented protocol
- Reliable data delivery
- Layer 4 protocol
- Port-based

**TCP Characteristics:**
- Connection-oriented: 3-way handshake
- Reliable: Acknowledgments, retransmission
- Ordered: Sequencing
- Flow control: Window size
- Congestion control: Adjusts rate

**TCP Ports:**
- 16-bit number (0-65535)
- Well-known ports: 0-1023
- Registered ports: 1024-49151
- Dynamic/private ports: 49152-65535
- Examples: 80 (HTTP), 443 (HTTPS), 22 (SSH)

**Sockets:**
- IP address + port = socket
- Endpoint for communication
- Example: 192.168.1.100:8080

**Three-Way Handshake:**
```
Client                    Server
  |  SYN                  |
  |--------------------->  |
  |        SYN+ACK        |
  |<---------------------|
  |          ACK          |
  |--------------------->  |
  |     ESTABLISHED       |
```

**SYN:** Synchronize sequence numbers
**ACK:** Acknowledge received
**SYN+ACK:** Synchronize and acknowledge

**TCP Segment:**
```
[Source Port] [Dest Port] [Sequence Number] [Ack Number] [Flags] [Window] [Checksum] [Urgent] [Data]
```

**Sequence Numbers:**
- Byte stream numbering
- Enables reassembly
- Enables duplicate detection

**Acknowledgments:**
- Confirm receipt of data
- Include next expected sequence number
- Trigger retransmission if lost

**Retransmission:**
- Lost segments resent
- Based on ACKs and timeouts
- Ensures reliability

**Flow Control:**
- Receiver advertises window size
- Sender limits data to window
- Prevents overwhelming receiver

**Connection Termination:**
```
Client                    Server
  |  FIN                  |
  |--------------------->  |
  |          ACK          |
  |<---------------------|
  |          FIN          |
  |<---------------------|
  |  ACK                  |
  |--------------------->  |
  |     CLOSED            |
```

**TCP vs UDP Use Cases:**
- **TCP:** Web (HTTP), email (SMTP), file transfer (FTP)
- **UDP:** Streaming, VoIP, DNS queries, real-time data

**Why this matters:** TCP is the backbone of most internet communication. Understanding TCP is essential for reliable networked applications.

---

### UDP

**UDP (User Datagram Protocol):**
- Connectionless protocol
- Unreliable data delivery
- Layer 4 protocol
- Port-based

**UDP Characteristics:**
- Connectionless: No handshake
- Unreliable: No acknowledgments, no retransmission
- Low overhead: Small header
- Fast: No connection setup
- Ordered: Not guaranteed

**UDP Datagram:**
```
[Source Port] [Dest Port] [Length] [Checksum] [Data]
```

**UDP Ports:**
- Same port space as TCP
- Independent from TCP
- Examples: 53 (DNS), 67 (DHCP server), 68 (DHCP client)

**UDP Advantages:**
- Low latency
- Low overhead
- Simple
- Multicast/broadcast support

**UDP Disadvantages:**
- No reliability
- No ordering
- No congestion control
- No flow control

**Embedded Use Cases:**
- Sensor data streaming
- Real-time control
- Discovery protocols
- DNS queries
- DHCP

**TCP vs UDP Comparison:**

| Characteristic | TCP | UDP |
|---------------|-----|-----|
| Connection | Connection-oriented | Connectionless |
| Reliability | Reliable | Unreliable |
| Ordering | Guaranteed | Not guaranteed |
| Overhead | Higher | Lower |
| Latency | Higher | Lower |
| Flow Control | Yes | No |
| Congestion Control | Yes | No |
| Use Cases | Web, email, file transfer | Streaming, VoIP, DNS |

**Why this matters:** UDP is essential for real-time and low-latency applications. Understanding when to use TCP vs UDP is critical for embedded systems.

---

### DHCP

**DHCP (Dynamic Host Configuration Protocol):**
- Automatically assigns IP addresses
- Reduces manual configuration
- Layer 7 application protocol
- Uses UDP ports 67 (server) and 68 (client)

**DHCP Process (DORA):**
```
Client                    DHCP Server
  |  DISCOVER (broadcast) |
  |--------------------->  |
  |       OFFER           |
  |<---------------------|
  |      REQUEST          |
  |--------------------->  |
  |       ACK             |
  |<---------------------|
```

**DISCOVER:**
- Client broadcasts: "I need an IP"
- Destination: 255.255.255.255
- Source: 0.0.0.0

**OFFER:**
- Server responds: "I can offer IP X.X.X.X"
- Includes: IP, subnet mask, lease time
- May include: gateway, DNS

**REQUEST:**
- Client requests specific IP
- Broadcast or unicast to server

**ACK:**
- Server confirms assignment
- Includes all configuration
- Client now has IP

**DHCP Lease:**
- IP assigned for specific time
- Typical: 24 hours
- Client must renew before expiration
- Renewal: REQUEST → ACK (simplified)

**DHCP Options:**
- Subnet mask
- Default gateway
- DNS servers
- Domain name
- Lease time
- And many more

**ESP32 Wi-Fi with DHCP:**
```cpp
WiFi.begin("SSID", "password");
// DHCP automatically assigns IP
Serial.println(WiFi.localIP());
```

**Static IP:**
- Manual IP assignment
- Useful for servers
- No DHCP required

**DHCP Troubleshooting:**
- No IP: DHCP server down, no network
- Wrong IP: Wrong DHCP server
- Lease expired: Renewal failed

**Why this matters:** DHCP simplifies network configuration. Understanding DHCP is essential for embedded device deployment.

---

### DNS

**DNS (Domain Name System):**
- Maps hostnames to IP addresses
- Distributed database
- Hierarchical structure

**Hostname:**
- Human-readable name
- Example: www.example.com

**Domain Name:**
- Part of DNS hierarchy
- Example: example.com

**Resolver:**
- DNS client
- Queries DNS servers
- Caches results

**DNS Query:**
```
Client                   DNS Server
  |  Query: www.example.com |
  |--------------------->  |
  |  Response: 93.184.216.34 |
  |<---------------------|
```

**DNS Hierarchy:**
- Root domain: .
- Top-level domains: .com, .org, .net
- Second-level domains: example.com
- Subdomains: www.example.com

**DNS Caching:**
- Resolvers cache responses
- Reduces DNS queries
- TTL (Time To Live) determines cache duration

**DNS Record Types:**
- **A:** IPv4 address
- **AAAA:** IPv6 address
- **CNAME:** Canonical name (alias)
- **MX:** Mail exchange
- **NS:** Name server
- **TXT:** Text record

**ESP32 DNS Example:**
```cpp
WiFi.begin("SSID", "password");
// DNS configured via DHCP
// Can now use hostnames
WiFiClient client;
client.connect("www.example.com", 80);
// DNS resolves www.example.com to IP
```

**DNS Troubleshooting:**
- Wrong IP: DNS cache issue, wrong DNS server
- No resolution: DNS server down, network issue
- Slow response: DNS server latency, network latency

**Why this matters:** DNS enables human-readable names. Understanding DNS is essential for user-friendly networked applications.

---

### Wi-Fi for Embedded Devices

**Building on Phase 6:**
- Phase 6 introduced ESP32 Wi-Fi basics
- Phase 9 expands on networking aspects

**Station Mode (STA):**
- ESP32 connects to existing network
- Client role
- Uses DHCP for IP assignment
- Most common for IoT devices

**Access Point Mode (AP):**
- ESP32 creates network
- Acts as router
- Devices connect to ESP32
- Useful for configuration, local control

**Station + AP Mode:**
- ESP32 both connects and creates network
- Can bridge networks
- More complex configuration

**SSID (Service Set Identifier):**
- Network name
- Case-sensitive
- Up to 32 characters

**Authentication:**
- Open (no password)
- WEP (obsolete, insecure)
- WPA/WPA2 (common)
- WPA3 (newer, more secure)

**DHCP on Wi-Fi:**
- ESP32 requests IP from DHCP server
- Receives: IP, subnet mask, gateway, DNS
- Simplifies configuration

**IP Assignment:**
- Static IP: Manual configuration
- Dynamic IP: DHCP assignment
- Static IP useful for servers, fixed addresses

**Gateway:**
- Router connecting to internet
- ESP32 sends external traffic through gateway
- Typically: 192.168.1.1 or similar

**DNS:**
- Provided by DHCP
- ESP32 uses for hostname resolution
- Can be manually configured

**Signal Strength:**
- Measured in dBm
- Typical: -30 dBm (excellent) to -90 dBm (poor)
- Affects reliability and speed

**Connection Failures:**
- Wrong SSID/password
- Out of range
- Wrong authentication type
- DHCP server down
- Channel congestion

**Reconnect Strategies:**
- Periodic reconnect attempts
- Exponential backoff
- Fallback to AP mode for configuration
- Watchdog to reset if stuck

**ESP32 Wi-Fi Example:**
```cpp
#include <WiFi.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

void setup() {
  Serial.begin(115200);
  
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.print("Gateway: ");
  Serial.println(WiFi.gatewayIP());
  Serial.print("DNS: ");
  Serial.println(WiFi.dnsIP());
}

void loop() {
  // Check connection, reconnect if needed
  if (WiFi.status() != WL_CONNECTED) {
    WiFi.reconnect();
  }
  delay(10000);
}
```

**Why this matters:** Wi-Fi is the primary connectivity for IoT devices. Understanding Wi-Fi networking aspects is essential for reliable IoT systems.

---

### Sockets

**Socket:**
- Endpoint for communication
- IP address + port
- Abstraction for network programming

**TCP Socket:**
- Connection-oriented
- Reliable
- Stream-oriented
- For applications requiring reliability

**UDP Socket:**
- Connectionless
- Unreliable
- Datagram-oriented
- For applications requiring speed

**Client:**
- Initiates connection
- Connects to server socket
- Typical: Web browser, email client

**Server:**
- Listens for connections
- Accepts client connections
- Typical: Web server, database server

**Listen:**
- Server prepares to accept connections
- Specifies port
- Creates connection queue

**Connect:**
- Client initiates connection to server
- Specifies server IP and port
- Performs TCP handshake

**Send:**
- Transmit data
- TCP: Reliable, ordered
- UDP: Unreliable, unordered

**Receive:**
- Receive data
- Blocks until data available (unless non-blocking)
- Returns data or error

**TCP Client Example (ESP32):**
```cpp
#include <WiFi.h>
#include <WiFiClient.h>

WiFiClient client;
const char* host = "www.example.com";
const int port = 80;

void setup() {
  Serial.begin(115200);
  WiFi.begin("SSID", "password");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  
  if (client.connect(host, port)) {
    Serial.println("Connected to server");
    client.println("GET / HTTP/1.1");
    client.println("Host: www.example.com");
    client.println("Connection: close");
    client.println();
  } else {
    Serial.println("Connection failed");
  }
}

void loop() {
  while (client.available()) {
    char c = client.read();
    Serial.print(c);
  }
  
  if (!client.connected()) {
    client.stop();
    delay(10000);
  }
}
```

**TCP Server Example (ESP32):**
```cpp
#include <WiFi.h>
#include <WiFiServer.h>

WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  WiFi.begin("SSID", "password");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  
  server.begin();
  Serial.println("Server started");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  WiFiClient client = server.available();
  
  if (client) {
    Serial.println("New client");
    String currentLine = "";
    
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        
        if (c == '\n') {
          if (currentLine.length() == 0) {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type: text/html");
            client.println();
            client.println("<html><body>Hello</body></html>");
            break;
          } else {
            currentLine = "";
          }
        } else if (c != '\r') {
          currentLine += c;
        }
      }
    }
    
    client.stop();
  }
}
```

**UDP Example (ESP32):**
```cpp
#include <WiFi.h>
#include <WiFiUDP.h>

WiFiUDP udp;
const int localPort = 8888;
char packetBuffer[255];

void setup() {
  Serial.begin(115200);
  WiFi.begin("SSID", "password");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  
  udp.begin(localPort);
  Serial.print("UDP server on port ");
  Serial.println(localPort);
}

void loop() {
  int packetSize = udp.parsePacket();
  
  if (packetSize) {
    int len = udp.read(packetBuffer, 255);
    if (len > 0) packetBuffer[len] = 0;
    Serial.print("Received: ");
    Serial.println(packetBuffer);
  }
}
```

**Why this matters:** Sockets are the programming interface for network communication. Understanding sockets is essential for networked embedded applications.

---

### Network Troubleshooting

**Systematic Workflow:**

**1. Physical Layer**
- Check cables
- Check link lights
- Check power
- Check wireless signal strength

**2. Link Layer**
- Check MAC address
- Check switch port
- Check ARP table
- Check for collisions

**3. IP Configuration**
- Check IP address
- Check subnet mask
- Check default gateway
- Check for IP conflicts

**4. ARP**
- Check ARP cache
- Ping local network
- Check for ARP issues

**5. Gateway**
- Ping gateway
- Check routing table
- Check firewall rules

**6. DNS**
- Check DNS configuration
- Check DNS resolution
- Check DNS cache

**7. Transport**
- Check firewall rules
- Check port availability
- Check for blocking

**8. Application**
- Check application configuration
- Check application logs
- Check service status

**Windows Tools:**

**ipconfig:**
- Display IP configuration
- `ipconfig`: Basic configuration
- `ipconfig /all`: Detailed configuration
- `ipconfig /release`: Release DHCP lease
- `ipconfig /renew`: Renew DHCP lease

**ping:**
- Test connectivity
- `ping 192.168.1.1`: Ping local gateway
- `ping google.com`: Test internet connectivity
- `ping -n 4`: Send 4 pings

**tracert:**
- Trace route to destination
- `tracert google.com`: Show path to google.com
- Identifies routing issues

**nslookup:**
- DNS query
- `nslookup google.com`: Resolve google.com
- `nslookup google.com 8.8.8.8`: Use specific DNS server

**arp:**
- Display ARP cache
- `arp -a`: Show all ARP entries
- `arp -d`: Clear ARP cache

**Linux Tools:**

**ip:**
- Display/configure network
- `ip addr`: Show IP addresses
- `ip route`: Show routing table
- `ip link`: Show interface status

**ping:**
- Same as Windows
- `ping -c 4`: Send 4 pings

**traceroute:**
- Trace route to destination
- `traceroute google.com`: Show path

**ss:**
- Socket statistics
- `ss -t`: Show TCP sockets
- `ss -u`: Show UDP sockets

**ip neigh:**
- Neighbor table (ARP cache)
- `ip neigh show`: Show ARP entries

**dig/nslookup:**
- DNS query
- `dig google.com`: Detailed DNS query
- `nslookup google.com`: Simple DNS query

**Wireshark:**
- Packet capture and analysis
- Inspect all protocol layers
- Essential for deep troubleshooting
- Can decode protocols: TCP, UDP, HTTP, DNS, etc.

**Common Network Problems:**

**No IP Address:**
- DHCP server down
- Network cable disconnected
- Wi-Fi not connected
- IP conflict

**Cannot Reach Gateway:**
- Gateway down
- Wrong gateway configured
- Routing issue
- Firewall blocking

**Cannot Resolve DNS:**
- DNS server down
- Wrong DNS configured
- Network issue
- DNS cache issue

**Cannot Reach Internet:**
- No internet connection
- Firewall blocking
- Routing issue
- ISP issue

**High Latency:**
- Network congestion
- Long path
- Poor wireless signal
- Overloaded link

**Packet Loss:**
- Network congestion
- Poor wireless signal
- Cabling issues
- Hardware failure

**Why this matters:** Systematic troubleshooting saves time. Understanding network tools and workflow is essential for maintaining networked systems.

---

## Exact Resources

### Resource 1: TCP/IP Guide
- **Provider:** No Starch Press (Book publisher)
- **Level:** Intermediate
- **Cost:** Paid (book)
- **Type:** Structured learning
- **Purpose:** Comprehensive TCP/IP guide
- **URL:** https://www.nostarch.com/tcpipguide

### Resource 2: ESP-IDF WiFi Documentation
- **Provider:** Espressif (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** ESP32 WiFi programming guide
- **URL:** https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/network/esp_wifi.html

### Resource 3: Arduino-ESP32 WiFi Documentation
- **Provider:** Espressif (Official)
- **Level:** Beginner
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** ESP32 WiFi with Arduino
- **URL:** https://docs.espressif.com/projects/arduino-esp32/en/latest/api/wifi.html

### Resource 4: Wireshark Documentation
- **Provider:** Wireshark Foundation (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Packet capture and analysis
- **URL:** https://www.wireshark.org/docs/

### Resource 5: RFC 791 (IP)
- **Provider:** IETF (Official)
- **Level:** Advanced
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** Internet Protocol specification
- **URL:** https://tools.ietf.org/html/rfc791

### Resource 6: RFC 793 (TCP)
- **Provider:** IETF (Official)
- **Level:** Advanced
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** TCP specification
- **URL:** https://tools.ietf.org/html/rfc793

### Resource 7: RFC 768 (UDP)
- **Provider:** IETF (Official)
- **Level:** Advanced
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** UDP specification
- **URL:** https://tools.ietf.org/html/rfc768

### Resource 8: Networking Basics
- **Provider:** Cisco (Structured learning)
- **Level:** Beginner
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Networking fundamentals
- **URL:** https://www.cisco.com/c/en/us/training/events/learning-network/networking-basics.html

### Resource 9: IP Subnetting Guide
- **Provider:** SubnetOnline (Structured learning)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Structured learning
- **Purpose:** Subnet calculation tools and tutorials
- **URL:** https://www.subnet-online.com/

### Resource 10: DNS Overview
- **Provider:** ICANN (Official)
- **Level:** Intermediate
- **Cost:** Free
- **Type:** Official / Primary
- **Purpose:** DNS overview and documentation
- **URL:** https://www.icann.org/resources/pages/dns-overview-2012-02-25-en

---

## Study Order

Follow this exact sequence:

1. **Study networking fundamentals** (hosts, clients, servers, topology)
2. **Understand OSI and TCP/IP models**
3. **Study Ethernet** (MAC addresses, frames, switches, ARP)
4. **Study IP addressing** (IPv4, subnetting, CIDR)
5. **Study IPv6 basics** (address format, compression)
6. **Study ARP** (IP-to-MAC resolution)
7. **Study ICMP** (ping, traceroute)
8. **Study TCP** (handshake, reliability, flow control)
9. **Study UDP** (connectionless, use cases)
10. **Study DHCP** (DORA process, IP assignment)
11. **Study DNS** (hostname resolution, caching)
12. **Study Wi-Fi for embedded** (building on Phase 6)
13. **Study sockets** (TCP/UDP client/server)
14. **Study network troubleshooting** (systematic workflow, tools)
15. **Study Wireshark basics** (packet inspection)
16. **Complete all exercises**
17. **Complete all labs**
18. **Complete the project**
19. **Take the knowledge test**
20. **Take the practical test**
21. **Review completion checklist**

---

## Exercises

### Exercise 1: IP Addressing

**Objective:** Calculate network parameters.

**Tasks:**
1. Given IP 192.168.1.100/24, what is the network address?
2. Given IP 192.168.1.100/24, what is the broadcast address?
3. Given IP 192.168.1.100/24, what is the usable host range?
4. How many usable hosts in /24 subnet?
5. Is 10.0.0.5 a public or private IP?

**Expected Outcome:** You can calculate network parameters.

### Exercise 2: Subnetting

**Objective:** Perform subnetting calculations.

**Tasks:**
1. Subnet 192.168.1.0/24 into 4 subnets. What is the new prefix?
2. What are the network addresses of the 4 subnets?
3. How many usable hosts per subnet?
4. What is the broadcast address of the first subnet?
5. Why subnet networks?

**Expected Outcome:** You can perform subnetting calculations.

### Exercise 3: TCP vs UDP

**Objective:** Compare TCP and UDP.

**Tasks:**
1. List 3 advantages of TCP over UDP
2. List 3 advantages of UDP over TCP
3. When would you use TCP?
4. When would you use UDP?
5. Why is TCP more reliable than UDP?

**Expected Outcome:** You understand TCP vs UDP tradeoffs.

### Exercise 4: DHCP Process

**Objective:** Understand DHCP DORA process.

**Tasks:**
1. What does DORA stand for?
2. Which message is broadcast?
3. Which messages are unicast?
4. What information does DHCP provide?
5. What happens when DHCP lease expires?

**Expected Outcome:** You understand DHCP process.

### Exercise 5: DNS Resolution

**Objective:** Understand DNS resolution.

**Tasks:**
1. What is the purpose of DNS?
2. What is a DNS resolver?
3. What is DNS caching?
4. What is the difference between A record and CNAME?
5. Why is DNS important for embedded systems?

**Expected Outcome:** You understand DNS resolution.

---

## Labs

### Lab 1: Identify Local Network Configuration

**Objective:** Identify network configuration of your PC.

**Prerequisites:**
- PC with network connectivity

**Components:**
- PC

**Theory:**
- Network configuration includes IP, subnet mask, gateway, DNS
- DHCP assigns these automatically
- Can also be configured manually

**Windows Commands:**
```
ipconfig
ipconfig /all
```

**Linux Commands:**
```
ip addr
ip route
```

**Expected Behavior:**
- Display IP address
- Display subnet mask
- Display default gateway
- Display DNS servers

**Document:**
- Your IP address
- Your subnet mask
- Your gateway
- Your DNS servers
- Whether DHCP or static

**Completion Criteria:**
- Can identify network configuration
- Understand each parameter
- Can use network commands

---

### Lab 2: IPv4 Subnetting Exercises

**Objective:** Practice subnetting calculations.

**Prerequisites:**
- Understanding of IP addressing

**Components:**
- None (paper/pencil or calculator)

**Theory:**
- Subnetting divides networks
- Calculations use binary AND
- Practice improves speed

**Exercises:**
1. Network: 10.0.0.0/8. What is the broadcast address?
2. Network: 172.16.0.0/16. How many usable hosts?
3. Network: 192.168.1.0/24. What is the usable host range?
4. Subnet 192.168.1.0/24 into 8 subnets. New prefix?
5. Given /27 prefix, how many usable hosts?

**Expected Outcome:**
- Correct subnetting calculations
- Understanding of binary operations

**Completion Criteria:**
- Can perform subnetting calculations
- Understand prefix notation
- Can calculate network/broadcast/host range

---

### Lab 3: Ping and ICMP

**Objective:** Use ping to test connectivity.

**Prerequisites:**
- PC with network connectivity

**Components:**
- PC

**Theory:**
- Ping uses ICMP Echo Request
- Tests connectivity and latency
- Identifies network problems

**Windows Commands:**
```
ping 127.0.0.1
ping 192.168.1.1
ping 8.8.8.8
ping google.com
ping -n 4 google.com
```

**Linux Commands:**
```
ping -c 4 127.0.0.1
ping -c 4 192.168.1.1
ping -c 4 8.8.8.8
ping -c 4 google.com
```

**Expected Behavior:**
- Ping localhost (loopback) works
- Ping gateway works
- Ping internet (8.8.8.8) works
- Ping hostname (google.com) works
- Latency values displayed

**Document:**
- Latency to gateway
- Latency to 8.8.8.8
- Latency to google.com
- Any packet loss

**Troubleshooting:**
- No response: Device down, firewall blocking
- High latency: Network congestion
- Packet loss: Network problem

**Completion Criteria:**
- Can use ping to test connectivity
- Understand ICMP
- Can interpret ping results

---

### Lab 4: ARP Inspection

**Objective:** Inspect ARP cache and understand ARP.

**Prerequisites:**
- PC with network connectivity

**Components:**
- PC

**Theory:**
- ARP maps IP to MAC
- ARP cache stores mappings
- Viewable with system commands

**Windows Commands:**
```
arp -a
arp -d
ping 192.168.1.1
arp -a
```

**Linux Commands:**
```
ip neigh show
ping 192.168.1.1
ip neigh show
```

**Expected Behavior:**
- ARP cache displayed
- Entries include IP and MAC
- Ping adds entry to cache

**Document:**
- Your MAC address
- Gateway MAC address
- Other device MAC addresses

**Completion Criteria:**
- Can view ARP cache
- Understand ARP process
- Can clear ARP cache

---

### Lab 5: DNS Resolution

**Objective:** Test DNS resolution.

**Prerequisites:**
- PC with network connectivity

**Components:**
- PC

**Theory:**
- DNS resolves hostnames to IPs
- Resolvers cache results
- Can use different DNS servers

**Windows Commands:**
```
nslookup google.com
nslookup google.com 8.8.8.8
```

**Linux Commands:**
```
nslookup google.com
dig google.com
dig google.com @8.8.8.8
```

**Expected Behavior:**
- DNS resolves hostname to IP
- Response includes IP address
- Can use specific DNS server

**Document:**
- IP of google.com
- Response time
- DNS server used

**Troubleshooting:**
- No response: DNS server down, network issue
- Wrong IP: DNS cache issue, wrong DNS server

**Completion Criteria:**
- Can test DNS resolution
- Understand DNS process
- Can use different DNS servers

---

### Lab 6: DHCP Observation

**Objective:** Observe DHCP process.

**Prerequisites:**
- PC with network connectivity
- Wireshark (optional)

**Components:**
- PC
- Wireshark (optional)

**Theory:**
- DHCP assigns IP automatically
- DORA process: Discover, Offer, Request, Ack
- Visible with packet capture

**Without Wireshark:**
```
ipconfig /release
ipconfig /renew
ipconfig /all
```

**With Wireshark:**
1. Start Wireshark capture
2. Run ipconfig /release
3. Run ipconfig /renew
4. Stop capture
5. Filter: bootp
6. Observe DORA messages

**Expected Behavior:**
- IP released (no IP)
- IP renewed (new IP or same)
- Wireshark shows DORA messages

**Document:**
- IP before release
- IP after renew
- DHCP server IP
- Lease time

**Completion Criteria:**
- Understand DHCP process
- Can observe DHCP with Wireshark
- Can renew DHCP lease

---

### Lab 7: ESP32 Wi-Fi Networking

**Objective:** Connect ESP32 to Wi-Fi and observe network parameters.

**Prerequisites:**
- Completed Phase 6 (ESP32)
- Wi-Fi network available

**Components:**
- ESP32 development board
- Wi-Fi network

**Theory:**
- ESP32 connects as station
- DHCP assigns IP
- Gateway and DNS provided

**Arduino-ESP32 Code:**
```cpp
#include <WiFi.h>

const char* ssid = "YOUR_SSID";
const char* password = "YOUR_PASSWORD";

void setup() {
  Serial.begin(115200);
  
  Serial.println("Connecting to WiFi");
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.print("Subnet mask: ");
  Serial.println(WiFi.subnetMask());
  Serial.print("Gateway: ");
  Serial.println(WiFi.gatewayIP());
  Serial.print("DNS: ");
  Serial.println(WiFi.dnsIP());
  Serial.print("RSSI: ");
  Serial.println(WiFi.RSSI());
}

void loop() {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi disconnected, reconnecting...");
    WiFi.reconnect();
  }
  delay(5000);
}
```

**Expected Behavior:**
- ESP32 connects to Wi-Fi
- Serial output shows IP, gateway, DNS
- RSSI shows signal strength

**Document:**
- ESP32 IP address
- Gateway IP
- DNS IP
- Signal strength (RSSI)

**Troubleshooting:**
- Cannot connect: Wrong SSID/password, out of range
- No IP: DHCP server down
- Weak signal: Too far from router

**Completion Criteria:**
- ESP32 connects to Wi-Fi reliably
- Understand DHCP on ESP32
- Can display network parameters

---

### Lab 8: ESP32 TCP Client

**Objective:** Implement TCP client on ESP32.

**Prerequisites:**
- Completed Lab 7
- Understanding of TCP

**Components:**
- ESP32 development board
- Wi-Fi network
- TCP server (e.g., web server)

**Theory:**
- TCP client initiates connection
- 3-way handshake
- Reliable data transfer

**Arduino-ESP32 Code:**
```cpp
#include <WiFi.h>
#include <WiFiClient.h>

WiFiClient client;
const char* host = "www.example.com";
const int port = 80;

void setup() {
  Serial.begin(115200);
  WiFi.begin("SSID", "password");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  
  Serial.println("Connecting to server");
  if (client.connect(host, port)) {
    Serial.println("Connected");
    
    client.println("GET / HTTP/1.1");
    client.println("Host: www.example.com");
    client.println("Connection: close");
    client.println();
  } else {
    Serial.println("Connection failed");
  }
}

void loop() {
  while (client.available()) {
    char c = client.read();
    Serial.print(c);
  }
  
  if (!client.connected()) {
    Serial.println();
    Serial.println("Server disconnected");
    client.stop();
    delay(10000);
  }
}
```

**Expected Behavior:**
- ESP32 connects to server
- HTTP request sent
- Response received and printed

**Document:**
- Server response
- Connection time
- Data received

**Troubleshooting:**
- Cannot connect: Server down, wrong host/port
- No response: Server not responding
- Connection lost: Network issue

**Completion Criteria:**
- TCP client works
- Understand TCP connection
- Can send/receive data

---

### Lab 9: ESP32 TCP Server

**Objective:** Implement TCP server on ESP32.

**Prerequisites:**
- Completed Lab 7
- Understanding of TCP

**Components:**
- ESP32 development board
- Wi-Fi network
- Client device (PC or phone)

**Theory:**
- TCP server listens for connections
- Accepts client connections
- Serves data

**Arduino-ESP32 Code:**
```cpp
#include <WiFi.h>
#include <WiFiServer.h>

WiFiServer server(80);

void setup() {
  Serial.begin(115200);
  WiFi.begin("SSID", "password");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  
  server.begin();
  Serial.println("Server started");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  WiFiClient client = server.available();
  
  if (client) {
    Serial.println("New client");
    
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        Serial.write(c);
        client.write(c);
      }
    }
    
    client.stop();
    Serial.println("Client disconnected");
  }
}
```

**Expected Behavior:**
- Server listens on port 80
- Client can connect
- Echo server (reflects data)

**Test:**
- Use telnet or netcat to connect
- `telnet ESP32_IP 80`
- Type characters, see them echoed

**Document:**
- Server IP
- Client connections
- Data transferred

**Troubleshooting:**
- Cannot connect: Firewall blocking, wrong IP
- No data: Buffer issue, connection issue

**Completion Criteria:**
- TCP server works
- Understand server programming
- Can handle multiple clients

---

### Lab 10: ESP32 UDP Communication

**Objective:** Implement UDP communication on ESP32.

**Prerequisites:**
- Completed Lab 7
- Understanding of UDP

**Components:**
- ESP32 development board
- Wi-Fi network
- UDP client (PC)

**Theory:**
- UDP is connectionless
- No handshake
- Unreliable but fast

**Arduino-ESP32 Code:**
```cpp
#include <WiFi.h>
#include <WiFiUDP.h>

WiFiUDP udp;
const int localPort = 8888;
char packetBuffer[255];

void setup() {
  Serial.begin(115200);
  WiFi.begin("SSID", "password");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }
  
  udp.begin(localPort);
  Serial.print("UDP server on port ");
  Serial.println(localPort);
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  int packetSize = udp.parsePacket();
  
  if (packetSize) {
    Serial.print("Received packet of size ");
    Serial.println(packetSize);
    Serial.print("From ");
    Serial.print(udp.remoteIP());
    Serial.print(":");
    Serial.println(udp.remotePort());
    
    int len = udp.read(packetBuffer, 255);
    if (len > 0) packetBuffer[len] = 0;
    Serial.print("Contents: ");
    Serial.println(packetBuffer);
    
    udp.beginPacket(udp.remoteIP(), udp.remotePort());
    udp.write("ACK");
    udp.endPacket();
  }
}
```

**Expected Behavior:**
- UDP server listens on port 8888
- Receives packets
- Sends ACK response

**Test:**
- Use netcat to send UDP packet
- `echo "Hello" | nc -u ESP32_IP 8888`

**Document:**
- Packets received
- Source IP and port
- Response sent

**Troubleshooting:**
- No packets: Firewall blocking, wrong port
- Packet loss: Normal for UDP

**Completion Criteria:**
- UDP communication works
- Understand UDP vs TCP
- Can send/receive UDP

---

### Lab 11: Network Troubleshooting Challenge

**Objective:** Debug a network problem systematically.

**Prerequisites:**
- Completed previous labs
- Understanding of troubleshooting workflow

**Components:**
- PC
- ESP32
- Network

**Theory:**
- Apply systematic troubleshooting workflow
- Start from physical layer
- Move up layers

**Challenge:**
- Instructor (or self) introduces a problem:
  - Cable disconnected
  - Wrong IP configuration
  - Gateway misconfigured
  - DNS misconfigured
  - Firewall blocking
  - Service not running

**Task:**
- Identify the problem using systematic approach
- Document each step
- Fix the problem
- Verify fix

**Expected Behavior:**
- Systematic troubleshooting applied
- Problem identified and fixed
- Network restored

**Completion Criteria:**
- Can troubleshoot network problems systematically
- Understand troubleshooting workflow
- Can use network tools effectively

---

### Lab 12: Wireshark Packet Observation

**Objective:** Use Wireshark to inspect network traffic.

**Prerequisites:**
- Wireshark installed
- Understanding of protocols

**Components:**
- PC
- Wireshark
- Network

**Theory:**
- Wireshark captures packets
- Displays all protocol layers
- Can filter and analyze

**Tasks:**
1. Start Wireshark
2. Select network interface
3. Start capture
4. Perform ping to google.com
5. Stop capture
6. Filter: `icmp`
7. Observe ICMP packets
8. Perform web request
9. Filter: `http`
10. Observe HTTP packets

**Expected Behavior:**
- Packets captured
- Protocol layers visible
- Filters work correctly

**Document:**
- ICMP packet structure
- HTTP packet structure
- IP addresses
- MAC addresses

**Completion Criteria:**
- Can use Wireshark
- Understand packet structure
- Can filter protocols

---

## Projects

### Project: ESP32 Networked Sensor Node

**Objective:** Create an ESP32-based networked sensor node that transmits sensor data over TCP/UDP.

**Requirements:**
- Read sensor (I2C or analog)
- Connect to Wi-Fi
- Implement TCP server for data access
- Implement UDP for data streaming (optional)
- Implement error handling
- Implement reconnection logic
- Display sensor data via serial
- Document configuration

**Suggested Architecture:**
```
Sensors
    ↓
ESP32
    ↓
Wi-Fi
    ↓
IP Network
    ↓
TCP/UDP
    ↓
PC/Server
    ↓
Data Display/Logging
```

**Deliverables:**
- Working firmware (Arduino-ESP32)
- Circuit documentation
- Code with comments
- TCP server/client working
- Sensor data transmission
- Error handling
- Reconnection logic
- Documentation

**Time Estimate:** 6-8 hours

**Project Structure:**
```
networked-sensor-node/
├── README.md
├── circuit/
│   └── wiring.md
├── src/
│   └── main.ino
├── docs/
│   └── architecture.md
└── results/
    └── measurements.md
```

**Note:** This project teaches networked embedded systems, preparing for IoT and MQTT implementation in later phases.

---

## Common Mistakes

### Mistake 1: Confusing MAC and IP
**Problem:** Treating MAC and IP as the same thing
**Consequence:** Confusion in troubleshooting
**Solution:** MAC is layer 2, IP is layer 3

### Mistake 2: Wrong Subnet Mask
**Problem:** Incorrect subnet mask configuration
**Consequence:** Cannot communicate with other devices
**Solution:** Calculate correct subnet mask for network size

### Mistake 3: IP Address Conflict
**Problem:** Two devices with same IP
**Consequence:** Intermittent connectivity
**Solution:** Use unique IP addresses or DHCP

### Mistake 4: Wrong Gateway
**Problem:** Incorrect default gateway
**Consequence:** Cannot reach internet or other networks
**Solution:** Configure correct gateway IP

### Mistake 5: DNS Issues
**Problem:** Cannot resolve hostnames
**Consequence:** Cannot access services by name
**Solution:** Configure correct DNS servers

### Mistake 6: TCP vs UDP Confusion
**Problem:** Using wrong protocol for application
**Consequence:** Poor performance or unreliability
**Solution:** Understand tradeoffs, choose appropriate protocol

### Mistake 7: Blocking Socket Operations
**Problem:** Socket operations block indefinitely
**Consequence:** Application hangs
**Solution:** Use timeouts or non-blocking sockets

### Mistake 8: No Reconnection Logic
**Problem:** ESP32 never reconnects after disconnect
**Consequence:** Device becomes unusable
**Solution:** Implement reconnection logic with backoff

### Mistake 9: Ignoring Signal Strength
**Problem:** Poor Wi-Fi signal causes unreliability
**Consequence:** Intermittent connectivity
**Solution:** Monitor RSSI, improve signal or handle failures

### Mistake 10: Not Troubleshooting Systematically
**Problem:** Random debugging approach
**Consequence:** Wasting time, missing root cause
**Solution:** Follow systematic workflow from physical to application

---

## Troubleshooting

### Network Connectivity Problems
**Problem:** Cannot reach internet
**Solutions:**
- Check physical connection
- Check IP configuration
- Ping gateway
- Ping external IP (8.8.8.8)
- Check DNS resolution
- Check firewall

### Wi-Fi Problems
**Problem:** ESP32 cannot connect to Wi-Fi
**Solutions:**
- Check SSID and password
- Check signal strength
- Check authentication type
- Check for interference
- Reboot ESP32

### TCP Connection Problems
**Problem:** Cannot establish TCP connection
**Solutions:**
- Check server is running
- Check IP and port
- Check firewall
- Check network connectivity
- Check timeout settings

### DNS Problems
**Problem:** Cannot resolve hostnames
**Solutions:**
- Check DNS server configuration
- Ping DNS server
- Try different DNS server (8.8.8.8)
- Clear DNS cache
- Check network connectivity

### High Latency
**Problem:** Slow network response
**Solutions:**
- Check network congestion
- Check routing path (traceroute)
- Check wireless signal
- Check for interference

### Packet Loss
**Problem:** Lost packets
**Solutions:**
- Check network congestion
- Check cabling
- Check wireless signal
- Check for hardware issues

---

## Knowledge Test

Answer these questions without looking at the materials:

1. What is the difference between a host and a node?
2. What is the difference between TCP and UDP?
3. What is the purpose of a subnet mask?
4. What is CIDR notation?
5. What is the difference between private and public IP?
6. What is ARP used for?
7. What is the purpose of ICMP?
8. What is a TCP three-way handshake?
9. What is the DHCP DORA process?
10. What is DNS used for?
11. What is the difference between MAC address and IP address?
12. What is the purpose of a gateway?
13. What is a socket?
14. What is the difference between TCP client and server?
15. What is Wireshark used for?
16. What is the first step in network troubleshooting?
17. What does TTL stand for?
18. What is the difference between broadcast and unicast?
19. Why is reconnection logic important for embedded devices?
20. What is the difference between station mode and AP mode?

**Passing Score:** 16/20 correct answers

---

## Practical Test

Complete these practical tasks:

1. **Network Configuration:**
   - Identify your PC's network configuration
   - Document IP, subnet mask, gateway, DNS
   - Explain each parameter

2. **Subnetting:**
   - Subnet a given network into required subnets
   - Calculate network, broadcast, and host ranges
   - Document calculations

3. **Network Tools:**
   - Use ping to test connectivity
   - Use traceroute to identify path
   - Use nslookup to test DNS
   - Document results

4. **ESP32 Networking:**
   - Connect ESP32 to Wi-Fi
   - Display network parameters
   - Implement TCP client or server
   - Test communication

5. **Troubleshooting:**
   - Given a network problem, identify the cause
   - Document troubleshooting steps
   - Propose and implement solution
   - Verify fix

**Passing Criteria:** All tasks completed with understanding demonstrated.

---

## Completion Checklist

Before moving to Phase 10, verify you have:

- [ ] Understand networking fundamentals
- [ ] Understand OSI and TCP/IP models
- [ ] Can perform IPv4 subnetting
- [ ] Understand IPv6 basics
- [ ] Understand ARP
- [ ] Understand ICMP (ping, traceroute)
- [ ] Understand TCP (handshake, reliability)
- [ ] Understand UDP (connectionless, use cases)
- [ ] Understand DHCP (DORA process)
- [ ] Understand DNS (resolution, caching)
- [ ] Can configure ESP32 Wi-Fi
- [ ] Can implement TCP client/server
- [ ] Can implement UDP communication
- [ ] Can use network diagnostic tools
- [ ] Can use Wireshark for packet inspection
- [ ] Can troubleshoot network problems systematically
- [ ] Completed all exercises
- [ ] Completed at least 5 labs
- [ ] Completed the networked sensor node project
- [ ] Passed the knowledge test (16/20 correct)
- [ ] Passed the practical test

---

## Do Not Continue Until...

**Do not start Phase 10 until:**

1. You have passed the knowledge test (16/20 correct)
2. You have passed the practical test
3. You have completed the completion checklist
4. You understand TCP/IP networking
5. You can configure networked embedded systems
6. You have completed at least 5 labs
7. You have completed the networked sensor node project
8. You can troubleshoot network problems systematically
9. You understand the difference between communication protocols and networking

**Networking is the foundation of IoT. Mastering TCP/IP, Wi-Fi, and network troubleshooting is essential before moving to IoT protocols like MQTT.**

---

## Next Step

Once you have completed this phase successfully, proceed to:

**Phase 10 — MQTT and IoT**

Phase 10 will teach you about MQTT protocol, IoT architectures, cloud integration, and building complete IoT systems, building on the networking foundation you established here.

---

**Networking enables embedded devices to communicate beyond local communication protocols. Understanding TCP/IP, Wi-Fi, and network troubleshooting is essential for any IoT system.**
