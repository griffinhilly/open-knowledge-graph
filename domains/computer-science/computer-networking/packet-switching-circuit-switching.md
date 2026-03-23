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
status: validated
---

# Packet Switching vs. Circuit Switching

## Core Idea
Packet switching divides data into small packets that are independently routed across shared network links, while circuit switching establishes a dedicated end-to-end path before communication begins. Packet switching provides better utilization of shared resources and fault tolerance but introduces latency variability; circuit switching guarantees bandwidth but wastes resources if no data is being sent. Most modern networks use packet switching.

## Questions

```yaml
- question: "100 users share a 1 Gbps packet-switched link. Each user can burst at 10 Mbps but is only actively transmitting 10% of the time. A network engineer claims this configuration works well in practice. What is the core reason?"
  type: multiple-choice
  options:
    - "Each user is allocated a guaranteed 10 Mbps slice of the 1 Gbps link at all times"
    - "Statistical multiplexing: because users are bursty and mostly idle, the probability that all 100 burst simultaneously is very low, so shared capacity suffices on average"
    - "Packet switching compresses data, reducing the effective bandwidth required per user"
    - "Routers distribute bandwidth perfectly equally so each user always gets exactly 10 Mbps"
  answer: 1
  explanation: "This is the fundamental efficiency argument for packet switching. If the link were circuit-switched, serving 100 users at 10 Mbps each would require 1 Gbps — exactly the link capacity — and idle time would be wasted. Packet switching uses statistical multiplexing: since real traffic is bursty and users are idle most of the time, the network can serve far more users than its dedicated capacity would suggest. When users don't all burst at once (which is statistically typical), everyone gets what they need. The cost of this efficiency is that when many users burst simultaneously, they experience queuing delays — variable latency is the price of statistical sharing."

- question: "A surgeon is performing a remote operation over a network, relying on robotic arm feedback with a hard real-time requirement of sub-5ms round-trip latency at all times. Which switching approach better serves this use case?"
  type: multiple-choice
  options:
    - "Packet switching — the internet's routing resilience ensures reliable delivery"
    - "Circuit switching — it reserves a dedicated end-to-end path guaranteeing consistent, predictable latency without queuing variability"
    - "Packet switching with QoS prioritization — always sufficient for real-time applications"
    - "Circuit switching — because packets would arrive out of order and require reassembly delay"
  answer: 1
  explanation: "This is the scenario where circuit switching's key strength — guaranteed, predictable bandwidth and latency — matters most. Packet switching introduces variable latency because packets queue behind other traffic at routers; under load, delays can spike unpredictably. For a remote surgical system where a 50ms latency spike could cause physical harm, the guarantee of a dedicated circuit with no queuing variability justifies the inefficiency of reserved (sometimes idle) bandwidth. QoS can reduce latency variability in packet networks but cannot eliminate it entirely."

- question: "In a packet-switched network, if a router on the primary path between two communicating hosts fails mid-session, the entire session must be torn down and re-established from the beginning."
  type: true-false
  answer: false
  explanation: "Fault tolerance is one of packet switching's core advantages. Because packets are independently routed and the network has no per-session state (unlike circuit switching's reserved paths), surviving routers can simply reroute subsequent packets along an alternate path. The receiving end reassembles packets using sequence numbers regardless of route. The session continues with a possible brief interruption but does not need to restart. This resilience was in fact a primary design goal of the original ARPANET — the predecessor to the internet."

- question: "In circuit switching, reserved bandwidth for an active session remains unavailable to other connections even during periods when no data is being transmitted."
  type: true-false
  answer: true
  explanation: "This is the defining inefficiency of circuit switching. When a circuit is established, resources (bandwidth on each link segment, switching capacity) are reserved end-to-end for the duration of the session. If you pause mid-phone-call, the circuit is still held open and no other call can use those reserved resources. Packet switching eliminates this waste through statistical multiplexing — shared links carry traffic from whoever has data to send at any moment, rather than sitting idle for a session that has nothing to transmit right now."

- question: "Explain why the internet was designed around packet switching rather than circuit switching, given that packet switching introduces variable latency."
  type: short-answer
  answer: "Packet switching was chosen primarily for efficiency and resilience. Statistical multiplexing allows shared links to serve far more users than their raw capacity would permit under circuit switching, since real traffic is bursty rather than continuous. Packet switching also provides fault tolerance — if a router fails, packets reroute around it without session state being lost. The variable latency cost is acceptable for the vast majority of applications (web browsing, email, file transfer, streaming) that can tolerate some delay variability. For real-time applications requiring strict latency guarantees, modern networks use quality-of-service mechanisms to reduce (though not eliminate) variability."
  explanation: "The key insight is that variable latency is a tradeoff, not a flaw. For most use cases, the efficiency and resilience gains of packet switching far outweigh the cost of managing variable delay. The internet's success proves this empirically — virtually all global data communication now runs on packet-switched infrastructure, with circuit switching surviving only in specialized contexts like legacy telephony and some industrial control systems."
```

## Explainer

Think of the difference between a phone call and sending a letter. In a traditional phone call, the telephone network establishes a dedicated circuit — a continuous electrical path — between you and the person you are calling. That path is yours for the duration of the call, whether you are speaking, listening, or sitting in silence. This is **circuit switching**: a dedicated, reserved connection from end to end. The old telephone network (PSTN) worked exactly this way, physically connecting copper wires through mechanical switches at each exchange.

**Packet switching** takes a fundamentally different approach. Instead of reserving a path, it breaks your data into small, self-contained **packets**, each labeled with a source address, destination address, and sequence number. These packets are tossed into the network independently, and each router along the way makes its own forwarding decision about where to send each packet next. Two packets from the same message might travel completely different routes and arrive out of order — the receiving end reassembles them using the sequence numbers. This is how the internet works, and it is the design you studied in network fundamentals.

The core tradeoff comes down to resource utilization versus predictability. Circuit switching guarantees a fixed amount of bandwidth for the entire session, which means consistent latency and no contention — ideal for real-time voice. But if you pause mid-conversation, the circuit sits idle while still consuming network capacity that no one else can use. Packet switching shares links among many users simultaneously through **statistical multiplexing**: since most connections are bursty (active in short bursts, idle most of the time), the network can serve far more users than it has dedicated capacity for. A 1 Gbps link shared among 100 users who each burst at 10 Mbps works well because they rarely all burst at once.

The cost of this efficiency is **variable latency**. Packets may queue behind other packets at congested routers, introducing delays that fluctuate depending on network load. This is why video calls sometimes stutter — the underlying packet-switched network cannot guarantee the constant timing that circuit switching provides. Modern networks address this with quality-of-service mechanisms and buffering, but the fundamental tradeoff remains: packet switching wins on efficiency and resilience (if one path fails, packets reroute around it), while circuit switching wins on guaranteed performance. The internet's dominance proves that for most applications, the efficiency gains of packet switching far outweigh the cost of managing variable delay.
