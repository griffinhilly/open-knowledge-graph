---
id: content-delivery-networks
title: Content Delivery Networks (CDNs)
domain: computer-science
course: computer-networking
prerequisites:
- id: dns-domain-name-system
  type: hard
- id: http-hypertext-transfer-protocol
  type: hard
tags:
- cdn
- content-distribution
- edge-caching
- latency-reduction
- geographical-distribution
stage: advanced
status: draft
---

# Content Delivery Networks (CDNs)

## Core Idea
A CDN is a geographically distributed network of caches (edge servers) that store copies of popular content. CDNs intercept DNS requests and direct clients to the nearest edge server, reducing latency and bandwidth costs. Modern CDNs like Akamai, Cloudflare, and AWS CloudFront are critical infrastructure for web performance.
