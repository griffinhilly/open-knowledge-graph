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
