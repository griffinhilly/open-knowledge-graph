---
id: data-sharding-partitioning
title: Data Sharding and Partitioning Strategies
domain: computer-science
course: distributed-systems
prerequisites:
- id: distributed-hash-tables
  type: hard
- id: consistent-hashing
  type: hard
tags:
- scalability
- partitioning
- sharding
stage: advanced
status: draft
---

# Data Sharding and Partitioning Strategies

## Core Idea
Data sharding partitions data across multiple nodes to enable horizontal scaling beyond a single machine's capacity. Range sharding assigns contiguous key ranges to nodes; hash sharding distributes based on hash(key) mod num_nodes; consistent hashing minimizes rebalancing when nodes join or leave. Each strategy involves tradeoffs in rebalancing cost, hot spot risk, and query efficiency.

## Explainer

You already understand distributed hash tables and consistent hashing — how to map keys to nodes in a way that distributes load and handles membership changes gracefully. **Data sharding** (also called partitioning) applies these ideas to real databases and storage systems: you split your dataset across multiple machines so that no single node has to store or serve everything. The goal is **horizontal scaling** — adding more machines to handle more data and more queries, rather than buying a bigger single machine.

**Range sharding** assigns contiguous key ranges to each node. For example, users with last names A–F go to node 1, G–M to node 2, and so on. The advantage is that range queries are efficient — scanning all users with names starting with "J" hits a single node. The disadvantage is **hot spots**: if most of your traffic involves names in one range (perhaps a viral signup event in a particular region), one node bears disproportionate load while others sit idle. Range sharding also requires manual or automated split/merge operations as data grows unevenly.

**Hash sharding** applies a hash function to each key and assigns the result to a node (typically via modular arithmetic or consistent hashing). Because hash functions scatter keys uniformly, load distribution is much more even — hot spots from natural key ordering are eliminated. The tradeoff is that range queries become expensive: scanning a range of keys now requires contacting every node, since adjacent keys hash to different locations. This is why hash sharding works well for key-value lookups and point queries but poorly for analytics workloads that scan ordered ranges. Consistent hashing, which you already know, is the standard approach for hash sharding because it minimizes data movement when nodes join or leave — only keys in the affected portion of the ring need to move.

In practice, most production systems use a hybrid approach. They define a **shard key** (the column or attribute used to partition data) and let the application or middleware route queries to the correct shard. Choosing the right shard key is the most consequential design decision: a key with high cardinality and even distribution prevents hot spots, while a key that aligns with common query patterns keeps most queries single-shard. A poor shard key — one that concentrates traffic or forces frequent cross-shard joins — can make sharding worse than no sharding at all. Systems like DynamoDB, Cassandra, and CockroachDB each implement different variants of these strategies, but the underlying tradeoffs between distribution uniformity, range query efficiency, and rebalancing cost remain the same.
