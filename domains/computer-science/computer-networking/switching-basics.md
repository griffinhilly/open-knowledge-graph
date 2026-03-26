---
id: switching-basics
title: Network Switching and Switching Tables
domain: computer-science
course: computer-networking
prerequisites:
- id: mac-addressing
  type: hard
builds-toward:
- vlans-virtual-area-networks
- spanning-tree-protocol-stp
tags:
- switch
- forwarding
- mac-table
- layer-2-forwarding
stage: advanced
status: validated
---

# Network Switching and Switching Tables

## Core Idea
A network switch is a Layer 2 device that forwards frames based on destination MAC addresses using a MAC address table. Switches learn MAC addresses by observing source addresses in arriving frames, then forward frames destined for known addresses directly to the appropriate port, reducing collision domains and improving bandwidth utilization.

## Questions

```yaml
- question: "A switch's MAC table has entries for ports 1–3. A frame arrives on Port 1 with source MAC AA:AA:AA:AA:AA:01 and destination MAC DD:DD:DD:DD:DD:04 (not in the table). What does the switch do?"
  type: multiple-choice
  options:
    - "Drops the frame, because it cannot forward to an unknown destination"
    - "Sends it back out Port 1, because that is where the frame arrived from"
    - "Floods the frame out every port except Port 1, to ensure delivery to the unknown destination"
    - "Queries a central directory service to look up the location of DD:DD:DD:DD:DD:04"
  answer: 2
  explanation: "When a switch receives a frame destined for a MAC address not in its table, it floods — sends the frame out all ports except the one it arrived on. This guarantees delivery even without complete knowledge. Flooding also occurs for broadcast frames (destination FF:FF:FF:FF:FF:FF). As the destination device responds, its source MAC address is learned and the switch adds it to the table. Subsequent frames to that destination will be forwarded precisely, not flooded. The key rule: unknown destination → flood; known destination → forward to specific port only."

- question: "When a new device connects to a switch and sends its first frame, how does the switch learn the device's MAC address?"
  type: multiple-choice
  options:
    - "The switch broadcasts a discovery query and the device responds with its MAC address"
    - "The switch reads the source MAC address of the arriving frame and records which port it arrived on"
    - "The network administrator manually enters the MAC-to-port mapping in the switch configuration"
    - "The device sends a special MAC registration frame that the switch stores separately"
  answer: 1
  explanation: "Switch learning is entirely passive and automatic. Every incoming frame contains a source MAC address, and the switch records 'this MAC address is reachable via this port' in its CAM table. No special registration or configuration is required. This is why MAC learning is called a 'transparent' process — devices have no idea a switch is observing their traffic. Table entries age out after ~300 seconds so the switch adapts as devices move or disconnect. The switch only learns from SOURCE addresses; it uses DESTINATION addresses for forwarding decisions."

- question: "A hub and a switch both connect multiple devices on a network. When a frame arrives, both devices forward it to most connected ports, making them functionally equivalent for normal network operation."
  type: true-false
  answer: false
  explanation: "This is the core distinction: a hub always floods every frame to every port — it has no intelligence and no MAC table. A switch floods only for unknown destinations and broadcasts; for known destinations, it forwards exclusively to the appropriate port. The practical consequences are dramatic: on a hub, all devices share the same collision domain and the same bandwidth. On a switch, each port is its own collision domain — devices on different ports can transmit simultaneously, and the switch's internal fabric can handle multiple conversations in parallel (microsegmentation), delivering full bandwidth to each port."

- question: "Each port on a network switch is its own collision domain, which allows multiple devices on different ports to transmit simultaneously without interfering with each other."
  type: true-false
  answer: true
  explanation: "Microsegmentation is the defining performance advantage of switches over hubs. On a hub, all ports share a single collision domain: if two devices transmit at the same time, the signals collide and both must retransmit (CSMA/CD). On a switch, each port connects to an independent collision domain. Two devices on different ports can transmit simultaneously; the switch's internal switching fabric handles both frames concurrently. A 24-port switch effectively gives each device a dedicated, full-bandwidth link — something impossible with a hub regardless of its port count."

- question: "Explain what 'flooding' is in network switching, when it occurs, and what mechanism causes its frequency to decrease over time on an active network."
  type: short-answer
  answer: "Flooding is when a switch sends a received frame out every port except the one it arrived on. It occurs in two situations: (1) when the destination MAC address is not yet in the switch's MAC address table — the switch doesn't know which port leads to the destination; and (2) always, for broadcast frames with destination FF:FF:FF:FF:FF:FF. As devices communicate normally, every frame they send teaches the switch about their location: the switch records the source MAC address and ingress port, building its table. Once a destination MAC is in the table, the switch forwards precisely to that port instead of flooding. On an active network, the MAC table fills in quickly and steady-state flooding drops to only genuine broadcasts and occasional unicast floods for new or moved devices."
  explanation: "Understanding flooding is essential because it explains both the initial behavior of a new switch (it floods everything until it learns) and persistent flooding-related issues like broadcast storms. Flooding is a safety mechanism — it ensures delivery even with incomplete knowledge — but it generates traffic that all ports must process. Table aging (entries expire after ~300 seconds) is the mechanism that handles devices moving or disconnecting: the stale entry times out, and the next frame from that device teaches the switch its new location."
```

## Explainer

From your study of MAC addressing, you know that every network interface has a unique hardware address burned into it, and that Ethernet frames carry source and destination MAC addresses. A switch exploits this addressing to make intelligent forwarding decisions. Before switches, networks used **hubs** — simple devices that repeat every incoming frame out every port. This meant all devices shared the same bandwidth and could hear each other's traffic, creating a single large **collision domain** where only one device could transmit at a time. Switches solved this problem by learning which device is connected to which port and sending frames only where they need to go.

The mechanism is elegantly simple. A switch maintains a **MAC address table** (also called a CAM table — Content Addressable Memory) that maps MAC addresses to port numbers. When a frame arrives on port 3 with source MAC AA:BB:CC:DD:EE:01, the switch records "AA:BB:CC:DD:EE:01 is reachable via port 3" in its table. This is called **learning**. Now when a frame arrives destined for that MAC address, the switch knows to forward it out port 3 only — no other ports see the traffic. This process is entirely automatic; no configuration is required. Table entries are aged out after a timeout (typically 300 seconds) so that the table stays current as devices move or disconnect.

When a switch receives a frame destined for a MAC address that is not yet in its table, it performs **flooding** — sending the frame out every port except the one it arrived on. This is also what happens with broadcast frames (destination FF:FF:FF:FF:FF:FF). Flooding ensures delivery even without complete knowledge, at the cost of extra traffic. As devices respond and the switch observes their source addresses, the table fills in and subsequent frames are forwarded precisely. The process of receiving a frame and checking the table is called **filtering and forwarding**: if the destination port is known and different from the source port, forward; if the destination port equals the source port, drop (the destination is already on the same segment); if unknown, flood.

The practical impact of switching is dramatic. Each switch port becomes its own collision domain, meaning devices on different ports can transmit simultaneously without interfering. A 24-port switch effectively gives each connected device a dedicated link to the switch, and the switch's internal fabric can handle multiple simultaneous forwarding operations. This is why modern Ethernet networks can deliver full bandwidth to every port concurrently — a capability called **microsegmentation** — whereas a hub divided the total bandwidth among all devices. Understanding switching is foundational for the topics ahead: VLANs partition a single switch into multiple logical segments, and the Spanning Tree Protocol prevents loops when switches are interconnected.
