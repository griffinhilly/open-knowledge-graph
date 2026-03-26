---
id: network-topologies
title: Network Topologies and Architectures
domain: computer-science
course: computer-networking
prerequisites: []
builds-toward:
- switching-basics
- routing-algorithms-overview
tags:
- topology
- architecture
- network-design
- graph-structure
stage: advanced
status: validated
---

# Network Topologies and Architectures

## Core Idea
Network topologies describe how devices are physically or logically connected: bus, star, ring, mesh, tree, and hybrid topologies each have different fault tolerance, cost, and scalability characteristics. The choice of topology affects latency, bandwidth utilization, and resilience to component failures.

## How It's Best Learned
Draw out each topology, then trace how data flows and what happens if a link or node fails. Relate topologies to real networks (e.g., data centers use mesh, home networks are star).

## Common Misconceptions
- Physical and logical topologies are always the same; they can differ significantly (e.g., star physical topology with mesh logical topology).
- No single topology is universally best; choice depends on cost, reliability, and scalability requirements.

## Questions

```yaml
- question: "In a company's network, every device is cabled to a central switch. One cable between a workstation and the switch is accidentally cut. What is the impact?"
  type: multiple-choice
  options:
    - "The entire network goes down because the central node is disrupted"
    - "Only the device connected by that cable loses network access"
    - "All devices experience degraded performance until the cable is replaced"
    - "Traffic is automatically rerouted through other devices"
  answer: 1
  explanation: "A star topology isolates failures to the individual link — only the device connected by the severed cable loses access. The central switch continues operating normally and all other devices remain connected. This fault isolation is one of the main reasons star topology dominates home and office networks. Compare this to a bus topology where a cable break anywhere takes down all devices, or a mesh topology where traffic could reroute — but star topology has no rerouting, just isolation."

- question: "A network administrator draws a diagram showing every device connected to a central switch (physical star). She then observes that the switch forwards every incoming frame out all ports simultaneously. What is the logical topology of this network?"
  type: multiple-choice
  options:
    - "Star — because the physical layout determines the logical layout"
    - "Bus — because all devices receive every frame, just like a shared cable"
    - "Mesh — because the switch connects to all devices at once"
    - "Ring — because frames circulate through all devices before returning"
  answer: 1
  explanation: "Physical and logical topologies can differ significantly. The physical layout (star wiring to a hub/switch) does not determine the logical data flow. A hub that broadcasts every frame to all ports creates bus-like logical behavior — every device sees every message, just as in a physical bus. A modern *switch* (which sends frames only to the destination port) creates a logical point-to-point topology despite the same physical star wiring. This distinction is the key insight: what you see in the wiring closet does not necessarily tell you how data actually flows."

- question: "In a full mesh topology, if a single link between two nodes fails, communication between those nodes becomes very difficult."
  type: true-false
  answer: false
  explanation: "In a full mesh topology, every node has a direct connection to every other node, meaning multiple paths exist between any pair. If one link fails, traffic can be rerouted through intermediate nodes. This is precisely why mesh topologies are used in high-availability data centers and backbone networks — fault tolerance is built into the redundant paths. The statement describes what would happen in a bus or star topology, not a mesh."

- question: "A star topology concentrates fault risk at the central hub or switch, making it a single point of failure for the entire network."
  type: true-false
  answer: true
  explanation: "This is a genuine and important limitation of star topology. While a star isolates individual cable failures (only one device goes offline), failure of the central hub or switch takes down the entire network simultaneously. This is the classic 'single point of failure' tradeoff that network designers must weigh against star topology's advantages of easy management, fault isolation per node, and low cable cost. Redundant switches or failover designs are used in critical environments to address this."

- question: "Why can physical and logical topologies differ, and why does this distinction matter for understanding network behavior?"
  type: short-answer
  answer: "Physical topology describes how cables are physically laid out; logical topology describes how data actually flows between devices. They differ because network equipment like switches and hubs impose their own forwarding behavior on top of the physical wiring. A star-wired network using a hub behaves logically like a bus (all devices share bandwidth, every frame is broadcast to all); a star-wired network using a modern switch behaves like a mesh of point-to-point links (each frame goes only to its destination). The distinction matters because performance, security, and congestion behavior all depend on the logical topology — the physical wiring plan alone is insufficient to understand or troubleshoot how a network actually performs."
  explanation: "Administrators who only think about physical topology will misdiagnose network problems. Broadcast storms, collisions, and security vulnerabilities all depend on logical topology. Modern Ethernet switched networks are physically star-shaped but logically very different from the hub-based networks they replaced — understanding this was a major practical insight in network evolution."
```

## Explainer

A network topology is the shape of how devices connect to each other — think of it as the blueprint of a network's wiring. The simplest way to understand topologies is to imagine a room full of computers and ask: if I had to run cables between them, what pattern would I use? Each pattern creates different tradeoffs in cost, speed, and what happens when something breaks.

In a **bus topology**, all devices share a single cable — like houses on one road. Data travels along the bus, and every device sees every message. It is cheap and simple but fragile: if the cable breaks anywhere, the entire network goes down. A **star topology** connects every device to a central hub or switch, the way spokes connect to the center of a wheel. If one cable fails, only that device loses connectivity — the rest keep working. Most home and office networks use a star topology because the central switch is inexpensive and the failure isolation is excellent. A **ring topology** passes data around a loop from device to device, like passing a note around a circle. Each device regenerates the signal, which extends range, but a single device failure can break the ring unless a dual-ring design provides redundancy.

A **mesh topology** connects every device directly to every other device (full mesh) or to several others (partial mesh). This provides the highest fault tolerance — multiple paths exist between any two points, so if one link fails, traffic reroutes automatically. Data centers and backbone networks use mesh designs because uptime is critical, even though the cabling cost grows rapidly. A **tree topology** arranges devices in a hierarchy, like a corporate org chart, combining star clusters connected by backbone links. Large campus networks often use trees because they mirror organizational structure and scale well.

The crucial insight is that **physical topology** and **logical topology** can differ. A network might look like a star physically — every cable runs to a central switch — but behave like a bus logically if the switch broadcasts every frame to all ports. Modern switched networks are physically star-shaped but logically provide point-to-point connections. Understanding this distinction prevents a common error: assuming that what you see in the wiring closet tells you everything about how data actually flows. When choosing a topology, the real question is always: what are the consequences when a component fails, how much does it cost to add another device, and does the design scale to the size I need?
