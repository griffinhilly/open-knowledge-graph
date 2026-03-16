---
id: packet-switching-circuit-switching
title: Packet Switching vs. Circuit Switching
domain: computer-science
course: computer-networking
prerequisites:
- id: network-fundamentals
  type: hard
builds-toward:
- osi-model-layers
tags:
- switching
- packet-switching
- circuit-switching
- network-design
stage: advanced
status: draft
---

# Packet Switching vs. Circuit Switching

## Core Idea
Packet switching divides data into small packets that are independently routed across shared network links, while circuit switching establishes a dedicated end-to-end path before communication begins. Packet switching provides better utilization of shared resources and fault tolerance but introduces latency variability; circuit switching guarantees bandwidth but wastes resources if no data is being sent. Most modern networks use packet switching.

## Explainer

Think of the difference between a phone call and sending a letter. In a traditional phone call, the telephone network establishes a dedicated circuit — a continuous electrical path — between you and the person you are calling. That path is yours for the duration of the call, whether you are speaking, listening, or sitting in silence. This is **circuit switching**: a dedicated, reserved connection from end to end. The old telephone network (PSTN) worked exactly this way, physically connecting copper wires through mechanical switches at each exchange.

**Packet switching** takes a fundamentally different approach. Instead of reserving a path, it breaks your data into small, self-contained **packets**, each labeled with a source address, destination address, and sequence number. These packets are tossed into the network independently, and each router along the way makes its own forwarding decision about where to send each packet next. Two packets from the same message might travel completely different routes and arrive out of order — the receiving end reassembles them using the sequence numbers. This is how the internet works, and it is the design you studied in network fundamentals.

The core tradeoff comes down to resource utilization versus predictability. Circuit switching guarantees a fixed amount of bandwidth for the entire session, which means consistent latency and no contention — ideal for real-time voice. But if you pause mid-conversation, the circuit sits idle while still consuming network capacity that no one else can use. Packet switching shares links among many users simultaneously through **statistical multiplexing**: since most connections are bursty (active in short bursts, idle most of the time), the network can serve far more users than it has dedicated capacity for. A 1 Gbps link shared among 100 users who each burst at 10 Mbps works well because they rarely all burst at once.

The cost of this efficiency is **variable latency**. Packets may queue behind other packets at congested routers, introducing delays that fluctuate depending on network load. This is why video calls sometimes stutter — the underlying packet-switched network cannot guarantee the constant timing that circuit switching provides. Modern networks address this with quality-of-service mechanisms and buffering, but the fundamental tradeoff remains: packet switching wins on efficiency and resilience (if one path fails, packets reroute around it), while circuit switching wins on guaranteed performance. The internet's dominance proves that for most applications, the efficiency gains of packet switching far outweigh the cost of managing variable delay.
