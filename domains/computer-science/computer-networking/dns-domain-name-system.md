---
id: dns-domain-name-system
title: 'DNS: Domain Name System'
domain: computer-science
course: computer-networking
prerequisites:
- id: udp-user-datagram-protocol
  type: hard
- id: port-addressing-sockets
  type: soft
builds-toward:
- http-hypertext-transfer-protocol
- content-delivery-networks
tags:
- dns
- domain-name
- resolution
- recursive-lookup
- caching
stage: advanced
status: draft
---

# DNS: Domain Name System

## Core Idea
DNS translates human-readable domain names (e.g., example.com) to IP addresses using a hierarchical, distributed database of authoritative nameservers. DNS queries are typically recursive (a resolver queries nameservers on behalf of the client) and heavily cached at multiple levels, making DNS central to Internet usability.

## How It's Best Learned
Use `nslookup` or `dig` to perform DNS lookups and observe the hierarchy of nameservers; enable DNS query logging to see cached vs. authoritative responses.

## Common Misconceptions
- DNS always performs full resolution from root; most queries hit cached resolvers.
- DNS is only for A records; DNS also handles CNAME, MX, TXT, and other record types.
