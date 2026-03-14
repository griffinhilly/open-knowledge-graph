---
id: load-balancing-server-selection
title: Load Balancing and Server Selection
domain: computer-science
course: computer-networking
prerequisites:
- id: ip-routing-basics
  type: hard
- id: http-hypertext-transfer-protocol
  type: hard
tags:
- load-balancing
- server-selection
- distribution
- failover
stage: advanced
status: draft
---

# Load Balancing and Server Selection

## Core Idea
Load balancers distribute incoming requests across multiple servers to balance load, improve throughput, and provide fault tolerance. They may operate at layer 4 (transport) for simple round-robin distribution or layer 7 (application) for sophisticated decisions based on request content. Load balancing is essential for scaling services and maintaining availability.
