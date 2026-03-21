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

## Questions

```yaml
- question: "In a DHT, why can't nodes simply route lookup requests directly to the responsible node, bypassing intermediate hops?"
  type: multiple-choice
  options:
    - "Direct routing is impossible because the hash function is not invertible — you cannot compute the node address from the key"
    - "Direct routing would require every node to maintain a complete membership list (O(n) state), which becomes impractical as the system grows to millions of nodes"
    - "Direct routing would violate the consistency guarantees required for uniform distribution on the hash ring"
    - "The network topology prevents nodes from communicating with non-adjacent nodes on the ring"
  answer: 1
  explanation: "The O(n) state problem is the core scalability barrier. With millions of nodes, a complete membership list is prohibitively large to store and keep synchronized — every join and leave event would require updating every node. DHTs like Chord and Kademlia solve this by maintaining only O(log n) routing state per node, accepting O(log n) hops as the cost. This is fundamentally the same tradeoff as binary search vs. linear scan: spending a little more time (hops) to avoid maintaining a huge index (full membership list)."

- question: "A new node joins a Chord DHT by picking a random ID on the ring. After the join is complete, which node transfers keys to the new node?"
  type: multiple-choice
  options:
    - "The successor of the new node transfers all its keys so the new node can replicate them for fault tolerance"
    - "The predecessor of the new node transfers the keys in the range that now falls under the new node's responsibility"
    - "Keys are recomputed using a new hash function and redistributed across all nodes to maintain uniform load"
    - "Keys remain with their current nodes until the next periodic rebalancing cycle"
  answer: 1
  explanation: "In Chord, each node is responsible for the keys between its predecessor's ID and its own ID on the ring. When a new node inserts itself, it takes over responsibility for a contiguous range of keys that was previously handled by its successor. The successor transfers those keys to the new node. This is the key virtue of consistent hashing: only the new node's immediate successor is affected — O(keys/n) keys move, rather than redistributing all keys as you would in a naive hash table resize."

- question: "In Kademlia, every lookup query both retrieves the target key and refreshes the querying node's routing table with new information about nearby nodes."
  type: true-false
  answer: true
  explanation: "This is one of Kademlia's architectural advantages. Each iterative lookup contacts nodes close to the target and receives responses that include those nodes' known neighbors. This naturally populates the querying node's k-buckets with fresh, recently-seen node addresses — routing table maintenance is a byproduct of normal operations, not a separate background process. As a result, Kademlia routing tables stay current without dedicated maintenance overhead, which is important in the high-churn peer-to-peer environments where Kademlia is deployed."

- question: "DHTs eliminate the need for data replication because consistent hashing guarantees that every key is always accessible on its responsible node."
  type: true-false
  answer: false
  explanation: "Consistent hashing provides key assignment, not fault tolerance. If the node responsible for a key fails, that key becomes temporarily or permanently unavailable unless copies exist elsewhere. Nodes in real systems fail frequently — hard drives die, machines reboot, network partitions occur. Production DHTs (Chord, Kademlia, Amazon Dynamo) replicate each key to k successor nodes precisely to handle failures. When a node fails, its successors already hold the replicas and can serve requests. Consistent hashing minimizes redistribution on membership changes, but data availability under failure requires explicit replication."

- question: "Explain why the Chord finger table produces O(log n) lookup time, and why this is a better solution than either maintaining a full membership list or routing only to adjacent nodes."
  type: short-answer
  answer: "Chord's finger table contains pointers to O(log n) nodes spaced at exponentially increasing distances around the ring (1/2, 1/4, 1/8 of the ring away, etc.). When forwarding a query, the node routes to the closest finger that precedes the target key, cutting the remaining ring distance roughly in half with each hop — like binary search. This yields O(log n) hops to reach any key. A full membership list achieves O(1) hops but requires O(n) storage per node and O(n) update messages per join/leave. Routing only to adjacent ring neighbors requires O(n) hops (walking around the ring). Finger tables hit the sweet spot: O(log n) state enables O(log n) hops — both costs grow logarithmically, keeping the system scalable for millions of nodes."
  explanation: "The key insight is that Chord applies binary-search logic to routing: each hop eliminates half the remaining candidate space, just as binary search eliminates half the remaining elements. This is not coincidental — the finger table is designed so that entries cover exponentially larger ranges, ensuring the halving property at every step. The tradeoff analysis (O(n) state for O(1) hops, vs. O(log n) state for O(log n) hops, vs. O(1) state for O(n) hops) is the fundamental design space of distributed routing, and Chord's choice sits at the efficient frontier."
```

## Explainer

You already understand hash tables — mapping keys to array positions for O(1) lookup — and consistent hashing — distributing keys around a ring so that adding or removing nodes only redistributes a fraction of keys. A **distributed hash table** combines these ideas into a fully decentralized storage system: data is spread across many machines, any machine can look up any key, and no central coordinator is needed. The core insight is that consistent hashing gives you a natural ownership model — each node is responsible for the keys that fall in its range on the hash ring — and the remaining problem is routing: how does a node that receives a query find the node that owns the key?

The naive approach is for every node to maintain a complete membership list and route directly, but that requires O(n) state per node and doesn't scale. **Chord**, one of the foundational DHT designs, solves this with a **finger table**: each node maintains pointers to O(log n) other nodes spaced at exponentially increasing distances around the ring. To look up a key, a node forwards the request to the closest predecessor of the key in its finger table, which does the same, and so on. Each hop cuts the remaining distance roughly in half, producing O(log n) hops to reach any key — similar to binary search. With 1,000 nodes, a lookup takes about 10 hops; with 1,000,000 nodes, about 20.

**Kademlia**, used in BitTorrent and IPFS, takes a different approach using **XOR distance**: the distance between two node IDs is their bitwise XOR, which forms a valid metric (symmetric, satisfies the triangle inequality). Each node maintains **k-buckets** — lists of known nodes at each XOR distance range. Lookups are iterative: the querying node contacts the α closest nodes it knows, asks them for nodes closer to the target, and repeats until it converges. Kademlia's advantage is that every lookup naturally refreshes routing information, and its XOR metric means the routing table fills unevenly — many entries for nearby nodes, few for distant ones — which is exactly the distribution you want for efficient routing.

When nodes join or leave, the DHT must rebalance. A joining node picks a random ID, looks up its position on the ring, and takes responsibility for the keys in its range — the predecessor transfers those keys. When a node fails, its keys become temporarily unavailable unless the system maintains **replicas** on successor nodes (most production DHTs replicate each key to k successors). The combination of consistent hashing for assignment, logarithmic routing for lookup, and replication for fault tolerance gives DHTs their characteristic properties: decentralized, scalable, and self-healing. These properties made DHTs the backbone of peer-to-peer file sharing and continue to underpin modern decentralized storage systems.
