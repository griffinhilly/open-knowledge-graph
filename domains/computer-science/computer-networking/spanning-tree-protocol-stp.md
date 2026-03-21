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

## Questions

```yaml
- question: "A network admin wants Switch A to always be elected as the root bridge. Switch A currently has the default bridge priority. What is the correct action?"
  type: multiple-choice
  options:
    - "Give Switch A the highest MAC address, since the root bridge is elected by the highest bridge ID"
    - "Lower Switch A's bridge priority value below that of all other switches, since the root bridge is the switch with the lowest bridge ID"
    - "Assign Switch A more ports, since the switch with the most connections becomes root"
    - "Configure Switch A to send BPDUs more frequently, since the most active switch wins election"
  answer: 1
  explanation: "The root bridge is elected as the switch with the lowest bridge ID, which is a combination of a configurable priority value and the switch's MAC address. By lowering Switch A's priority (e.g., to 4096 from the default 32768), its bridge ID becomes lower than all others, guaranteeing root election. Option A is backwards — the switch with the *lowest* bridge ID wins, and a low MAC address would help, but administrators control the priority field precisely to override MAC-based randomness. Options C and D describe non-existent criteria."

- question: "During normal STP operation, a port is in the 'blocking' state. What is that port actually doing?"
  type: multiple-choice
  options:
    - "The port is completely powered down and does not process any frames"
    - "The port forwards traffic but at reduced speed to avoid overloading the network"
    - "The port does not forward traffic but continues to receive and process BPDUs, staying ready to transition if the topology changes"
    - "The port discards all incoming frames including BPDUs, acting as a complete barrier"
  answer: 2
  explanation: "A blocked port is not 'off' — it is actively listening for BPDUs. This is critical to STP's recovery function: if an active link fails and the blocked port detects the change (through missing BPDUs or a topology change notification), it can transition to forwarding and restore connectivity. If blocked ports discarded BPDUs, STP could not detect topology changes and would lose its fault-tolerance capability. The port suppresses data traffic to prevent loops, but must remain aware of the spanning tree's state at all times."

- question: "STP prevents broadcast storms by removing redundant cables from the physical network, so that no loops exist in the wiring."
  type: true-false
  answer: false
  explanation: "STP prevents loops by logically blocking ports — the redundant physical cables remain in place and fully connected. Blocked ports suppress data forwarding while retaining the physical link, keeping the redundant paths as standing backups. If STP removed the cables, you would gain loop prevention but lose all redundancy. The whole value of STP is that you get both: loop-free operation during normal conditions AND automatic failover when an active link goes down (the blocked port detects the failure and transitions to forwarding). Physical removal of cables would require manual intervention to restore."

- question: "Rapid Spanning Tree Protocol (RSTP) converges faster than classic STP primarily because it uses higher-speed hardware to process BPDUs faster."
  type: true-false
  answer: false
  explanation: "RSTP's speed improvement is architectural, not hardware-based. Classic STP forces all ports to transition through listening and learning states on fixed 15-second timers before forwarding — a design inherited from when networks had no way to quickly verify topology. RSTP replaces these timers with a proposal-agreement handshake: when a port comes up, switches negotiate directly with their neighbor to confirm there is no loop before forwarding. This port-by-port negotiation converges in under a second regardless of hardware speed, because the delay was always a timer, not processing time."

- question: "Explain why blocking redundant ports rather than disabling redundant cables is essential to STP's purpose."
  type: short-answer
  answer: "STP's goal is to provide both loop-free forwarding AND fault tolerance. Physically removing redundant cables would eliminate loops but also eliminate the backup paths that enable recovery from link failures. By blocking ports logically (suppressing data forwarding while keeping the physical link active and listening for BPDUs), STP preserves the redundant links as standby backups. When an active link fails, the previously blocked port detects the topology change and transitions to forwarding, restoring connectivity without any manual intervention. The blocked state is a standby state, not an off state."
  explanation: "The distinction matters because a network built for reliability needs redundant physical infrastructure — but that same redundancy creates loops at Layer 2. STP resolves this tension by operating at the logical forwarding layer rather than the physical layer, leaving redundant cables in place while preventing the broadcast storms that loops would cause. The blocked port is essentially a closed valve on a pressurized backup line: inactive during normal operation, immediately available when needed."
```

## Explainer

From your study of Ethernet and switching, you know that switches forward frames based on MAC address tables and that they flood frames when the destination is unknown. Now consider what happens when you add redundant links between switches for reliability — a frame that gets flooded will travel the loop forever, multiplying with each pass. Within seconds, these **broadcast storms** consume all bandwidth and crash the network. Spanning Tree Protocol exists to prevent this by logically disabling just enough links to eliminate all loops while keeping the network connected.

STP works by electing a single **root bridge** — the switch with the lowest bridge ID (a combination of a configurable priority value and the switch's MAC address). Every other switch then calculates the shortest path to the root bridge using path cost, which is inversely related to link speed. Each switch identifies one **root port** — the port with the lowest cost path to the root. On each network segment, one switch's port is designated as the **designated port** (the one offering the best path to the root for that segment), and all other ports connecting to that segment are placed in a **blocked state**. Blocked ports do not forward traffic but continue listening for BPDUs, ready to activate if the topology changes.

The protocol communicates through **Bridge Protocol Data Units** (BPDUs) — small frames that switches exchange to announce their identity, their root bridge claim, and their path cost to the root. When a switch first connects, or when a link fails, the switches re-exchange BPDUs and recalculate the spanning tree. In classic STP (802.1D), this reconvergence takes 30 to 50 seconds as ports transition through listening and learning states before forwarding — an eternity for modern networks. **Rapid Spanning Tree Protocol** (RSTP, 802.1w) dramatically improves this by introducing proposal-agreement handshakes between directly connected switches, allowing ports to transition to forwarding in under a second.

Think of STP as a network-wide consensus algorithm: every switch agrees on who the root is, calculates its own best path, and cooperatively blocks redundant paths. The blocked links are not wasted — they are standing by as backups. If an active link fails, the blocked port detecting the change can transition to forwarding, restoring connectivity. This gives you the reliability benefit of redundant physical links without the catastrophic failure mode of Layer 2 loops. The tradeoff is that blocked links carry zero traffic during normal operation, which is why more advanced techniques like link aggregation (LACP) and per-VLAN spanning tree eventually supplement or replace basic STP in larger networks.
