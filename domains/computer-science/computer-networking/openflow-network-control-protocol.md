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
