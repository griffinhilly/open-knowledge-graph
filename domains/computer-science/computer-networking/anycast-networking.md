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

## Questions

```yaml
- question: "A company deploys DNS resolvers in five cities and wants clients worldwide to be automatically served by their geographically nearest resolver without any client-side configuration. Which approach achieves this?"
  type: multiple-choice
  options:
    - "Assign each resolver a unique IP and configure split-horizon DNS to return geolocation-appropriate addresses"
    - "Use DNS round-robin to distribute queries evenly across all five resolver IPs"
    - "Assign all five resolvers the same IP prefix and have each advertise it via BGP — anycast routing directs each client to the nearest"
    - "Deploy a centralized load balancer that inspects source IPs and proxies each query to the nearest resolver"
  answer: 2
  explanation: "Anycast assigns the same IP to multiple servers; each advertises that prefix via routing protocols (typically BGP). Routers between the client and Internet backbone see multiple paths to that prefix and select the one with the best metric — effectively the nearest node. No client configuration or centralized load balancer is needed. This is exactly how services like 8.8.8.8 and root DNS nameservers work globally."

- question: "Why does anycast work well for DNS queries but poorly for long-lived TCP connections like video streaming?"
  type: multiple-choice
  options:
    - "Anycast addresses cannot be used with TCP because TCP requires a connection-oriented protocol with a fixed endpoint"
    - "A mid-session route change can redirect subsequent packets to a different server with no knowledge of the existing connection state, breaking the TCP session"
    - "Video streaming requires more bandwidth than a single anycast node can provide"
    - "TCP connections use port numbers that conflict with the anycast routing mechanism"
  answer: 1
  explanation: "TCP sessions accumulate state: sequence numbers, acknowledgment counters, socket buffers, and application session data. If a route change causes subsequent packets to arrive at a different anycast node mid-session, that server has none of this state and cannot continue the connection. For DNS (single UDP request-response pairs), this is harmless — each query is independent. The stateless nature of DNS is what makes it a perfect fit for anycast."

- question: "In anycast, the routing infrastructure — not the client or a centralized coordinator — determines which physical server instance receives a given packet."
  type: true-false
  answer: true
  explanation: "This is the elegant core of anycast: clients send packets to a single IP address with no knowledge of which server will receive them. BGP routing on the network's backbone makes the selection automatically by choosing the path with the best metric to whichever node advertised that prefix. The client needs no special configuration, and no centralized controller is involved — the distributed routing system handles the selection transparently."

- question: "Anycast provides fault tolerance by maintaining a registry of all active servers and actively redirecting traffic away from servers that go offline."
  type: true-false
  answer: false
  explanation: "Anycast resilience is passive, not active. When an anycast node fails and stops advertising its route, the BGP routing system simply reconverges: routers that previously had a route through that node select the next-best path to another node that is still advertising the same prefix. No registry, health-check system, or active redirection is needed. This makes anycast resilient by design — failure of one node is handled automatically by the same routing protocol that handles any link failure."

- question: "Explain why anycast is well-suited to DNS but poorly suited to video streaming, in terms of the session state each protocol requires."
  type: short-answer
  answer: "DNS uses stateless UDP request-response pairs: each query is independent, and if routing changes between queries, a different server can answer the next one without any context. Video streaming requires a persistent TCP connection over which state accumulates — sequence numbers, buffering position, session authentication. If routing changes mid-stream and packets are redirected to a different anycast node, that server has no knowledge of the session and cannot continue it. Anycast's geographic routing instability is irrelevant for stateless queries and fatal for stateful sessions."
  explanation: "The statefulness of the application is the key variable. Short, independent transactions like DNS, NTP, or QUIC retries are natural fits. Applications requiring persistent sessions need either TCP connection pinning, flow-aware load balancers, or a different routing architecture entirely."
```

## Explainer

From your work with IPv4 addressing, you know that an IP address normally identifies a single interface on a single host. From your study of routing algorithms, you know that routers build forwarding tables and select the best path to each destination prefix. **Anycast** exploits this routing machinery in a clever way: multiple servers in different physical locations all announce the same IP address prefix to the routing system. Each router along the way simply picks the "closest" announcement based on its normal routing metrics — hop count, latency, or link cost — and forwards packets accordingly. No special protocol is needed; the standard routing infrastructure does all the work.

Imagine a DNS service that operates servers in New York, London, and Tokyo, all advertising the address 198.51.100.1. When a client in Paris sends a DNS query to that address, the routers between Paris and the Internet backbone see multiple routes to 198.51.100.1 and select the London server because it has the fewest hops or lowest latency. A client in Osaka would be routed to Tokyo for the same reason. The client has no idea that the address maps to multiple servers — it simply sends a packet and gets a response from whichever server the routing system deemed nearest.

Anycast works best for **short, stateless transactions** like DNS queries, where each request-response pair is independent. This is because routing can change: if a network path shifts, subsequent packets might be delivered to a different server than the one that received the first packet. For a single UDP query-and-response this is harmless, but for a long-lived TCP connection, a mid-conversation route change would send packets to a server that has no knowledge of the connection state, breaking the session. Modern CDNs work around this limitation using techniques like connection pinning and flow-aware load balancers, but the natural fit for anycast remains short-lived, stateless protocols.

The practical benefits are twofold: **latency reduction** and **resilience**. Latency drops because users are automatically routed to the geographically nearest server without any client-side configuration or DNS-based geographic steering. Resilience improves because if one anycast node goes offline and stops advertising the route, traffic automatically shifts to the next-closest node — the routing protocol reconverges, and clients are redirected within seconds. This is why the root DNS servers, major public DNS resolvers like 8.8.8.8, and DDoS mitigation services all rely heavily on anycast.
