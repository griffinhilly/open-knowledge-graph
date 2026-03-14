---
id: spanning-tree-protocol-stp
title: Spanning Tree Protocol and Loop Prevention
domain: computer-science
course: computer-networking
prerequisites:
- id: ethernet-protocol
  type: hard
- id: switching-basics
  type: hard
- id: network-topologies
  type: soft
builds-toward:
- vlans-virtual-area-networks
- link-aggregation-control-protocol-lacp
tags:
- link-layer
- switching
- loop-prevention
- stp
stage: advanced
status: draft
---

# Spanning Tree Protocol and Loop Prevention

## Core Idea
Spanning Tree Protocol (STP, IEEE 802.1D) prevents broadcast storms in switched networks with redundant links by computing a loop-free spanning tree. Switches exchange Bridge Protocol Data Units (BPDUs) to elect a root bridge and calculate port roles (root, designated, blocked). Rapid Spanning Tree (RSTP, 802.1w) reduces convergence time from 30 seconds to under 1 second.

## How It's Best Learned
Build a test network with switch loops and observe STP convergence. Monitor BPDU exchanges using tcpdump and trace the spanning tree calculation. Trigger topology changes and measure convergence time for STP vs RSTP.

## Common Misconceptions
STP does not remove redundant links; it blocks them, keeping them as backup. All switches participate equally in STP; the root bridge is elected by bridge ID (priority + MAC). TCN (Topology Change Notification) is not broadcast; only the root generates TCA messages.
