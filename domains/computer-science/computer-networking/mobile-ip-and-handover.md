---
id: mobile-ip-and-handover
title: Mobile IP and Handover
domain: computer-science
course: computer-networking
prerequisites:
- id: ip-routing-basics
  type: hard
- id: wireless-networking-802-11
  type: hard
tags:
- mobile-ip
- handover
- mobility
- seamless-roaming
stage: advanced
status: draft
---

# Mobile IP and Handover

## Core Idea
Mobile IP allows a mobile device to maintain connectivity while moving between networks by using a home agent to intercept and forward traffic to the device's current location. Handover—transitioning from one access point or network to another—must be fast enough to maintain active connections. Cellular networks embed mobility support; WiFi requires higher-layer solutions like Mobile IP.

## Explainer

From IP routing, you know that an IP address serves two purposes simultaneously: it **identifies** a host and it **locates** that host within the network topology. Routers use the network prefix of an IP address to forward packets toward the correct subnet. This works beautifully for stationary hosts, but it creates a fundamental problem for mobile devices. When a laptop moves from a coffee shop's WiFi to a university's network, it gets a new IP address on the new subnet. Any existing TCP connections — bound to the old IP address — break immediately. **Mobile IP** solves this by decoupling identity from location, allowing a device to keep its original IP address while physically moving between networks.

The Mobile IP architecture introduces three key entities. The **mobile node** is the device that moves. The **home agent** is a router on the mobile node's original (home) network that acts as an anchor point. The **foreign agent** is a router on the network the mobile node is currently visiting. When the mobile node moves to a foreign network, it registers its current location — its **care-of address** on the foreign network — with its home agent. Now, when a remote host sends a packet to the mobile node's permanent (home) IP address, the packet arrives at the home network via normal routing. The home agent intercepts it, wraps it in a new IP header addressed to the care-of address (**IP-in-IP tunneling**), and forwards it to the foreign agent, which strips the tunnel header and delivers the original packet to the mobile node. Outbound packets from the mobile node can go directly to the destination, creating an asymmetric routing path known as **triangle routing**.

**Handover** (or handoff) is the process of transferring the mobile node's active connection from one access point or network to another. The challenge is speed: if a VoIP call is in progress, the handover must complete in tens of milliseconds to avoid audible gaps. Handovers are classified as **hard** (the old connection is broken before the new one is established, causing a brief interruption) or **soft** (the device communicates with both the old and new access points simultaneously during the transition, then drops the old one). Cellular networks like LTE implement soft handovers at the radio layer — the base stations coordinate so the device is never disconnected. WiFi handovers are harder because 802.11 access points typically operate independently, requiring the device to scan for a new AP, authenticate, and associate before traffic can flow.

Several optimizations address Mobile IP's limitations. **Route optimization** allows the remote host to learn the mobile node's care-of address directly, sending packets straight to the foreign network instead of triangle-routing through the home agent. **Hierarchical Mobile IP** reduces handover latency by using local mobility anchors within a region, so a short-distance move only requires local re-registration rather than contacting the distant home agent. **Mobile IPv6** integrates mobility support directly into the IPv6 protocol, using features like neighbor discovery and IPsec to simplify the architecture and eliminate the need for separate foreign agents. These refinements reflect a broader trend: as wireless connectivity becomes the norm rather than the exception, mobility support is moving from an overlay protocol to a fundamental part of the network architecture.
