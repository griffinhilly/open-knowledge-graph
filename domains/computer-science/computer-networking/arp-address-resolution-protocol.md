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

## Explainer

You already know that IPv4 addresses identify hosts at the network layer and MAC addresses identify network interface cards at the data link layer. These two addressing systems operate independently — an IP address is assigned by network configuration, while a MAC address is burned into the hardware. The fundamental problem ARP solves is bridging this gap: when your computer wants to send a packet to 192.168.1.50 on the local network, it knows the destination IP address but needs the destination MAC address to construct the Ethernet frame. Without the MAC address, the frame cannot be addressed and the switch will not know which port to forward it to.

The **ARP process** works through a simple broadcast-and-reply mechanism. The sender constructs an ARP request containing its own MAC and IP addresses (so the target knows who is asking) and the target IP address, with the target MAC field set to all zeros. This request is sent as an Ethernet broadcast (destination MAC FF:FF:FF:FF:FF:FF), meaning every device on the local network segment receives it. The device whose IP address matches the request responds with an **ARP reply** — a unicast frame sent directly back to the requester — containing its MAC address. The sender then caches this IP-to-MAC mapping in its **ARP table** (also called the ARP cache) so it does not need to broadcast again for subsequent packets to the same destination.

ARP entries have a finite **time-to-live** (typically 1–20 minutes depending on the operating system), after which they expire and must be refreshed. This ensures that if a device changes its network interface or IP assignment, stale mappings do not persist indefinitely. You can inspect the ARP table on most systems with `arp -a`, and you will see entries for every local host your machine has recently communicated with. When the destination IP address is not on the local network, the sender ARPs for the **default gateway's MAC address** instead — the router will handle forwarding the packet to the remote network, but it still needs to be reached via a local Ethernet frame.

ARP's simplicity is also its vulnerability. Because any device can send an ARP reply — even unsolicited — an attacker can send forged ARP replies claiming that their MAC address corresponds to the gateway's IP address. This **ARP spoofing** (or ARP poisoning) attack redirects traffic through the attacker's machine, enabling man-in-the-middle interception. ARP has no authentication mechanism; it trusts every reply it receives. This is why ARP security extensions like Dynamic ARP Inspection (DAI) exist at the switch level, and why IPv6 replaced ARP entirely with the more secure Neighbor Discovery Protocol (NDP).
