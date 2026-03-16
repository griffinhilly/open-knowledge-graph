---
id: network-virtualization-network-slicing
title: Network Virtualization and Network Slicing
domain: computer-science
course: computer-networking
prerequisites:
- id: software-defined-networking
  type: hard
tags:
- network-virtualization
- slicing
- multi-tenancy
- resource-isolation
stage: advanced
status: draft
---

# Network Virtualization and Network Slicing

## Core Idea
Network slicing partitions shared physical infrastructure into independent virtual networks with isolated resources and customized behavior, allowing multiple tenants or applications to coexist. Slicing combines SDN, NFV, and other technologies to enable flexible allocation of bandwidth, latency, and other network properties. Slicing is critical for 5G networks supporting diverse service requirements.

## Explainer

From your work with software-defined networking, you know that decoupling the control plane from the data plane lets a centralized controller program forwarding behavior across an entire network. Network virtualization takes that programmability a step further: instead of running one logical network on the physical infrastructure, you run many. Think of it like virtual machines for networks — the same physical switches, links, and servers host multiple independent networks that cannot see or interfere with each other, even though they share the same cables and hardware.

The key abstraction is **network slicing**. A slice is a logically isolated end-to-end virtual network carved from shared physical resources. Each slice gets its own topology, its own forwarding rules, its own allocated bandwidth, and its own quality-of-service guarantees. A hospital might run one slice for ultra-reliable remote surgery traffic (demanding sub-millisecond latency and near-zero packet loss) while a streaming service runs another slice on the same infrastructure optimized for high throughput with relaxed latency requirements. Neither slice is aware the other exists, and a traffic surge on the streaming slice cannot starve the surgical slice of resources.

Building a slice requires three ingredients you have already encountered in SDN. First, **resource partitioning** divides physical capacity — CPU cycles on switches, link bandwidth, buffer memory — into pools assigned to each slice. Second, **traffic isolation** ensures that packets belonging to one slice are processed only by that slice's forwarding rules, typically using tags, tunnels, or separate flow tables. Third, **programmable control** lets the slice owner configure routing, security policies, and monitoring independently, as if they owned a dedicated physical network. The SDN controller orchestrates all of this, translating high-level slice definitions into low-level forwarding instructions installed on shared hardware.

Network slicing became essential with **5G** because a single cellular network must simultaneously serve wildly different applications: autonomous vehicles needing guaranteed low latency, IoT sensors sending tiny bursts of data, and smartphones streaming video. Without slicing, you would need separate physical networks for each use case — economically impractical. With slicing, a single infrastructure flexibly serves all of them, each application type getting a tailored virtual network. The operator defines slices through templates specifying bandwidth, latency, reliability, and mobility requirements, and the SDN/NFV stack instantiates and manages them dynamically. This is why slicing is considered the defining architectural innovation of modern carrier networks.
