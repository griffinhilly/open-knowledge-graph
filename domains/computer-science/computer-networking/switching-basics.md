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
- spanning-tree-protocol
tags:
- switch
- forwarding
- mac-table
- layer-2-forwarding
stage: advanced
status: draft
---

# Network Switching and Switching Tables

## Core Idea
A network switch is a Layer 2 device that forwards frames based on destination MAC addresses using a MAC address table. Switches learn MAC addresses by observing source addresses in arriving frames, then forward frames destined for known addresses directly to the appropriate port, reducing collision domains and improving bandwidth utilization.

## Explainer

From your study of MAC addressing, you know that every network interface has a unique hardware address burned into it, and that Ethernet frames carry source and destination MAC addresses. A switch exploits this addressing to make intelligent forwarding decisions. Before switches, networks used **hubs** — simple devices that repeat every incoming frame out every port. This meant all devices shared the same bandwidth and could hear each other's traffic, creating a single large **collision domain** where only one device could transmit at a time. Switches solved this problem by learning which device is connected to which port and sending frames only where they need to go.

The mechanism is elegantly simple. A switch maintains a **MAC address table** (also called a CAM table — Content Addressable Memory) that maps MAC addresses to port numbers. When a frame arrives on port 3 with source MAC AA:BB:CC:DD:EE:01, the switch records "AA:BB:CC:DD:EE:01 is reachable via port 3" in its table. This is called **learning**. Now when a frame arrives destined for that MAC address, the switch knows to forward it out port 3 only — no other ports see the traffic. This process is entirely automatic; no configuration is required. Table entries are aged out after a timeout (typically 300 seconds) so that the table stays current as devices move or disconnect.

When a switch receives a frame destined for a MAC address that is not yet in its table, it performs **flooding** — sending the frame out every port except the one it arrived on. This is also what happens with broadcast frames (destination FF:FF:FF:FF:FF:FF). Flooding ensures delivery even without complete knowledge, at the cost of extra traffic. As devices respond and the switch observes their source addresses, the table fills in and subsequent frames are forwarded precisely. The process of receiving a frame and checking the table is called **filtering and forwarding**: if the destination port is known and different from the source port, forward; if the destination port equals the source port, drop (the destination is already on the same segment); if unknown, flood.

The practical impact of switching is dramatic. Each switch port becomes its own collision domain, meaning devices on different ports can transmit simultaneously without interfering. A 24-port switch effectively gives each connected device a dedicated link to the switch, and the switch's internal fabric can handle multiple simultaneous forwarding operations. This is why modern Ethernet networks can deliver full bandwidth to every port concurrently — a capability called **microsegmentation** — whereas a hub divided the total bandwidth among all devices. Understanding switching is foundational for the topics ahead: VLANs partition a single switch into multiple logical segments, and the Spanning Tree Protocol prevents loops when switches are interconnected.
