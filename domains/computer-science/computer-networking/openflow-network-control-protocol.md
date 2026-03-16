---
id: openflow-network-control-protocol
title: OpenFlow and Network Control Plane
domain: computer-science
course: computer-networking
prerequisites:
- id: software-defined-networking
  type: hard
- id: network-topologies
  type: hard
builds-toward:
- network-function-virtualization-nfv
- network-management-and-monitoring
tags:
- sdn
- openflow
- control-plane
- switching
stage: advanced
status: draft
---

# OpenFlow and Network Control Plane

## Core Idea
OpenFlow decouples the control plane (routing decisions) from the data plane (packet forwarding) in network switches. A controller communicates with switches via OpenFlow protocol, installing flow entries that define how packets matching certain criteria (source IP, destination port, etc.) are forwarded. This enables dynamic, programmatic network control.

## How It's Best Learned
Deploy Mininet with Floodlight or ONOS controller to simulate OpenFlow networks. Write a simple OpenFlow controller that modifies flow tables. Monitor OpenFlow messages using Wireshark. Implement traffic engineering by dynamically adjusting flow priorities.

## Common Misconceptions
OpenFlow replaces the entire routing protocol stack; it does not, only the forwarding decision mechanism. OpenFlow switches require a controller; they do not function as traditional switches without one. OpenFlow is not a transport protocol; it runs over TCP.

## Explainer

In a traditional network, every switch and router contains both the brain (control plane) and the muscles (data plane). Each device independently decides where to send packets using its own routing tables, built by protocols like OSPF or BGP running locally. This means that to change network behavior — rerouting traffic, applying a security policy, or load balancing — you must reconfigure each device individually. **OpenFlow** eliminates this by giving all the decision-making authority to a single external controller, leaving switches as simple packet-forwarding devices that follow instructions.

The mechanism is straightforward. An OpenFlow switch maintains a **flow table** — a list of rules, each consisting of a match pattern, a set of actions, and counters. When a packet arrives, the switch checks the flow table for a matching entry. A match might specify criteria like "source IP is 10.0.0.5 and destination port is 80." If a match is found, the switch executes the associated actions: forward to port 3, drop the packet, modify a header field, or send it to another flow table for further processing. If no match is found, the switch sends the packet (or a summary of it) to the controller and asks what to do. The controller then installs a new flow entry so future matching packets are handled directly by the switch without controller involvement.

This architecture, which you know from studying SDN, creates a powerful separation of concerns. The **OpenFlow protocol** itself is the communication channel between controller and switches, running over a TCP connection (typically secured with TLS). The controller can proactively install flow entries before traffic arrives — for example, pre-programming paths for expected traffic patterns — or it can react to new flows as they appear. Messages flow in both directions: the controller sends flow modifications and configuration commands to switches, and switches send statistics, topology change notifications, and unmatched packet events back to the controller.

The practical power of OpenFlow becomes clear through examples. Consider a data center with hundreds of switches. Without OpenFlow, implementing a new security policy means logging into each switch and updating access control lists. With OpenFlow, the controller pushes updated flow entries to every affected switch simultaneously. Or consider traffic engineering: the controller can monitor link utilization across the entire network and dynamically reroute flows away from congested paths — something impossible when each switch makes routing decisions independently with only local visibility. The controller's global view of the network, combined with programmable flow entries, enables network behaviors that traditional distributed protocols cannot easily achieve.

One subtlety worth understanding is the relationship between flow granularity and controller load. Very fine-grained flow entries (matching on all header fields) give precise control but can overwhelm the controller with setup requests for every new connection. Very coarse entries (matching only on destination network) reduce controller involvement but sacrifice flexibility. Real deployments balance these tradeoffs, often using proactive rules for common traffic patterns and reactive rules for exceptional cases. OpenFlow version 1.3 and later support multiple flow tables in a pipeline, allowing switches to process packets through a sequence of matching stages — much like a series of filters — which makes complex policies practical without explosion in table size.
