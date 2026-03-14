---
id: mac-addressing
title: MAC Addressing and Hardware Identification
domain: computer-science
course: computer-networking
prerequisites:
- id: ethernet-protocol
  type: hard
builds-toward:
- switching-basics
- arp-address-resolution-protocol
- vlans-virtual-area-networks
tags:
- mac-address
- layer-2
- hardware-address
- identification
stage: advanced
status: draft
---

# MAC Addressing and Hardware Identification

## Core Idea
A Media Access Control (MAC) address is a 48-bit identifier assigned to network interface cards to uniquely identify devices on a local network segment. MAC addresses are hierarchical: the first 24 bits identify the manufacturer (OUI), and the remaining 24 bits are assigned by the manufacturer. They are used at Layer 2 to deliver frames within a LAN.

## How It's Best Learned
Use `ip link show` (Linux) or `ipconfig /all` (Windows) to view your machine's MAC address; use ARP tools to see MAC-to-IP mappings on your local network.

## Common Misconceptions
- MAC addresses are globally unique; the OUI is globally assigned, but the lower 24 bits are only unique within a manufacturer and can be spoofed.
- MAC addresses work across the Internet; they only identify devices on the same link segment.
