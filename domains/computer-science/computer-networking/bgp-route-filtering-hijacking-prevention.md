---
id: bgp-route-filtering-hijacking-prevention
title: BGP Route Filtering and Hijacking Prevention
domain: computer-science
course: computer-networking
prerequisites:
- id: bgp-border-gateway-protocol
  type: hard
- id: network-security-fundamentals
  type: hard
builds-toward:
- network-security-fundamentals
- network-standards-and-ietf
tags:
- routing
- bgp
- security
- hijacking
stage: advanced
status: draft
---

# BGP Route Filtering and Hijacking Prevention

## Core Idea
BGP route hijacking occurs when unauthorized ASes announce prefixes they do not own or should not announce. Prevention mechanisms include route filtering (accepting only authorized prefixes from peers), prefix lists, AS-PATH filtering, and RPKI (Resource Public Key Infrastructure). Inbound and outbound filters enforce routing policies and prevent propagation of invalid routes.

## How It's Best Learned
Configure inbound route filters on a BGP router using prefix lists and AS-PATH filters. Simulate a route hijack by announcing a legitimate prefix from an unauthorized AS. Deploy RPKI validation and observe its effect on route acceptance. Monitor BGP RIB (Routing Information Base) changes.

## Common Misconceptions
BGP does not verify that an AS owns a prefix; it relies on filtering and RPKI. AS-PATH filtering is not foolproof against path manipulation. Default-deny filtering is essential; permitting all routes by default opens the network to hijacking.
