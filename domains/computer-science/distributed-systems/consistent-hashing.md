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
- id: modular-arithmetic-discrete
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

## Explainer

You already know how hash tables work: hash the key, compute an index with modular arithmetic (`hash(key) % n`), and store the value at that index. This works beautifully on a single machine. But in a distributed system with *n* server nodes, the same approach — `hash(key) % n` to pick a server — has a fatal flaw. When you add or remove a server, *n* changes, and nearly every key maps to a different server. If you go from 10 to 11 servers, roughly 90% of your keys need to move. For a distributed cache, that means a near-total cache miss storm; for a storage system, it means massive data migration.

**Consistent hashing** solves this by arranging the hash space into a ring (imagine the numbers 0 through 2^32 - 1 wrapped into a circle). Both keys and nodes are hashed onto this ring using the same hash function. To find which node owns a key, you start at the key's position on the ring and walk clockwise until you hit a node — that node is responsible for the key. The elegant consequence is that when a node joins, it takes over only the keys in the arc between it and the next node counterclockwise. When a node leaves, only its keys need to be reassigned to the next node clockwise. In both cases, the vast majority of keys stay exactly where they are.

The naive version has a practical problem: with only a few nodes, the arcs between them can be very uneven, leading to severe **load imbalance** — one node might own 60% of the key space while another owns 5%. The standard fix is **virtual nodes** (vnodes): instead of placing each physical node at one point on the ring, you place it at many points (say, 100-200) by hashing variations of its identifier (e.g., "nodeA-1", "nodeA-2", ...). This spreads each node's responsibility across many small arcs, and the law of large numbers smooths out the distribution. When a physical node leaves, its load is distributed across many other nodes rather than dumped onto a single successor.

Consistent hashing is foundational infrastructure in distributed systems. Amazon's Dynamo uses it to partition data across storage nodes. Memcached and Redis Cluster use it to distribute cache keys. CDNs use it to route requests to edge servers. The core insight is simple but profound: by decoupling the hash space from the number of nodes, you make the system **elastic** — nodes can come and go with minimal disruption, which is exactly the property you need in systems designed to scale horizontally and tolerate failures.
