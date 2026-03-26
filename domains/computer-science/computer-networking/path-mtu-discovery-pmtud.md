---
id: path-mtu-discovery-pmtud
title: Path MTU Discovery and Handling MTU Issues
domain: computer-science
course: computer-networking
prerequisites:
- id: ip-fragmentation-reassembly
  type: hard
- id: icmp-internet-control-message-protocol
  type: hard
- id: icmpv6-neighbor-discovery-protocol
  type: soft
builds-toward:
- tcp-flow-control-and-congestion-control
- network-management-and-monitoring
tags:
- network-layer
- mtu
- path-discovery
- icmp
stage: advanced
status: validated
---
# Path MTU Discovery and Handling MTU Issues

## Core Idea
Path MTU Discovery (PMTUD) determines the smallest MTU along a path to avoid fragmentation. The source sends packets with the DF (Do Not Fragment) flag set; routers responding with ICMP Fragmentation Needed messages indicate the bottleneck MTU. Hosts adjust MSS (Maximum Segment Size) accordingly, improving performance.

## How It's Best Learned
Trace PMTUD across networks with varying MTUs using ping with DF flag and large sizes. Observe ICMP Fragmentation Needed messages. Simulate broken PMTUD (blocked ICMP) and observe performance degradation. Monitor MSS negotiation in TCP handshakes.

## Common Misconceptions
PMTUD requires ICMP Fragmentation Needed messages; blocking ICMP breaks PMTUD. MTU-related issues cause subtle failures; packets succeed on some hops but fail downstream. Black-hole routers (drop ICMP) cause connection timeouts, not immediate failures.

## Questions

```yaml
- question: "A TCP connection establishes successfully — the handshake completes and small messages transfer fine — but the connection hangs every time a large file transfer begins. Pings to the same host succeed. The DF flag is set on data packets. What is the most likely cause?"
  type: multiple-choice
  options:
    - "TCP's congestion window is collapsing due to a slow uplink"
    - "ICMP Fragmentation Needed messages are being blocked by a firewall, preventing PMTUD from reducing the packet size"
    - "The server's MSS advertisement during the handshake is misconfigured too large"
    - "The local network interface MTU is smaller than 1500 bytes, causing the initial path MTU estimate to be wrong"
  answer: 1
  explanation: "This is the classic PMTUD black hole symptom. Small packets (SYN, ACK, short messages) fit within every link's MTU and pass through fine. Large data packets with DF set exceed some intermediate link's MTU, so that router drops them and sends ICMP Fragmentation Needed back to the sender. But if a firewall blocks all ICMP, the sender never receives this feedback — it keeps retransmitting the same oversized packets, which keep getting dropped silently. The connection stalls indefinitely. The handshake works because small control packets are not affected by the MTU bottleneck."

- question: "What is the purpose of setting the DF (Don't Fragment) flag in PMTUD, given that allowing fragmentation seems simpler?"
  type: multiple-choice
  options:
    - "DF prevents TCP reassembly at the destination from being overloaded by fragments"
    - "DF forces routers to send ICMP feedback when a packet is too large, so the sender can learn the bottleneck MTU and avoid fragmentation entirely"
    - "DF is required by the TCP specification and is set automatically regardless of PMTUD"
    - "DF prevents intermediate routers from modifying the packet payload in transit"
  answer: 1
  explanation: "PMTUD's goal is to discover and avoid fragmentation, not just work around it. Fragmentation wastes bandwidth on duplicate headers, adds reassembly latency, and forces full packet retransmission if any fragment is lost. By setting DF, the sender forces routers to send ICMP Fragmentation Needed when a packet is too large rather than silently fragmenting it. This feedback tells the sender exactly how much to shrink its packets, enabling efficient large transfers without fragmentation overhead."

- question: "Blocking most ICMP traffic at a firewall improves security without affecting TCP functionality like Path MTU Discovery."
  type: true-false
  answer: false
  explanation: "ICMP is not optional for correct TCP operation. PMTUD depends entirely on receiving ICMP Fragmentation Needed messages from bottleneck routers. Blocking ICMP creates a black hole: oversized packets with DF set are dropped silently, the sender never receives feedback, and large transfers stall. The firewall administrator may believe they're improving security, but they're breaking a fundamental IP mechanism. Selective ICMP filtering — allowing Fragmentation Needed (Type 3, Code 4) while blocking echo requests — is the correct approach."

- question: "When a router encounters a packet larger than its outgoing link's MTU with the DF flag set, it sends back an ICMP Fragmentation Needed message containing the MTU of the bottleneck link."
  type: true-false
  answer: true
  explanation: "This is the core mechanism of PMTUD. The router cannot fragment the packet (DF is set) so it drops it and sends ICMP Type 3, Code 4 (Destination Unreachable: Fragmentation Needed), including the Next-Hop MTU field — the MTU of the link the packet couldn't traverse. The sender uses this to reduce packet size and retransmit. This process repeats at each bottleneck until packets pass through every link without hitting an MTU ceiling."

- question: "Why do PMTUD black holes cause connections to fail only during large data transfers and not during the TCP handshake or small request exchanges?"
  type: short-answer
  answer: "Handshake packets (SYN, SYN-ACK, ACK) and small messages carry no large payload and fit easily within any link's MTU — typically well under 576 bytes. Only when actual data transfer begins do packets grow to the negotiated MSS size — typically 1460 bytes of data plus 40 bytes of IP/TCP headers, totaling 1500 bytes (standard Ethernet MTU). If any link along the path has a smaller MTU (e.g., a VPN at 1400 bytes or PPPoE at 1492 bytes), only those large data packets exceed the limit and get silently dropped."
  explanation: "This asymmetry — small packets work, large ones silently fail — is the diagnostic clue pointing to an MTU problem. Network engineers test for this by sending pings with large payloads and the DF flag set. The symptom of 'browsing works but file downloads hang' almost always indicates a PMTUD black hole."
```

## Explainer

From your study of IP fragmentation, you know that every network link has a **Maximum Transmission Unit (MTU)** — the largest packet it can carry. When a packet exceeds a link's MTU, the router must either fragment it or drop it. Fragmentation works but carries real costs: it wastes bandwidth on duplicate headers, complicates reassembly at the destination, and if any fragment is lost, the entire original packet must be retransmitted. Path MTU Discovery exists to avoid fragmentation entirely by figuring out the smallest MTU along the entire path before sending full-sized data.

The mechanism is elegant and relies directly on ICMP, which you already understand. The sender sets the **Don't Fragment (DF)** flag on every outgoing IP packet. When a router along the path encounters a packet larger than its outgoing link's MTU, it cannot fragment it (because DF is set), so it drops the packet and sends back an **ICMP Fragmentation Needed** message. This ICMP message includes the MTU of the bottleneck link. The sender receives this feedback, reduces its packet size to fit through that link, and retries. This process repeats until packets pass through every link without hitting an MTU ceiling — at that point, the sender has discovered the **path MTU**, the smallest MTU across all hops.

In practice, PMTUD interacts closely with TCP. During the TCP handshake, both sides advertise their **Maximum Segment Size (MSS)**, which is derived from their local MTU minus header overhead. But the local MTU only reflects the first hop — the path MTU could be smaller. When PMTUD discovers a tighter bottleneck, TCP adjusts its segment size downward so that IP packets (segment plus headers) fit within the path MTU. This adjustment happens transparently to the application.

The most common failure mode is **PMTUD black holes**. Some network administrators configure firewalls to block all ICMP traffic, believing this improves security. But this prevents ICMP Fragmentation Needed messages from reaching the sender. The sender keeps transmitting oversized packets with DF set, the bottleneck router keeps dropping them silently, and the connection stalls — packets simply vanish with no error feedback. The connection appears to establish normally (small handshake packets pass through fine) but hangs when transferring real data. This is notoriously difficult to debug because the symptoms — timeouts on large transfers, working pings but failing downloads — do not obviously point to an MTU problem. The lesson is clear: ICMP is not optional. Blocking it breaks fundamental internet mechanisms.
