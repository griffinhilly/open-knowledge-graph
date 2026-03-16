---
id: vlans-virtual-area-networks
title: VLANs (Virtual Local Area Networks)
domain: computer-science
course: computer-networking
prerequisites:
- id: switching-basics
  type: hard
builds-toward:
- network-security-fundamentals
tags:
- vlan
- segmentation
- layer-2
- traffic-isolation
stage: advanced
status: draft
---

# VLANs (Virtual Local Area Networks)

## Core Idea
A VLAN is a logical subdivision of a physical network that isolates traffic at Layer 2, allowing multiple broadcast domains to coexist on one switch. VLANs are identified by VLAN IDs (1–4094) and enable traffic segregation for security, performance, and administrative purposes without requiring separate physical switches.

## How It's Best Learned
Configure VLANs on a managed switch or in a network simulator; test that frames in different VLANs cannot communicate directly at Layer 2, and observe how a router enables inter-VLAN routing.

## Common Misconceptions
- VLANs provide security; they only segment Layer 2 traffic and can be bypassed by a determined attacker—security requires Layer 3 firewalls.
- VLANs eliminate the need for routers; they require routers or multi-layer switches to route between VLANs.

## Explainer

From your study of switching basics, you know that a switch learns which MAC addresses are reachable on which ports and forwards frames accordingly. By default, every port on a switch belongs to the same **broadcast domain** — when any device sends a broadcast frame (like an ARP request), every other device on the switch receives it. In a small network this is fine, but in a building with hundreds of devices, broadcast storms can saturate the network and every device wastes CPU processing irrelevant broadcasts. **VLANs** solve this by letting you partition a single physical switch into multiple independent broadcast domains.

Think of a VLAN as a virtual wall inside the switch. Ports assigned to VLAN 10 can only communicate at Layer 2 with other ports on VLAN 10 — they cannot see or be seen by ports on VLAN 20, even though they share the same physical hardware. Each VLAN gets a numeric **VLAN ID** (1–4094), and you assign switch ports to VLANs through configuration. An **access port** belongs to exactly one VLAN and connects to end devices (computers, printers). A **trunk port** carries traffic for multiple VLANs simultaneously between switches, using 802.1Q tagging — each frame on the trunk gets a small header inserted that identifies which VLAN it belongs to, so the receiving switch knows where to deliver it.

The practical benefits are immediate. A university can put all faculty devices on VLAN 100 and all student devices on VLAN 200, even if faculty and student offices are on the same floor and plugged into the same switch. The two groups are completely isolated at Layer 2 — a broadcast from a student's laptop never reaches faculty machines. This reduces broadcast traffic, improves performance, and limits the blast radius of network problems. If a student's machine gets infected with malware that floods the network, only VLAN 200 is affected.

Critically, VLANs alone do not allow communication between groups — that requires **inter-VLAN routing**. Since VLANs are separate broadcast domains, traffic from VLAN 100 to VLAN 200 must pass through a router or a Layer 3 switch, just as traffic between two physically separate networks would. This is often done with a "router on a stick" configuration, where a single router interface uses 802.1Q sub-interfaces to route between VLANs. The router becomes the policy enforcement point where you can apply access control lists and firewall rules, giving you both segmentation and controlled inter-segment communication.
