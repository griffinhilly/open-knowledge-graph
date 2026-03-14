---
id: anycast-networking
title: Anycast Networking
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv4-addressing
  type: hard
- id: routing-algorithms-overview
  type: hard
builds-toward:
- content-delivery-networks
tags:
- anycast
- load-balancing
- address-reuse
- routing
stage: advanced
status: draft
---

# Anycast Networking

## Core Idea
Anycast allows multiple servers to share the same IP address, with routing protocols directing packets to the nearest or best server based on network distance. Unlike unicast (one sender to one receiver) and multicast (one sender to many receivers), anycast provides one-sender-to-one-of-many-receivers semantics. Anycast is used in DNS and CDNs to direct clients to nearby servers.
