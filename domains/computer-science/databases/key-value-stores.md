---
id: key-value-stores
title: Key-Value Stores
domain: computer-science
course: databases
prerequisites:
- id: nosql-concepts
  type: hard
- id: hash-tables
  type: soft
- id: hash-indexes
  type: soft
builds-toward:
- cap-theorem
tags:
- key-value store
- Redis
- caching
- TTL
- in-memory
- Memcached
- pub-sub
stage: formal-systems
status: draft
---

# Key-Value Stores

## Core Idea
Key-value stores provide the simplest NoSQL data model: values are stored and retrieved by opaque string keys with O(1) average-case lookups, analogous to a distributed hash table. Their extreme simplicity and speed make them ideal for caching, session storage, rate limiting, feature flags, and pub/sub messaging. Systems like Redis extend the basic model with rich data structures (sorted sets, lists, streams) and optional persistence. The data model's simplicity is also its limitation: no secondary indexes, no joins, and no complex query support.

## How It's Best Learned
Use Redis CLI or a client library to implement a caching layer over a slower database query, with TTL-based expiration. Explore cache invalidation strategies and atomic operations like INCR for counters.

## Common Misconceptions
- Key-value stores are used alongside relational databases (caching, sessions), not as replacements — their use cases are complementary.
- In-memory stores like Redis offer persistence options (RDB snapshots, AOF logging) but are not substitutes for durable transactional storage.
- Cache invalidation — knowing when to evict a stale value — is a hard problem that key-value stores do not solve automatically.
