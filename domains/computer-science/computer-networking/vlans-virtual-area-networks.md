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
