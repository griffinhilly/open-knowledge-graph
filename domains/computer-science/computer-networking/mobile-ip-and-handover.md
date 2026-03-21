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

## Questions

```yaml
- question: "A laptop has an active TCP connection to a server. The user moves to a different WiFi network, and the laptop gets a new IP address. Why does the TCP connection break, even though both networks are working correctly?"
  type: multiple-choice
  options:
    - "TCP connections break whenever the physical link layer changes, regardless of whether the IP address changes"
    - "The new network uses a different MTU, causing packet fragmentation that terminates the connection"
    - "TCP connections are bound to IP address pairs; when the laptop's IP changes, the server cannot route responses to the new address, and the connection state referencing the old IP becomes invalid"
    - "TCP does not support user mobility and requires a new three-way handshake whenever a user roams to any new location"
  answer: 2
  explanation: "This is the fundamental tension that Mobile IP solves: IP addresses serve dual purposes as both host identifiers and location descriptors. TCP connections are defined by four-tuples (source IP, source port, destination IP, destination port). When the source IP changes because a host moves, the server still sends responses to the old IP, which is now on a different subnet — packets are misrouted or undeliverable, and the connection breaks. Mobile IP solves this by keeping the home address constant while routing through the care-of address."

- question: "In Mobile IP, a remote host sends a packet to the mobile node's home address while the node is visiting a foreign network. The home agent tunnels the packet to the care-of address. What problem does this triangle routing create?"
  type: multiple-choice
  options:
    - "The packet is delivered twice — once directly and once via the tunnel — causing duplicate processing"
    - "Triangle routing forces the packet to travel via the home network even if the remote host is geographically close to the foreign network, wasting bandwidth and adding latency"
    - "The home agent cannot distinguish the tunnel header from the original packet, causing header corruption"
    - "IP-in-IP tunneling is incompatible with wireless links, so the tunnel fails on any mobile network"
  answer: 1
  explanation: "Triangle routing is Mobile IP's main performance drawback. If a mobile node is in Tokyo and its home network is in New York, every packet from a San Francisco host must travel to New York, get tunneled, and travel back to Tokyo — a massive detour. Route optimization addresses this by allowing the remote host to learn the care-of address directly and send packets straight to the foreign network, eliminating the home-agent detour after the first exchange."

- question: "The main architectural advantage of Mobile IPv6 over Mobile IPv4 is that it integrates mobility support directly into the protocol, eliminating the need for separate foreign agents."
  type: true-false
  answer: true
  explanation: "Mobile IPv6 leverages built-in IPv6 features — neighbor discovery, address autoconfiguration, and mandatory IPsec support — to implement mobility without requiring foreign agents on every visited network. The mobile node can form a care-of address directly using stateless address autoconfiguration and register it with its home agent using binding update messages. This simplifies deployment significantly compared to Mobile IPv4, which requires foreign agent infrastructure at every foreign network."

- question: "In soft handover, the mobile device disconnects from the old access point before establishing a connection to the new one, ensuring a clean single-connection transition."
  type: true-false
  answer: false
  explanation: "This describes hard handover, not soft. In soft handover, the device communicates with both the old and new access points simultaneously during the transition period, then drops the old connection once the new one is stable. This eliminates the gap that would otherwise cause dropped packets or interrupted calls. Cellular networks like LTE implement soft handover at the radio layer through base station coordination. WiFi typically uses hard handover because access points operate independently without coordination mechanisms."

- question: "Explain why IP routing creates a fundamental problem for mobile devices, and how Mobile IP's home agent / care-of address architecture solves it."
  type: short-answer
  answer: "IP addresses encode both host identity and network location — routers use the address prefix to determine which subnet a packet should be delivered to. When a device moves and joins a new subnet, it must get a new address, which breaks any existing connections bound to the old address. Mobile IP solves this by letting the device keep its permanent home address (identity) while using a care-of address (location) on the foreign network. The home agent intercepts packets sent to the home address and tunnels them to the care-of address, decoupling identity from location."
  explanation: "The core insight is that the dual role of IP addresses — identity and location — is not a bug but a feature exploited by routing. Mobile IP adds an indirection layer: the home agent maintains the mapping from permanent identity to current location, and tunneling bridges the two. This allows the rest of the network to continue routing based on the home address as if the device never moved, while the tunneling mechanism handles the actual delivery to wherever the device currently is."
```

## Explainer

From IP routing, you know that an IP address serves two purposes simultaneously: it **identifies** a host and it **locates** that host within the network topology. Routers use the network prefix of an IP address to forward packets toward the correct subnet. This works beautifully for stationary hosts, but it creates a fundamental problem for mobile devices. When a laptop moves from a coffee shop's WiFi to a university's network, it gets a new IP address on the new subnet. Any existing TCP connections — bound to the old IP address — break immediately. **Mobile IP** solves this by decoupling identity from location, allowing a device to keep its original IP address while physically moving between networks.

The Mobile IP architecture introduces three key entities. The **mobile node** is the device that moves. The **home agent** is a router on the mobile node's original (home) network that acts as an anchor point. The **foreign agent** is a router on the network the mobile node is currently visiting. When the mobile node moves to a foreign network, it registers its current location — its **care-of address** on the foreign network — with its home agent. Now, when a remote host sends a packet to the mobile node's permanent (home) IP address, the packet arrives at the home network via normal routing. The home agent intercepts it, wraps it in a new IP header addressed to the care-of address (**IP-in-IP tunneling**), and forwards it to the foreign agent, which strips the tunnel header and delivers the original packet to the mobile node. Outbound packets from the mobile node can go directly to the destination, creating an asymmetric routing path known as **triangle routing**.

**Handover** (or handoff) is the process of transferring the mobile node's active connection from one access point or network to another. The challenge is speed: if a VoIP call is in progress, the handover must complete in tens of milliseconds to avoid audible gaps. Handovers are classified as **hard** (the old connection is broken before the new one is established, causing a brief interruption) or **soft** (the device communicates with both the old and new access points simultaneously during the transition, then drops the old one). Cellular networks like LTE implement soft handovers at the radio layer — the base stations coordinate so the device is never disconnected. WiFi handovers are harder because 802.11 access points typically operate independently, requiring the device to scan for a new AP, authenticate, and associate before traffic can flow.

Several optimizations address Mobile IP's limitations. **Route optimization** allows the remote host to learn the mobile node's care-of address directly, sending packets straight to the foreign network instead of triangle-routing through the home agent. **Hierarchical Mobile IP** reduces handover latency by using local mobility anchors within a region, so a short-distance move only requires local re-registration rather than contacting the distant home agent. **Mobile IPv6** integrates mobility support directly into the IPv6 protocol, using features like neighbor discovery and IPsec to simplify the architecture and eliminate the need for separate foreign agents. These refinements reflect a broader trend: as wireless connectivity becomes the norm rather than the exception, mobility support is moving from an overlay protocol to a fundamental part of the network architecture.
