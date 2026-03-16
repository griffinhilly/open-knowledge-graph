---
id: software-defined-networking
title: Software-Defined Networking (SDN)
domain: computer-science
course: computer-networking
prerequisites:
- id: network-topologies
  type: hard
- id: routing-algorithms-overview
  type: hard
builds-toward:
- network-virtualization-network-slicing
tags:
- sdn
- openflow
- control-plane
- data-plane
stage: advanced
status: draft
---

# Software-Defined Networking (SDN)

## Core Idea
SDN decouples the control plane (routing decisions) from the data plane (packet forwarding) by centralizing control in a logically centralized controller. Switches become simple forwarding devices following controller-installed rules, enabling dynamic network reconfiguration and simplified management. OpenFlow is the most widely deployed protocol for controller-switch communication.

## Explainer

In a conventional network, every router and switch is an independent decision-maker. Each device runs routing algorithms locally, builds its own forwarding tables, and acts autonomously. If you want to change how traffic flows — say, to reroute around a congested link — you must log into each affected device and update its configuration individually. For a network with hundreds or thousands of devices, this is slow, error-prone, and makes coordinated network-wide policies extremely difficult to implement. **Software-Defined Networking (SDN)** addresses this by separating the network's brain from its body.

The key architectural insight is the split between two planes. The **control plane** is where routing decisions are made — which path should a packet take, should it be allowed through, how should it be prioritized? The **data plane** (or forwarding plane) is the mechanical act of moving packets from input port to output port according to rules. In traditional networking, both planes exist together inside each device. SDN pulls the control plane out of individual switches and centralizes it in a **controller** — a software application running on a standard server. Switches become simple forwarding devices that receive rules from the controller and execute them. You already know from studying network topologies how devices are interconnected; SDN lets you manage all those interconnections from a single logical point.

Think of the difference like this: a traditional network is like a city where every intersection has a local traffic officer making independent decisions. SDN is like having a central traffic management system with cameras at every intersection, where a single operations center decides all signal timings and reroutes based on a global view of congestion. The central system can optimize across the entire city in ways that individual officers, who can only see their own intersection, simply cannot. This **global network view** is SDN's fundamental advantage — the controller sees all links, all traffic, and all devices simultaneously, enabling optimizations that distributed protocols struggle to achieve.

The controller communicates with switches through a well-defined protocol interface — most commonly **OpenFlow**, though alternatives like P4 and gRPC-based interfaces exist. Through this interface, the controller installs forwarding rules in switch flow tables, and switches report events (new traffic flows, link failures, statistics) back to the controller. Above the controller, applications interact through a **northbound API**, requesting network services like "create an isolated network segment" or "prioritize video traffic." This three-layer architecture — applications, controller, and switches — makes the network programmable in the same way that operating systems made computers programmable: by providing abstractions that hide hardware complexity.

SDN's practical impact is most visible in large data centers, where cloud providers like Google and Microsoft use it to manage tens of thousands of switches. SDN enables network slicing (carving a physical network into isolated virtual networks for different tenants), rapid provisioning (spinning up network connectivity for new virtual machines in seconds rather than days), and automated traffic engineering (dynamically shifting traffic patterns based on real-time demand). The tradeoff is that the centralized controller becomes a critical point of failure, which production deployments address through controller clustering and failover — but the simplicity and programmability of the centralized model has made SDN the dominant architecture for modern large-scale networks.
