---
id: mpls-multiprotocol-label-switching
title: 'MPLS: Multiprotocol Label Switching'
domain: computer-science
course: computer-networking
prerequisites:
- id: routing-table-concepts
  type: hard
- id: routing-algorithms-overview
  type: hard
builds-toward:
- segment-routing-architecture-sr
- vpn-virtual-private-networks
tags:
- routing
- mpls
- label-switching
- traffic-engineering
stage: advanced
status: draft
---

# MPLS: Multiprotocol Label Switching

## Core Idea
MPLS (Multiprotocol Label Switching) inserts labels between the IP and link-layer headers, enabling fast forwarding based on simple label lookups rather than longest-prefix IP matching. Label Distribution Protocol (LDP) and RSVP-TE distribute labels and establish label-switched paths (LSPs). MPLS enables Traffic Engineering (TE) and VPN services (MPLS-TE, L3VPN).

## How It's Best Learned
Deploy LDP-based MPLS on Cisco or open-source routers (Quagga, FRRouting). Observe label distribution and LSP establishment. Configure MPLS-TE with explicit paths and bandwidth constraints. Monitor label stacks using tcpdump.

## Common Misconceptions
MPLS is not a replacement for IP routing; it runs alongside it. Label lookups are O(1) but still require table lookups; MPLS does not eliminate routing overhead. MPLS labels are local to each link; different labels represent the same path on different hops.
