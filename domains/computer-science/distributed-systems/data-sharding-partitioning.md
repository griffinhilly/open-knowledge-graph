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

## Questions

```yaml
- question: "A database uses hash sharding on user_id. An analyst runs the query: 'Find all users who signed up between January and March 2024.' How does the database handle this query?"
  type: multiple-choice
  options:
    - "It routes the query to the shard responsible for the date range Jan–Mar 2024"
    - "It must contact every shard, because hash(user_id) scatters adjacent user_ids across all nodes — there is no correlation between signup date and shard location"
    - "It contacts only the shard that happens to store the most recent signups, since hash functions preserve insertion order"
    - "It uses a secondary index on signup date stored on the coordinator node to route the query efficiently"
  answer: 1
  explanation: "Hash sharding distributes data by hash(key) mod N, which scatters adjacent keys across all nodes uniformly. This eliminates hot spots but destroys range locality — there is no shard responsible for a date range. A range scan on any attribute other than the shard key requires contacting every shard (a 'scatter-gather' query). This is the fundamental tradeoff: hash sharding gives excellent uniform load distribution but makes range queries and analytics workloads expensive."

- question: "A social media platform is choosing a shard key. Option A: shard on user_id (high cardinality, uniformly distributed). Option B: shard on country (low cardinality, uneven distribution). Why is option A generally better?"
  type: multiple-choice
  options:
    - "user_id produces more shards, which always improves performance"
    - "country causes hot spots because a few large countries (US, India) would receive a disproportionate fraction of traffic, overwhelming those shards while others sit idle"
    - "user_id is better because alphabetical ordering makes range queries on users more efficient"
    - "country is worse only because it has fewer possible values, not because of traffic distribution"
  answer: 1
  explanation: "The critical failure mode of a poor shard key is the hot spot: when one shard receives significantly more traffic than others, horizontal scaling provides no benefit — the overloaded shard becomes the bottleneck. Country has low cardinality (around 200 values) and highly uneven traffic — the US and India alone represent a huge fraction of most platforms' user bases. Sharding on country concentrates traffic on those two shards. user_id has high cardinality and, with a good hash, uniform distribution — every shard gets roughly equal traffic."

- question: "Hash sharding is strictly better than range sharding because it always distributes load evenly and eliminates hot spots."
  type: true-false
  answer: false
  explanation: "Hash sharding eliminates hot spots from natural key ordering, but at the cost of range query efficiency. When your workload involves range scans — such as 'find all orders placed last week' or 'list users with IDs between 10000 and 20000' — hash sharding forces scatter-gather queries that contact every shard. Range sharding handles these queries efficiently by routing to a single shard. The right choice depends on access patterns: hash sharding suits key-value lookups and point queries; range sharding suits analytics and ordered traversals. Neither is universally better."

- question: "With range sharding on last name, all users with last names starting with 'J' can typically be served by querying a single shard."
  type: true-false
  answer: true
  explanation: "Range sharding assigns contiguous key ranges to nodes, so all keys within a range are co-located on the same shard. If the range partition assigns A–F to shard 1, G–M to shard 2, etc., then all 'J' names fall within the G–M range and live on shard 2. This is the defining advantage of range sharding: range queries are single-shard and efficient. The disadvantage is that uneven data or traffic distribution within a range creates hot spots — if most users have names starting with 'S', the S-range shard may be overloaded."

- question: "A startup is designing a sharding strategy for a social media platform. Why might sharding on user_id be better than sharding on country, and what failure mode remains even with a good shard key?"
  type: short-answer
  answer: "Sharding on user_id provides high cardinality and, with a hash function, near-uniform distribution across shards — each shard gets roughly equal traffic regardless of where users are from. Country has only ~200 possible values and highly skewed traffic (a few countries dominate), causing hot spots on those shards. Even with user_id as the shard key, the remaining failure mode is cross-shard queries: operations that need data from many users simultaneously — like 'find all mutual friends between two users on different shards' or 'compute global leaderboards' — require contacting multiple shards, increasing latency and coordination overhead."
  explanation: "Shard key selection is the single most consequential design decision in a sharded system. A poor key concentrates traffic and negates the benefits of horizontal scaling. But even a well-chosen key cannot eliminate cross-shard queries for all workloads — the fundamental tradeoff is between distribution uniformity (preventing hot spots) and data locality (keeping related data on the same shard to avoid scatter-gather). Most production systems accept some cross-shard queries for rare operations while optimizing the shard key for the most common access patterns."
```

## Explainer

You already understand distributed hash tables and consistent hashing — how to map keys to nodes in a way that distributes load and handles membership changes gracefully. **Data sharding** (also called partitioning) applies these ideas to real databases and storage systems: you split your dataset across multiple machines so that no single node has to store or serve everything. The goal is **horizontal scaling** — adding more machines to handle more data and more queries, rather than buying a bigger single machine.

**Range sharding** assigns contiguous key ranges to each node. For example, users with last names A–F go to node 1, G–M to node 2, and so on. The advantage is that range queries are efficient — scanning all users with names starting with "J" hits a single node. The disadvantage is **hot spots**: if most of your traffic involves names in one range (perhaps a viral signup event in a particular region), one node bears disproportionate load while others sit idle. Range sharding also requires manual or automated split/merge operations as data grows unevenly.

**Hash sharding** applies a hash function to each key and assigns the result to a node (typically via modular arithmetic or consistent hashing). Because hash functions scatter keys uniformly, load distribution is much more even — hot spots from natural key ordering are eliminated. The tradeoff is that range queries become expensive: scanning a range of keys now requires contacting every node, since adjacent keys hash to different locations. This is why hash sharding works well for key-value lookups and point queries but poorly for analytics workloads that scan ordered ranges. Consistent hashing, which you already know, is the standard approach for hash sharding because it minimizes data movement when nodes join or leave — only keys in the affected portion of the ring need to move.

In practice, most production systems use a hybrid approach. They define a **shard key** (the column or attribute used to partition data) and let the application or middleware route queries to the correct shard. Choosing the right shard key is the most consequential design decision: a key with high cardinality and even distribution prevents hot spots, while a key that aligns with common query patterns keeps most queries single-shard. A poor shard key — one that concentrates traffic or forces frequent cross-shard joins — can make sharding worse than no sharding at all. Systems like DynamoDB, Cassandra, and CockroachDB each implement different variants of these strategies, but the underlying tradeoffs between distribution uniformity, range query efficiency, and rebalancing cost remain the same.
