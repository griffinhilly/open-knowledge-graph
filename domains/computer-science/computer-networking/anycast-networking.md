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

## Explainer

From your work with IPv4 addressing, you know that an IP address normally identifies a single interface on a single host. From your study of routing algorithms, you know that routers build forwarding tables and select the best path to each destination prefix. **Anycast** exploits this routing machinery in a clever way: multiple servers in different physical locations all announce the same IP address prefix to the routing system. Each router along the way simply picks the "closest" announcement based on its normal routing metrics — hop count, latency, or link cost — and forwards packets accordingly. No special protocol is needed; the standard routing infrastructure does all the work.

Imagine a DNS service that operates servers in New York, London, and Tokyo, all advertising the address 198.51.100.1. When a client in Paris sends a DNS query to that address, the routers between Paris and the Internet backbone see multiple routes to 198.51.100.1 and select the London server because it has the fewest hops or lowest latency. A client in Osaka would be routed to Tokyo for the same reason. The client has no idea that the address maps to multiple servers — it simply sends a packet and gets a response from whichever server the routing system deemed nearest.

Anycast works best for **short, stateless transactions** like DNS queries, where each request-response pair is independent. This is because routing can change: if a network path shifts, subsequent packets might be delivered to a different server than the one that received the first packet. For a single UDP query-and-response this is harmless, but for a long-lived TCP connection, a mid-conversation route change would send packets to a server that has no knowledge of the connection state, breaking the session. Modern CDNs work around this limitation using techniques like connection pinning and flow-aware load balancers, but the natural fit for anycast remains short-lived, stateless protocols.

The practical benefits are twofold: **latency reduction** and **resilience**. Latency drops because users are automatically routed to the geographically nearest server without any client-side configuration or DNS-based geographic steering. Resilience improves because if one anycast node goes offline and stops advertising the route, traffic automatically shifts to the next-closest node — the routing protocol reconverges, and clients are redirected within seconds. This is why the root DNS servers, major public DNS resolvers like 8.8.8.8, and DDoS mitigation services all rely heavily on anycast.
