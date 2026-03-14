---
id: consistent-hashing
title: Consistent Hashing
domain: computer-science
course: distributed-systems
prerequisites:
- id: hash-tables
  type: hard
- id: distributed-systems-overview
  type: soft
builds-toward:
- distributed-hash-tables
tags:
- hashing
- load-balancing
- scalability
stage: advanced
status: draft
---

# Consistent Hashing

## Core Idea
Consistent hashing maps both keys and nodes to a ring; a key is assigned to the nearest node clockwise. When a node joins or leaves, only keys in a contiguous range need reassignment, minimizing data movement. This enables dynamic scaling without disrupting unaffected keys and is used in caches (Memcached), CDNs, and DHTs.
