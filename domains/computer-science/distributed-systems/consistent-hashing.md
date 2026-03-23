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
status: validated
---

# Consistent Hashing

## Core Idea
Consistent hashing maps both keys and nodes to a ring; a key is assigned to the nearest node clockwise. When a node joins or leaves, only keys in a contiguous range need reassignment, minimizing data movement. This enables dynamic scaling without disrupting unaffected keys and is used in caches (Memcached), CDNs, and DHTs.

## Questions

```yaml
- question: "A distributed cache has 10 servers and uses hash(key) % 10 to assign keys to servers. A new server is added, making 11 total. Approximately what fraction of keys must be remapped?"
  type: multiple-choice
  options:
    - "About 1/11 — only the keys that will belong to the new server need to move"
    - "About 1/10 — only the keys on the least-loaded server need to be redistributed"
    - "About 90% — changing n from 10 to 11 changes the result of hash(key) % n for nearly every key"
    - "0% — hash functions are stable, so existing key assignments are preserved"
  answer: 2
  explanation: "With modular hashing, the number of servers n is baked into every assignment. Changing n from 10 to 11 means hash(key) % 10 vs. hash(key) % 11 give different results for approximately (n−1)/n ≈ 90% of keys. This near-total remapping causes a cache miss storm in distributed caches and massive data migration in storage systems. Consistent hashing solves exactly this problem — only the keys in the arc adjacent to the new node (roughly 1/11) need remapping."

- question: "A consistent hashing ring has five servers at widely spaced positions. One server owns 5% of the ring, another owns 60%. Which technique addresses this load imbalance?"
  type: multiple-choice
  options:
    - "Replicate data from the overloaded server to the underloaded one to balance storage"
    - "Add more physical servers until ring arcs are approximately equal"
    - "Use virtual nodes — hash each physical server to many ring positions so each server's responsibility is spread across many small arcs"
    - "Switch to modular hashing, which produces more uniform distribution by design"
  answer: 2
  explanation: "Virtual nodes (vnodes) solve the load imbalance that arises when few physical nodes produce uneven arc lengths. By hashing variations of each server's identifier (e.g., 'nodeA-1', 'nodeA-2', ...) to place it at 100–200 positions on the ring, each physical server owns many small, scattered arcs. The law of large numbers smooths the distribution. When a node leaves, its load is spread across all remaining nodes rather than dumped onto a single successor."

- question: "With consistent hashing, when a node is added to or removed from the ring, only keys in a contiguous arc of the ring need to be reassigned."
  type: true-false
  answer: true
  explanation: "This is the core property that makes consistent hashing valuable. When a node joins, it takes over the arc between itself and the next node counterclockwise — only those keys need remapping. When a node leaves, its keys transfer to the next node clockwise. All keys outside this arc remain with their existing nodes, unchanged. This localized disruption is the fundamental advantage over modular hashing, where any change to n disrupts nearly all assignments globally."

- question: "A cluster using consistent hashing will experience a near-total cache miss storm when a node is added, just like modular hashing, because all hash values need to be recomputed."
  type: true-false
  answer: false
  explanation: "Hash values for existing keys do not change in consistent hashing — keys and nodes are already mapped to the ring. Adding a node only changes which node 'owns' the arc containing the new node's ring position; only the keys in that arc need remapping, approximately 1/n of all keys. The cache miss storm in modular hashing comes from changing n, which invalidates nearly all hash(key) % n assignments. Consistent hashing decouples assignments from n entirely."

- question: "Explain why consistent hashing is described as 'elastic' — what property makes it fundamentally better suited to horizontally scalable distributed systems?"
  type: short-answer
  answer: "Consistent hashing decouples key assignment from the number of nodes. In modular hashing, n is embedded in every assignment, so any change to n invalidates nearly all mappings. In consistent hashing, keys and nodes share a stable ring, and only the keys in the arc adjacent to an added or removed node need reassignment. Because the vast majority of keys are unaffected by any single node change, the system can expand and contract — scaling up under load, removing failed nodes — without triggering mass data migration or cache miss storms."
  explanation: "'Elastic' means the system can change size without global disruption. This is essential for distributed systems that must handle variable load, hardware failures, and rolling upgrades — all of which cause nodes to join and leave. The disruption is proportional and local rather than catastrophic, which is exactly what horizontal scalability requires."
```

## Explainer

You already know how hash tables work: hash the key, compute an index with modular arithmetic (`hash(key) % n`), and store the value at that index. This works beautifully on a single machine. But in a distributed system with *n* server nodes, the same approach — `hash(key) % n` to pick a server — has a fatal flaw. When you add or remove a server, *n* changes, and nearly every key maps to a different server. If you go from 10 to 11 servers, roughly 90% of your keys need to move. For a distributed cache, that means a near-total cache miss storm; for a storage system, it means massive data migration.

**Consistent hashing** solves this by arranging the hash space into a ring (imagine the numbers 0 through 2^32 - 1 wrapped into a circle). Both keys and nodes are hashed onto this ring using the same hash function. To find which node owns a key, you start at the key's position on the ring and walk clockwise until you hit a node — that node is responsible for the key. The elegant consequence is that when a node joins, it takes over only the keys in the arc between it and the next node counterclockwise. When a node leaves, only its keys need to be reassigned to the next node clockwise. In both cases, the vast majority of keys stay exactly where they are.

The naive version has a practical problem: with only a few nodes, the arcs between them can be very uneven, leading to severe **load imbalance** — one node might own 60% of the key space while another owns 5%. The standard fix is **virtual nodes** (vnodes): instead of placing each physical node at one point on the ring, you place it at many points (say, 100-200) by hashing variations of its identifier (e.g., "nodeA-1", "nodeA-2", ...). This spreads each node's responsibility across many small arcs, and the law of large numbers smooths out the distribution. When a physical node leaves, its load is distributed across many other nodes rather than dumped onto a single successor.

Consistent hashing is foundational infrastructure in distributed systems. Amazon's Dynamo uses it to partition data across storage nodes. Memcached and Redis Cluster use it to distribute cache keys. CDNs use it to route requests to edge servers. The core insight is simple but profound: by decoupling the hash space from the number of nodes, you make the system **elastic** — nodes can come and go with minimal disruption, which is exactly the property you need in systems designed to scale horizontally and tolerate failures.
