---
id: ethernet-protocol
title: Ethernet and Frame Structure
domain: computer-science
course: computer-networking
prerequisites:
- id: bandwidth-latency-throughput
  type: soft
builds-toward:
- mac-addressing
- switching-basics
tags:
- ethernet
- link-layer
- frame-format
- lan
stage: advanced
status: draft
---

# Ethernet and Frame Structure

## Core Idea
Ethernet is the dominant Link Layer (Layer 2) technology for local area networks, defining how frames are structured, addressed via MAC addresses, and transmitted over shared or switched media. Modern Ethernet supports speeds from 10 Mbps to 400 Gbps and can work over twisted-pair copper or fiber-optic cable.

## How It's Best Learned
Use packet capture tools (tcpdump, Wireshark) to examine real Ethernet frames, identifying header fields (source/destination MAC, EtherType, CRC) in captured data.

## Common Misconceptions
- Ethernet is only for wired networks; Ethernet frames also travel over wireless via WiFi.
- Ethernet inherently broadcasts; modern switched Ethernet is point-to-point except for broadcast/multicast frames.
