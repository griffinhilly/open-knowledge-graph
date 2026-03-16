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
status: draft
---

# Network Topologies and Architectures

## Core Idea
Network topologies describe how devices are physically or logically connected: bus, star, ring, mesh, tree, and hybrid topologies each have different fault tolerance, cost, and scalability characteristics. The choice of topology affects latency, bandwidth utilization, and resilience to component failures.

## How It's Best Learned
Draw out each topology, then trace how data flows and what happens if a link or node fails. Relate topologies to real networks (e.g., data centers use mesh, home networks are star).

## Common Misconceptions
- Physical and logical topologies are always the same; they can differ significantly (e.g., star physical topology with mesh logical topology).
- No single topology is universally best; choice depends on cost, reliability, and scalability requirements.

## Explainer

A network topology is the shape of how devices connect to each other — think of it as the blueprint of a network's wiring. The simplest way to understand topologies is to imagine a room full of computers and ask: if I had to run cables between them, what pattern would I use? Each pattern creates different tradeoffs in cost, speed, and what happens when something breaks.

In a **bus topology**, all devices share a single cable — like houses on one road. Data travels along the bus, and every device sees every message. It is cheap and simple but fragile: if the cable breaks anywhere, the entire network goes down. A **star topology** connects every device to a central hub or switch, the way spokes connect to the center of a wheel. If one cable fails, only that device loses connectivity — the rest keep working. Most home and office networks use a star topology because the central switch is inexpensive and the failure isolation is excellent. A **ring topology** passes data around a loop from device to device, like passing a note around a circle. Each device regenerates the signal, which extends range, but a single device failure can break the ring unless a dual-ring design provides redundancy.

A **mesh topology** connects every device directly to every other device (full mesh) or to several others (partial mesh). This provides the highest fault tolerance — multiple paths exist between any two points, so if one link fails, traffic reroutes automatically. Data centers and backbone networks use mesh designs because uptime is critical, even though the cabling cost grows rapidly. A **tree topology** arranges devices in a hierarchy, like a corporate org chart, combining star clusters connected by backbone links. Large campus networks often use trees because they mirror organizational structure and scale well.

The crucial insight is that **physical topology** and **logical topology** can differ. A network might look like a star physically — every cable runs to a central switch — but behave like a bus logically if the switch broadcasts every frame to all ports. Modern switched networks are physically star-shaped but logically provide point-to-point connections. Understanding this distinction prevents a common error: assuming that what you see in the wiring closet tells you everything about how data actually flows. When choosing a topology, the real question is always: what are the consequences when a component fails, how much does it cost to add another device, and does the design scale to the size I need?
