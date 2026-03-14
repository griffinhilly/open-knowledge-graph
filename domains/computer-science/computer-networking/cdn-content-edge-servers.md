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
