---
id: icmpv6-neighbor-discovery-protocol
title: ICMPv6 and Neighbor Discovery Protocol
domain: computer-science
course: computer-networking
prerequisites:
- id: ipv6-addressing
  type: hard
- id: ipv4-ipv6-comparison
  type: hard
- id: icmp-internet-control-message-protocol
  type: soft
builds-toward:
- ipv6-addressing
- network-security-fundamentals
tags:
- network-layer
- ipv6
- neighbor-discovery
- icmp
stage: advanced
status: draft
---

# ICMPv6 and Neighbor Discovery Protocol

## Core Idea
ICMPv6 Neighbor Discovery Protocol (NDP) replaces IPv4's ARP and provides host and router discovery, address autoconfiguration, and prefix announcement. Router Advertisement messages announce prefixes and configuration parameters, while Neighbor Solicitation/Advertisement messages resolve IPv6 addresses to link-layer addresses. NDP is integral to IPv6's stateless address autoconfiguration.

## How It's Best Learned
Monitor NDP traffic using tcpdump on an IPv6 network or test environment. Configure stateless address autoconfiguration and observe RA/NS/NA message sequences. Test duplicate address detection and understand default router selection.

## Common Misconceptions
NDP is more complex than ARP; it integrates address resolution, router discovery, and configuration. Neighbor Solicitation is not broadcast; it uses IPv6 multicast to the solicited-node multicast group. ICMPv6 cannot be fully blocked without breaking IPv6 functionality.
