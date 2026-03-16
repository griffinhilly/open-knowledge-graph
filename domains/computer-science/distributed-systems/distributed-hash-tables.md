---
id: distributed-hash-tables
title: Distributed Hash Tables and DHT
domain: computer-science
course: distributed-systems
prerequisites:
- id: hash-tables
  type: hard
- id: consistent-hashing
  type: hard
builds-toward:
- gossip-protocols
tags:
- dht
- peer-to-peer
- distributed-storage
stage: advanced
status: draft
---

# Distributed Hash Tables and DHT

## Core Idea
Distributed hash tables (DHTs) extend hash tables across many machines using consistent hashing: keys hash to positions on a ring, each node stores a range, and lookups route toward the responsible node. DHTs enable decentralized storage (Chord, Kademlia) with logarithmic lookup time and automatic load balancing as nodes join and leave.

## Explainer

You already understand hash tables — mapping keys to array positions for O(1) lookup — and consistent hashing — distributing keys around a ring so that adding or removing nodes only redistributes a fraction of keys. A **distributed hash table** combines these ideas into a fully decentralized storage system: data is spread across many machines, any machine can look up any key, and no central coordinator is needed. The core insight is that consistent hashing gives you a natural ownership model — each node is responsible for the keys that fall in its range on the hash ring — and the remaining problem is routing: how does a node that receives a query find the node that owns the key?

The naive approach is for every node to maintain a complete membership list and route directly, but that requires O(n) state per node and doesn't scale. **Chord**, one of the foundational DHT designs, solves this with a **finger table**: each node maintains pointers to O(log n) other nodes spaced at exponentially increasing distances around the ring. To look up a key, a node forwards the request to the closest predecessor of the key in its finger table, which does the same, and so on. Each hop cuts the remaining distance roughly in half, producing O(log n) hops to reach any key — similar to binary search. With 1,000 nodes, a lookup takes about 10 hops; with 1,000,000 nodes, about 20.

**Kademlia**, used in BitTorrent and IPFS, takes a different approach using **XOR distance**: the distance between two node IDs is their bitwise XOR, which forms a valid metric (symmetric, satisfies the triangle inequality). Each node maintains **k-buckets** — lists of known nodes at each XOR distance range. Lookups are iterative: the querying node contacts the α closest nodes it knows, asks them for nodes closer to the target, and repeats until it converges. Kademlia's advantage is that every lookup naturally refreshes routing information, and its XOR metric means the routing table fills unevenly — many entries for nearby nodes, few for distant ones — which is exactly the distribution you want for efficient routing.

When nodes join or leave, the DHT must rebalance. A joining node picks a random ID, looks up its position on the ring, and takes responsibility for the keys in its range — the predecessor transfers those keys. When a node fails, its keys become temporarily unavailable unless the system maintains **replicas** on successor nodes (most production DHTs replicate each key to k successors). The combination of consistent hashing for assignment, logarithmic routing for lookup, and replication for fault tolerance gives DHTs their characteristic properties: decentralized, scalable, and self-healing. These properties made DHTs the backbone of peer-to-peer file sharing and continue to underpin modern decentralized storage systems.
