---
id: cdn-content-edge-servers
title: CDN Architecture and Edge Server Placement
domain: computer-science
course: computer-networking
prerequisites:
- id: content-delivery-networks
  type: hard
- id: load-balancing-server-selection
  type: hard
builds-toward:
- network-management-and-monitoring
- qos-quality-of-service
tags:
- application-layer
- cdn
- edge-computing
- performance
stage: advanced
status: draft
---

# CDN Architecture and Edge Server Placement

## Core Idea
Content Delivery Networks (CDNs) distribute content to edge servers located near end users, reducing latency and origin server load. Clients are directed to the nearest edge server using DNS-based redirection or anycast routing. CDNs optimize for geographic locality, peer ISP relationships, and congestion to select the best server per client.

## How It's Best Learned
Analyze CDN routing decisions using DNS lookups from different geographic locations. Configure a local CDN edge server using Open Connect (Netflix) or Akamai's test CDN. Measure latency improvement for edge-cached vs. origin-served content.

## Common Misconceptions
CDNs do not cache all content; they cache only what is pushed or accessed frequently. Nearest edge server is not always fastest; ISP relationships and congestion matter more. CDNs require cache invalidation and purge APIs for dynamic content.

## Explainer

You already understand that a CDN distributes copies of content to servers closer to end users, and that load balancing distributes requests across multiple servers. CDN edge server architecture takes these ideas further by asking: *where exactly should those servers be placed, and how does a client get directed to the right one?* The answer involves a combination of network topology awareness, DNS manipulation, and caching strategy that together reduce latency from hundreds of milliseconds to single digits.

**Edge servers** are deployed in strategic locations — typically inside or adjacent to major ISP networks, at Internet exchange points (IXPs), and in data centers within large metropolitan areas. The goal is to place content within one or two network hops of the largest concentrations of users. A large CDN like Akamai operates over 300,000 servers in more than 130 countries, while a purpose-built CDN like Netflix's Open Connect places appliances directly inside ISP networks. The placement decision balances geographic proximity, network peering relationships, and the cost of deploying and maintaining hardware at each location.

Client-to-edge routing uses two primary mechanisms. In **DNS-based redirection**, when a user requests `video.example.com`, the authoritative DNS server (operated by the CDN) examines the client's location (inferred from the DNS resolver's IP address or EDNS Client Subnet data) and returns the IP address of the nearest healthy edge server. The CDN's DNS infrastructure makes this decision in real time, considering server load, network congestion, and content availability. The alternative is **anycast routing**, where multiple edge servers advertise the same IP address via BGP, and the Internet's routing infrastructure naturally directs each client to the topologically closest instance. Anycast is simpler to operate but offers less fine-grained control than DNS redirection.

Edge servers maintain caches of popular content using policies informed by access frequency and recency. When a user requests content that exists in the edge cache (a **cache hit**), the response is served locally with minimal latency. On a **cache miss**, the edge server fetches the content from the **origin server** (or a mid-tier cache), serves the user, and caches it for subsequent requests. The cache's effectiveness depends on the **hit ratio**, which CDNs optimize through techniques like consistent hashing (ensuring the same content always maps to the same edge server), pre-positioning popular content during off-peak hours, and tiered caching architectures where regional mid-tier caches absorb misses before requests reach the origin. For dynamic or personalized content, edge servers may run application logic (edge computing) rather than simply caching, collapsing the boundary between CDN and application server.
