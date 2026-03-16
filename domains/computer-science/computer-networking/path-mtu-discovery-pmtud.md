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
builds-toward:
- tcp-flow-control-and-congestion-control
- network-management-and-monitoring
tags:
- network-layer
- mtu
- path-discovery
- icmp
stage: advanced
status: draft
---

# Path MTU Discovery and Handling MTU Issues

## Core Idea
Path MTU Discovery (PMTUD) determines the smallest MTU along a path to avoid fragmentation. The source sends packets with the DF (Do Not Fragment) flag set; routers responding with ICMP Fragmentation Needed messages indicate the bottleneck MTU. Hosts adjust MSS (Maximum Segment Size) accordingly, improving performance.

## How It's Best Learned
Trace PMTUD across networks with varying MTUs using ping with DF flag and large sizes. Observe ICMP Fragmentation Needed messages. Simulate broken PMTUD (blocked ICMP) and observe performance degradation. Monitor MSS negotiation in TCP handshakes.

## Common Misconceptions
PMTUD requires ICMP Fragmentation Needed messages; blocking ICMP breaks PMTUD. MTU-related issues cause subtle failures; packets succeed on some hops but fail downstream. Black-hole routers (drop ICMP) cause connection timeouts, not immediate failures.

## Explainer

From your study of IP fragmentation, you know that every network link has a **Maximum Transmission Unit (MTU)** — the largest packet it can carry. When a packet exceeds a link's MTU, the router must either fragment it or drop it. Fragmentation works but carries real costs: it wastes bandwidth on duplicate headers, complicates reassembly at the destination, and if any fragment is lost, the entire original packet must be retransmitted. Path MTU Discovery exists to avoid fragmentation entirely by figuring out the smallest MTU along the entire path before sending full-sized data.

The mechanism is elegant and relies directly on ICMP, which you already understand. The sender sets the **Don't Fragment (DF)** flag on every outgoing IP packet. When a router along the path encounters a packet larger than its outgoing link's MTU, it cannot fragment it (because DF is set), so it drops the packet and sends back an **ICMP Fragmentation Needed** message. This ICMP message includes the MTU of the bottleneck link. The sender receives this feedback, reduces its packet size to fit through that link, and retries. This process repeats until packets pass through every link without hitting an MTU ceiling — at that point, the sender has discovered the **path MTU**, the smallest MTU across all hops.

In practice, PMTUD interacts closely with TCP. During the TCP handshake, both sides advertise their **Maximum Segment Size (MSS)**, which is derived from their local MTU minus header overhead. But the local MTU only reflects the first hop — the path MTU could be smaller. When PMTUD discovers a tighter bottleneck, TCP adjusts its segment size downward so that IP packets (segment plus headers) fit within the path MTU. This adjustment happens transparently to the application.

The most common failure mode is **PMTUD black holes**. Some network administrators configure firewalls to block all ICMP traffic, believing this improves security. But this prevents ICMP Fragmentation Needed messages from reaching the sender. The sender keeps transmitting oversized packets with DF set, the bottleneck router keeps dropping them silently, and the connection stalls — packets simply vanish with no error feedback. The connection appears to establish normally (small handshake packets pass through fine) but hangs when transferring real data. This is notoriously difficult to debug because the symptoms — timeouts on large transfers, working pings but failing downloads — do not obviously point to an MTU problem. The lesson is clear: ICMP is not optional. Blocking it breaks fundamental internet mechanisms.
