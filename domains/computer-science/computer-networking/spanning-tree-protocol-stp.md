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

## Explainer

From your study of Ethernet and switching, you know that switches forward frames based on MAC address tables and that they flood frames when the destination is unknown. Now consider what happens when you add redundant links between switches for reliability — a frame that gets flooded will travel the loop forever, multiplying with each pass. Within seconds, these **broadcast storms** consume all bandwidth and crash the network. Spanning Tree Protocol exists to prevent this by logically disabling just enough links to eliminate all loops while keeping the network connected.

STP works by electing a single **root bridge** — the switch with the lowest bridge ID (a combination of a configurable priority value and the switch's MAC address). Every other switch then calculates the shortest path to the root bridge using path cost, which is inversely related to link speed. Each switch identifies one **root port** — the port with the lowest cost path to the root. On each network segment, one switch's port is designated as the **designated port** (the one offering the best path to the root for that segment), and all other ports connecting to that segment are placed in a **blocked state**. Blocked ports do not forward traffic but continue listening for BPDUs, ready to activate if the topology changes.

The protocol communicates through **Bridge Protocol Data Units** (BPDUs) — small frames that switches exchange to announce their identity, their root bridge claim, and their path cost to the root. When a switch first connects, or when a link fails, the switches re-exchange BPDUs and recalculate the spanning tree. In classic STP (802.1D), this reconvergence takes 30 to 50 seconds as ports transition through listening and learning states before forwarding — an eternity for modern networks. **Rapid Spanning Tree Protocol** (RSTP, 802.1w) dramatically improves this by introducing proposal-agreement handshakes between directly connected switches, allowing ports to transition to forwarding in under a second.

Think of STP as a network-wide consensus algorithm: every switch agrees on who the root is, calculates its own best path, and cooperatively blocks redundant paths. The blocked links are not wasted — they are standing by as backups. If an active link fails, the blocked port detecting the change can transition to forwarding, restoring connectivity. This gives you the reliability benefit of redundant physical links without the catastrophic failure mode of Layer 2 loops. The tradeoff is that blocked links carry zero traffic during normal operation, which is why more advanced techniques like link aggregation (LACP) and per-VLAN spanning tree eventually supplement or replace basic STP in larger networks.
