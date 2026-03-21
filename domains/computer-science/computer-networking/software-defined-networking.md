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

## Questions

```yaml
- question: "A network administrator needs to implement a quality-of-service policy that prioritizes video conferencing traffic over bulk file transfers, applying consistently across all 500 switches in a data center. How does this differ between traditional networking and SDN?"
  type: multiple-choice
  options:
    - "In traditional networking, the administrator updates one central router; in SDN, each switch must be configured individually."
    - "In traditional networking, each switch must be configured individually; in SDN, the controller installs updated forwarding rules to all switches centrally."
    - "In both approaches, the change propagates automatically — traditional routing protocols handle this via distributed consensus."
    - "In SDN, the change is impossible because switches only make binary forward/drop decisions, not priority-based ones."
  answer: 1
  explanation: "This is the core practical advantage of SDN. In traditional networking, each switch runs its own routing logic — implementing a consistent network-wide policy requires logging into each device and modifying its configuration individually, an error-prone and slow process across hundreds of devices. In SDN, the controller has a global view and installs rules in all switch flow tables simultaneously through the southbound interface (e.g., OpenFlow). What would take hours of manual configuration in a traditional network takes seconds via the SDN controller."

- question: "A production SDN deployment uses three geographically distributed controller instances. What architectural concern motivates this design choice?"
  type: multiple-choice
  options:
    - "Three controllers allow parallel processing, tripling the throughput of flow rule installations."
    - "Distributed controllers provide geographic locality, reducing latency between controller and switches."
    - "The centralized controller is a single point of failure — if it fails, new flows cannot be handled. Clustering provides fault tolerance."
    - "Three controllers are required by the OpenFlow protocol, which mandates a minimum of three instances for quorum-based decision making."
  answer: 2
  explanation: "SDN's centralization is also its main architectural risk. If the single controller fails, switches continue forwarding existing cached flows but cannot handle new flows or policy updates. Production deployments use controller clustering with failover so that if one controller instance goes down, others take over. This is the fundamental tradeoff of SDN: centralization enables powerful global optimization but creates a critical point of failure that distributed architectures — where failure of one router doesn't affect others — inherently avoid."

- question: "In an SDN architecture, the OpenFlow protocol allows the controller to remotely install and update forwarding rules in switch flow tables."
  type: true-false
  answer: true
  explanation: "OpenFlow is the southbound API — the protocol through which the controller communicates with switches. Using OpenFlow, the controller installs match-action rules in the switch's flow table: 'if packet destination is 10.0.0.5, forward out port 3.' Switches report events (new flows, link failures, statistics) back to the controller. This protocol is what makes switches programmable forwarding devices rather than autonomous decision-makers — the entire SDN architecture rests on this well-defined control-data plane interface."

- question: "In an SDN network, each switch continues to run distributed routing algorithms locally and makes its own forwarding decisions, but reports its decisions to the controller for monitoring."
  type: true-false
  answer: false
  explanation: "This inverts the SDN architecture. In SDN, switches are simple forwarding devices — they execute rules installed by the controller, they do not run routing algorithms. The intelligence (control plane) has been entirely removed from the switches and placed in the controller. Switches match incoming packets against their flow tables and forward accordingly; if no rule matches, they ask the controller. Traditional distributed routing (where each switch runs OSPF or BGP locally) is precisely what SDN replaces."

- question: "What is the fundamental advantage of the SDN controller's global network view over the distributed routing protocols used in traditional networking?"
  type: short-answer
  answer: "Distributed routing protocols make locally optimal decisions based on what each node can observe — they cannot optimize across the entire network simultaneously. The controller sees all links, all traffic loads, and all device states at once, enabling globally optimal decisions: routing around congestion, balancing load across multiple paths, enforcing consistent policies, and responding to failures in a coordinated way that no individual router with only a local view can achieve."
  explanation: "The traffic management analogy illustrates this: a central operations center seeing all intersections simultaneously can optimize across the whole city, while individual officers can only see their own corner. Distributed routing protocols converge on a consistent topology view eventually, but the view is aggregated topology, not real-time traffic. The controller's global, real-time view is what enables sophisticated traffic engineering — like Google and Microsoft's data center management — that would be impractical in traditional distributed architectures."
```

## Explainer

In a conventional network, every router and switch is an independent decision-maker. Each device runs routing algorithms locally, builds its own forwarding tables, and acts autonomously. If you want to change how traffic flows — say, to reroute around a congested link — you must log into each affected device and update its configuration individually. For a network with hundreds or thousands of devices, this is slow, error-prone, and makes coordinated network-wide policies extremely difficult to implement. **Software-Defined Networking (SDN)** addresses this by separating the network's brain from its body.

The key architectural insight is the split between two planes. The **control plane** is where routing decisions are made — which path should a packet take, should it be allowed through, how should it be prioritized? The **data plane** (or forwarding plane) is the mechanical act of moving packets from input port to output port according to rules. In traditional networking, both planes exist together inside each device. SDN pulls the control plane out of individual switches and centralizes it in a **controller** — a software application running on a standard server. Switches become simple forwarding devices that receive rules from the controller and execute them. You already know from studying network topologies how devices are interconnected; SDN lets you manage all those interconnections from a single logical point.

Think of the difference like this: a traditional network is like a city where every intersection has a local traffic officer making independent decisions. SDN is like having a central traffic management system with cameras at every intersection, where a single operations center decides all signal timings and reroutes based on a global view of congestion. The central system can optimize across the entire city in ways that individual officers, who can only see their own intersection, simply cannot. This **global network view** is SDN's fundamental advantage — the controller sees all links, all traffic, and all devices simultaneously, enabling optimizations that distributed protocols struggle to achieve.

The controller communicates with switches through a well-defined protocol interface — most commonly **OpenFlow**, though alternatives like P4 and gRPC-based interfaces exist. Through this interface, the controller installs forwarding rules in switch flow tables, and switches report events (new traffic flows, link failures, statistics) back to the controller. Above the controller, applications interact through a **northbound API**, requesting network services like "create an isolated network segment" or "prioritize video traffic." This three-layer architecture — applications, controller, and switches — makes the network programmable in the same way that operating systems made computers programmable: by providing abstractions that hide hardware complexity.

SDN's practical impact is most visible in large data centers, where cloud providers like Google and Microsoft use it to manage tens of thousands of switches. SDN enables network slicing (carving a physical network into isolated virtual networks for different tenants), rapid provisioning (spinning up network connectivity for new virtual machines in seconds rather than days), and automated traffic engineering (dynamically shifting traffic patterns based on real-time demand). The tradeoff is that the centralized controller becomes a critical point of failure, which production deployments address through controller clustering and failover — but the simplicity and programmability of the centralized model has made SDN the dominant architecture for modern large-scale networks.
