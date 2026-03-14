---
id: overlay-networks-and-tunneling
title: Overlay Networks and Tunneling
domain: computer-science
course: computer-networking
prerequisites:
- id: ip-routing-basics
  type: hard
builds-toward:
- software-defined-networking
- vpn-virtual-private-networks
tags:
- overlay
- tunneling
- encapsulation
- virtual-networks
stage: advanced
status: draft
---

# Overlay Networks and Tunneling

## Core Idea
Overlay networks layer logical topologies on top of physical networks by tunneling packets from one endpoint to another through intermediate routers. A tunnel encapsulates packets from the overlay network inside packets destined to the tunnel endpoint, where they are decapsulated. Overlays enable VPNs, multicast on unicast-only networks, and experimental protocol deployments.
