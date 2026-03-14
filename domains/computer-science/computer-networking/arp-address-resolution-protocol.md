---
id: arp-address-resolution-protocol
title: 'ARP: Address Resolution Protocol'
domain: computer-science
course: computer-networking
prerequisites:
- id: mac-addressing
  type: hard
- id: ipv4-addressing
  type: hard
builds-toward:
- network-security-fundamentals
tags:
- arp
- protocol
- address-resolution
- mac-to-ip
stage: advanced
status: draft
---

# ARP: Address Resolution Protocol

## Core Idea
Address Resolution Protocol (ARP) is a Layer 2.5 protocol that maps IPv4 addresses to MAC addresses on a local network segment. When a host needs to send a packet to a destination IP address on the same link, it broadcasts an ARP request; the host with that IP responds with its MAC address, allowing the sender to frame the packet correctly.
