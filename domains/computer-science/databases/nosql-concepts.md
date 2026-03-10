---
id: nosql-concepts
title: NoSQL Database Concepts
domain: computer-science
course: databases
prerequisites:
- id: relational-model-basics
  type: hard
- id: acid-properties
  type: soft
builds-toward:
- cap-theorem
- document-databases
- key-value-stores
tags:
- NoSQL
- BASE
- eventual consistency
- horizontal scaling
- schema-free
- polyglot persistence
stage: formal-systems
status: draft
---

# NoSQL Database Concepts

## Core Idea
NoSQL ('Not only SQL') databases sacrifice some ACID guarantees in exchange for horizontal scalability, flexible schemas, and high throughput on specific access patterns. Major categories include key-value stores (Redis), document databases (MongoDB), column-family stores (Cassandra), and graph databases (Neo4j). Many NoSQL systems adopt BASE semantics (Basically Available, Soft state, Eventually consistent): replicas may briefly diverge and converge asynchronously, enabling continued operation during network partitions at the cost of potential stale reads.

## How It's Best Learned
Map the same data model into a relational schema and a document schema side-by-side, then compare query and update patterns. Explore why joins are avoided in NoSQL by denormalizing data to match dominant read patterns.

## Common Misconceptions
- 'NoSQL' does not mean no SQL — many NoSQL databases support SQL-like query languages (Cassandra's CQL, BigQuery).
- NoSQL is not inherently faster than relational databases; it is optimized for different access patterns and scale dimensions.
- Eventual consistency doesn't mean data is permanently wrong; it means briefly stale reads are possible during network partitions, eventually resolving.
