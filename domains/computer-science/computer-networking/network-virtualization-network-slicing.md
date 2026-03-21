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

## Questions

```yaml
- question: "A hospital runs remote surgery traffic on a dedicated network slice with guaranteed sub-millisecond latency. A streaming service runs on a separate slice on the same physical 5G infrastructure. During peak streaming hours, video traffic surges to maximum capacity. What happens to the surgery slice?"
  type: multiple-choice
  options:
    - "Surgery traffic experiences degraded latency because both slices share the same physical links"
    - "The surgery slice is unaffected — resource isolation means slices cannot steal capacity from each other"
    - "The network operator must provision additional physical hardware for the surgery slice"
    - "The streaming slice is automatically throttled by the hospital's IT department"
  answer: 1
  explanation: "Resource isolation is the defining property of network slicing. Each slice is allocated a guaranteed pool of bandwidth, buffer memory, and processing capacity that other slices cannot consume. A traffic surge on the streaming slice uses only the resources reserved for that slice; the surgery slice's reserved resources remain available and its SLA guarantees hold. This is precisely why slicing was developed — to provide dedicated-network guarantees on shared infrastructure."

- question: "Which combination of capabilities is required to implement a network slice on shared physical infrastructure?"
  type: multiple-choice
  options:
    - "Resource partitioning, traffic isolation, and programmable control"
    - "Dedicated physical switches, VLAN tagging, and bandwidth throttling"
    - "Traffic encryption, static routing tables, and hardware redundancy"
    - "Software-defined networking alone is sufficient to create isolated slices"
  answer: 0
  explanation: "Building a network slice requires all three ingredients working together: resource partitioning divides physical capacity (CPU, bandwidth, buffers) into reserved pools per slice; traffic isolation ensures packets belonging to one slice are processed only by that slice's forwarding rules (via tags, tunnels, or separate flow tables); and programmable control lets each slice be independently configured as if it were a dedicated network. SDN provides the control plane programmability but cannot alone create resource isolation — you also need the partitioning and isolation layers."

- question: "Network slicing enables a single physical infrastructure to simultaneously support applications with radically different latency and throughput requirements by isolating their allocated resources."
  type: true-false
  answer: true
  explanation: "This is exactly the value proposition of network slicing. A 5G network must serve autonomous vehicles (requiring sub-millisecond latency and near-zero packet loss), IoT sensors (tiny data bursts, relaxed latency), and video streaming (high throughput, flexible latency) — all with incompatible SLA requirements. Slicing creates independent virtual networks, each configured and allocated resources to match its application's requirements, running simultaneously on shared hardware without interfering with each other."

- question: "Network slices require dedicated physical hardware for each tenant; they cannot function on shared switches and links."
  type: true-false
  answer: false
  explanation: "Network slicing is specifically designed to virtualize shared physical infrastructure. The entire point is that multiple logical networks run on the same cables, switches, and servers through software-defined partitioning and isolation — not physical separation. Requiring dedicated hardware per tenant would eliminate the economic rationale for slicing. Isolation is achieved through software mechanisms (flow tables, tunnels, resource allocation policies), not by dedicating physical resources to each slice."

- question: "What problem does network slicing solve in 5G networks, and why wasn't deploying separate physical networks for each application type a viable solution?"
  type: short-answer
  answer: "5G must simultaneously serve applications with incompatible requirements: autonomous vehicles need guaranteed sub-millisecond latency, IoT sensors need massive device connectivity with tiny data bursts, and smartphones need high throughput for streaming. These requirements cannot all be optimized by a single monolithic network configuration. Separate physical networks would require duplicating all infrastructure (towers, cables, core equipment) for each use case — economically impractical at 5G scale. Network slicing solves this by creating logically isolated virtual networks with tailored configurations on shared physical infrastructure, giving each application type a customized network while splitting the infrastructure cost across all use cases."
  explanation: "The economic argument is central: 5G infrastructure is enormously expensive to build and operate. Requiring separate physical infrastructure for each service type would multiply those costs several times over, making the business case impossible. Network slicing is the technical innovation that makes one physical deployment economically serve the full breadth of 5G use cases — what operators call 'network as a service.'"
```

## Explainer

From your work with software-defined networking, you know that decoupling the control plane from the data plane lets a centralized controller program forwarding behavior across an entire network. Network virtualization takes that programmability a step further: instead of running one logical network on the physical infrastructure, you run many. Think of it like virtual machines for networks — the same physical switches, links, and servers host multiple independent networks that cannot see or interfere with each other, even though they share the same cables and hardware.

The key abstraction is **network slicing**. A slice is a logically isolated end-to-end virtual network carved from shared physical resources. Each slice gets its own topology, its own forwarding rules, its own allocated bandwidth, and its own quality-of-service guarantees. A hospital might run one slice for ultra-reliable remote surgery traffic (demanding sub-millisecond latency and near-zero packet loss) while a streaming service runs another slice on the same infrastructure optimized for high throughput with relaxed latency requirements. Neither slice is aware the other exists, and a traffic surge on the streaming slice cannot starve the surgical slice of resources.

Building a slice requires three ingredients you have already encountered in SDN. First, **resource partitioning** divides physical capacity — CPU cycles on switches, link bandwidth, buffer memory — into pools assigned to each slice. Second, **traffic isolation** ensures that packets belonging to one slice are processed only by that slice's forwarding rules, typically using tags, tunnels, or separate flow tables. Third, **programmable control** lets the slice owner configure routing, security policies, and monitoring independently, as if they owned a dedicated physical network. The SDN controller orchestrates all of this, translating high-level slice definitions into low-level forwarding instructions installed on shared hardware.

Network slicing became essential with **5G** because a single cellular network must simultaneously serve wildly different applications: autonomous vehicles needing guaranteed low latency, IoT sensors sending tiny bursts of data, and smartphones streaming video. Without slicing, you would need separate physical networks for each use case — economically impractical. With slicing, a single infrastructure flexibly serves all of them, each application type getting a tailored virtual network. The operator defines slices through templates specifying bandwidth, latency, reliability, and mobility requirements, and the SDN/NFV stack instantiates and manages them dynamically. This is why slicing is considered the defining architectural innovation of modern carrier networks.
