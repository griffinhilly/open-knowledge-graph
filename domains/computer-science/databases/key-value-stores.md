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
status: validated
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

## Questions

```yaml
- question: "An application stores user profiles in PostgreSQL (200ms per query). A developer proposes caching results in Redis with a 5-minute TTL. A colleague objects: 'Key-value stores shouldn't hold data that's also in our relational database.' Who is correct?"
  type: multiple-choice
  options:
    - "The colleague — key-value stores should never duplicate data from a relational database"
    - "The developer — Redis should replace PostgreSQL for user profiles since it's faster"
    - "The developer — using Redis as a cache layer in front of PostgreSQL is a common and appropriate pattern; TTL manages staleness"
    - "Neither — the right solution is to optimize the SQL query itself"
  answer: 2
  explanation: "Using a key-value store as a cache layer in front of a relational database is one of the most common and appropriate architectural patterns in web systems. Redis (or Memcached) absorbs repeated read traffic at sub-millisecond latency, while PostgreSQL remains the durable source of truth for writes and complex queries. This is the complementary architecture the topic describes — not a replacement, a performance layer. TTL-based expiration is a simple but effective staleness strategy for many use cases. The colleague's objection reflects a misunderstanding of the complementary relationship."

- question: "A product manager asks the backend team to use their existing Redis cluster to answer: 'Which users in New York signed up in the last 7 days?' An engineer says this is not what key-value stores are designed for. Why?"
  type: multiple-choice
  options:
    - "Redis does not support storing user data — it is only for caching computed values"
    - "Redis has no secondary indexes, so finding all keys matching a criterion requires a full scan — the O(1) model only applies to individual key lookups by exact key"
    - "Redis data expires too quickly through TTL to support historical queries"
    - "Key-value stores only work for session data and cannot store location or date information"
  answer: 1
  explanation: "The fundamental limitation of key-value stores is that retrieval requires knowing the exact key. There are no secondary indexes — you cannot query 'find all records where city = New York AND signup_date > X.' To answer that question, you would need to iterate over every key in Redis and check each value, which is O(n) and defeats the purpose. This query is exactly what relational databases with indexes are designed for. Recognizing this limitation — and routing queries accordingly — is the core skill in choosing between these storage systems."

- question: "Redis is an in-memory store and therefore can seldom persist data to disk, making it unsuitable for any use case where data is expected to survive a server restart."
  type: true-false
  answer: false
  explanation: "Redis supports two persistence mechanisms: RDB (Redis Database) snapshots that write a point-in-time copy of the dataset to disk at configurable intervals, and AOF (Append-Only File) that logs every write operation for replay on restart. Redis is primarily optimized as an in-memory system, and its persistence is not as durable as a transactional database with synchronous disk writes — but the claim that it cannot persist is simply wrong. Many production Redis deployments use persistence options while still benefiting from in-memory speed."

- question: "Cache invalidation — deciding when to evict or update cached data — is a problem that key-value stores solve automatically through TTL expiration."
  type: true-false
  answer: false
  explanation: "TTL expiration handles one specific case: time-based staleness. If data doesn't change frequently and brief staleness is acceptable, TTL works well. But if source data is updated (a user changes their profile, a price changes), the cached entry may remain stale until the TTL expires — the key-value store has no mechanism to detect or respond to changes in the underlying database. Cache invalidation strategy must be designed at the application level: either explicitly deleting or updating cache keys on writes (write-through or write-around caching), or accepting bounded staleness via TTL. This is why cache invalidation is famously described as one of computer science's hard problems."

- question: "What is the fundamental tradeoff of the key-value data model, and why does this make key-value stores a complement to relational databases rather than a replacement?"
  type: short-answer
  answer: "Key-value stores trade flexibility for speed. They provide O(1) average-case lookup by a single exact key, making them extremely fast for read-heavy workloads. But they have no secondary indexes (you can't find all records matching a field value), no joins, no schema enforcement, and no complex query support. Relational databases are slower for simple key lookups but can answer arbitrary structured queries. The right architecture uses both: a relational database as the durable, queryable source of truth, and a key-value store as a fast cache layer in front of it. Each tool does what it is designed to do — using a key-value store for complex queries, or a relational database for high-throughput key lookups, would be using the wrong tool."
  explanation: "The complementary architecture is the key practical takeaway. The most common mistake is viewing key-value stores as a simpler, faster alternative to relational databases — implying one replaces the other. In practice, they serve different functions and are deployed together. Redis handles session state, caching, rate limiting, and pub/sub; PostgreSQL handles transactions, reporting, and complex queries. Understanding which problems each solves well is the design skill."
```

## Explainer

From your study of NoSQL concepts, you know that not every application needs the full power of a relational database with schemas, joins, and ACID transactions. **Key-value stores** sit at the simplest end of the NoSQL spectrum: you store a value under a key, and you retrieve it by that key. That's essentially the entire API — `GET(key)`, `SET(key, value)`, `DELETE(key)`. If you've worked with hash tables, the mental model is identical, except the hash table is now a networked service that can be shared across multiple application servers.

The power of this simplicity becomes clear when you consider the most common use case: **caching**. Suppose your web application runs an expensive SQL query that joins five tables and takes 200 milliseconds. You can store the result in a key-value store like Redis under a descriptive key (say, `"user:42:dashboard"`), and subsequent requests retrieve it in under a millisecond. The key-value store acts as a fast intermediate layer between your application and your relational database, absorbing repeated reads that would otherwise hammer the slower storage layer. TTL (time-to-live) settings let entries expire automatically, so stale data doesn't persist indefinitely.

Beyond simple caching, systems like Redis extend the key-value model with rich **data structures** as values. A value can be a string, a list (for message queues), a set (for tracking unique visitors), a sorted set (for leaderboards ranked by score), or a hash (for storing structured objects without serialization). These structures support atomic operations — `INCR` to bump a counter, `LPUSH`/`RPOP` for queue behavior, `ZADD`/`ZRANGE` for sorted set operations — making Redis useful for rate limiting, session management, real-time analytics, and pub/sub messaging, all without the overhead of a query parser or transaction manager.

The fundamental tradeoff is flexibility for speed. Key-value stores have no secondary indexes — you can't query "find all users in New York" without scanning every key. There are no joins, no aggregation, and no schema enforcement. This makes them a complement to relational databases, not a replacement. The typical architecture uses a relational database as the system of record (durable, queryable, consistent) and a key-value store as a performance layer in front of it (fast, ephemeral, simple). Understanding when to reach for each tool — and how to keep them in sync through cache invalidation strategies — is one of the core skills in designing scalable systems.
